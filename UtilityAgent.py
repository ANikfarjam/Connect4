#minimax and util function
import Connect4Game
import math
import numpy as np
import random
# Function to calculate optimal pruning values (alpha and beta)
def calculate_pruning_values(maximizingPlayer, best_value, alpha, beta):
    if maximizingPlayer:
        alpha = max(alpha, best_value)
    else:
        beta = min(beta, best_value)
    return alpha, beta

# Your existing minimax function remains the same, just add pruning value calculations
def minimax(board, depth, alpha, beta, maximizingPlayer):
    AI_Peace = 0
    Player_Peace = 1
    valid_locations = []
    for col in range(board.shape[1]):  # Corrected the range
        valid_locations.append(Connect4Game.get_next_open_row(board, col), col)
        is_terminal = Connect4Game.game_over

    # Base case: If the depth is zero or the game is over, return the current board's score.
    if depth == 0 or is_terminal:
        if is_terminal:
            if Connect4Game.winning_move(board, AI_Peace): #ai peace is 0 
                return (None, math.inf)
            elif Connect4Game.winning_move(board, Player_Peace):#played peace
                return (None, -math.inf)
            else: # Game is over, no more valid moves
                return (None, 0)
        else: # Depth is zero
            return (None, util_function(board, AI_Peace))

    # Maximize the score if it's the maximizing player's turn
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = Connect4Game.get_next_open_row(board, col)
            b_copy = board.copy()
            Connect4Game.drop_piece(b_copy, row, col, 0)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]

            # Update the best move
            if new_score > value:
                value = new_score
                column = col
            
            # Calculate pruning values
            alpha, beta = calculate_pruning_values(maximizingPlayer, value, alpha, beta)

            # Prune the search if the alpha value is greater than or equal to beta.
            if alpha >= beta:
                break
        return column, value

    else: # Minimize the score if it's the minimizing player's turn.
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = Connect4Game.get_next_open_row(board, col)
            b_copy = board.copy()
            Connect4Game.drop_piece(b_copy, row, col, Player_Peace)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]

            # Update the best move
            if new_score < value:
                value = new_score
                column = col
            
            # Calculate pruning values
            alpha, beta = calculate_pruning_values(maximizingPlayer, value, alpha, beta)

            # Prune the search if the alpha value is greater than or equal to beta
            if alpha >= beta:
                break
        return column, value
def util_function(board, piece):
    score = 0
    opponent_piece = 1

    # Evaluation board for scoring positions on the actual game board.

    # TODO: Fill in values for this board. Give higher values to the positions that you think
    # lead to more wins, and lower values to the positions you think can result in less winning combinations.
    evaluation_board = np.array([[0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0]])


    # Calculate scores for the given player's and opponent's pieces on the board.
    piece_score = np.sum(evaluation_board[board == piece])
    opponent_score = np.sum(evaluation_board[board == opponent_piece])

    # Calculate the final score by subtracting the opponent's score from the player's score.
    score = piece_score - opponent_score
    return score

