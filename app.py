from flask import Flask, render_template, jsonify, request
import tictactoe as ttt

app = Flask(__name__)

# Initialize game state
class TicTacToe:
    def __init__(self):
        self.board = ttt.initial_state()
        self.user_choice = None  # This stores whether user plays as 'X' or 'O'

    def reset(self):
        self.board = ttt.initial_state()
        self.user_choice = None  # Allow user to pick X or O again

    def make_move(self, i, j):
        if self.board[i][j] is ttt.EMPTY and not ttt.terminal(self.board):
            self.board = ttt.result(self.board, (i, j))
            return True
        return False

    def get_winner(self):
        return ttt.winner(self.board)

    def get_current_player(self):
        return ttt.player(self.board)

    def is_terminal(self):
        return ttt.terminal(self.board)

    def ai_move(self):
        if not ttt.terminal(self.board):
            move = ttt.minimax(self.board)
            if move:
                self.board = ttt.result(self.board, move)
                return True
        return False

    def set_user_choice(self, choice):
        self.user_choice = choice


game = TicTacToe()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    i, j = data['i'], data['j']
    
    # Make user move
    if game.make_move(i, j):
        current_player = game.get_current_player()
        winner = game.get_winner()
        is_terminal = game.is_terminal()
        
        # If game is not over and it's AI's turn, make AI move
        if not is_terminal and current_player != game.user_choice:
            if game.ai_move():
                current_player = game.get_current_player()
                winner = game.get_winner()
                is_terminal = game.is_terminal()
    
    return jsonify({
        'board': game.board, 
        'current_player': game.get_current_player(), 
        'winner': winner,
        'is_terminal': game.is_terminal()
    })

@app.route('/reset', methods=['GET'])
def reset():
    game.reset()
    return jsonify({
        'board': game.board, 
        'current_player': game.get_current_player()
    })

@app.route('/set_user_choice', methods=['POST'])
def set_user_choice():
    choice = request.json['choice']
    game.set_user_choice(choice)
    
    # If user picks O, AI (X) should play first
    if choice == ttt.O:
        game.ai_move()
    
    return jsonify({
        'board': game.board, 
        'current_player': game.get_current_player(),
        'user_choice': game.user_choice
    })

if __name__ == '__main__':
    app.run(debug=True)