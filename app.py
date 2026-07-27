from flask import Flask, render_template, jsonify, request
import tictactoe as ttt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_user_choice', methods=['POST'])
def set_user_choice():
    data = request.json or {}
    choice = data.get('choice')
    board = ttt.initial_state()
    
    # If user picks O, AI (X) plays first move
    if choice == ttt.O:
        move = ttt.minimax(board)
        if move:
            board = ttt.result(board, move)
            
    return jsonify({
        'board': board, 
        'current_player': ttt.player(board),
        'user_choice': choice,
        'winner': ttt.winner(board),
        'is_terminal': ttt.terminal(board)
    })

@app.route('/move', methods=['POST'])
def move():
    data = request.json or {}
    board = data.get('board')
    user_choice = data.get('user_choice')
    i, j = data.get('i'), data.get('j')
    
    # Process User Move
    if board[i][j] is ttt.EMPTY and not ttt.terminal(board):
        board = ttt.result(board, (i, j))
        
        # If game is not over and it's AI's turn, make AI move
        if not ttt.terminal(board) and ttt.player(board) != user_choice:
            move = ttt.minimax(board)
            if move:
                board = ttt.result(board, move)

    return jsonify({
        'board': board, 
        'current_player': ttt.player(board), 
        'winner': ttt.winner(board),
        'is_terminal': ttt.terminal(board)
    })

if __name__ == '__main__':
    app.run(debug=True)
