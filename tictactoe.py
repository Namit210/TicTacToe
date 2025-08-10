import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count > o_count:
        return O
    elif o_count > x_count:
        return X
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                actions_set.add((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")
    new_board = [row[:] for row in board]  # Create a copy of the board
    i, j = action
    current_player = player(board)
    new_board[i][j] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None  # No winner yet


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if all(cell is not EMPTY for row in board for cell in row):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0  # No winner or draw


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)

    if current_player == X:
        # Maximize for X
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value = minimax_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    else:
        # Minimize for O
        best_value = math.inf
        best_action = None
        for action in actions(board):
            value = minimax_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action


def minimax_value(board):
    """
    Returns the minimax value of the board for the current player.
    """
    if terminal(board):
        return utility(board)
    
    if player(board) == X:
        # Maximize for X
        best_value = -math.inf
        for action in actions(board):
            value = minimax_value(result(board, action))
            best_value = max(best_value, value)
        return best_value
    else:  # O's turn, minimize
        best_value = math.inf
        for action in actions(board):
            value = minimax_value(result(board, action))
            best_value = min(best_value, value)
        return best_value
