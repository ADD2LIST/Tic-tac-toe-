import streamlit as st

import random

# Function to check if any player has won

def check_win(board, player):

    # Check rows

    for i in range(3):

        if board[i][0] == board[i][1] == board[i][2] == player:

            return True

    # Check columns

    for i in range(3):

        if board[0][i] == board[1][i] == board[2][i] == player:

            return True

    # Check diagonals

    if board[0][0] == board[1][1] == board[2][2] == player:

        return True

    if board[0][2] == board[1][1] == board[2][0] == player:

        return True

    return False

# Function to make a move for the computer

def make_computer_move(board, computer_player):

    # Check if the computer can win in the next move

    for i in range(3):

        for j in range(3):

            if board[i][j] == "-":

                board[i][j] = computer_player

                if check_win(board, computer_player):

                    return

                # Undo the move if it doesn't lead to a win

                board[i][j] = "-"

    # Check if the user can win in the next move

    for i in range(3):

        for j in range(3):

            if board[i][j] == "-":

                board[i][j] = "X"

                if check_win(board, "X"):

                    board[i][j] = computer_player

                    return

                # Undo the move if it doesn't lead to a win

                board[i][j] = "-"

    # If no winning move is possible, make a random move

    while True:

        i = random.randint(0, 2)

        j = random.randint(0, 2)

        if board[i][j] == "-":

            board[i][j] = computer_player

            return

# Function to reset the game

def reset_game():

    return [["-" for _ in range(3)] for _ in range(3)]

# Main game logic

def play_game():

    st.title("Tic Tac Toe")

    board = reset_game()

    player = "X"

    game_over = False

    while not game_over:

        st.write("Current Player: ", player)

        # User's turn

        if player == "X":

            row = st.slider("Select row (0, 1, or 2)", 0, 2)

            col = st.slider("Select column (0, 1, or 2)", 0, 2)

            if board[row][col] == "-":

                board[row][col] = player

                st.write("User placed", player, "at", (row, col))

                player = "O"

            else:

                st.warning("Invalid move! Try again.")

        # Computer's turn

        else:

            make_computer_move(board, player)

            st.write("Computer placed", player)

            player = "X"

        st.write("---------")

        for row in board:

            st.write("|".join(row))

            st.write("---------")

        # Check for a win or draw

        if check_win(board, "X"):

            st.success("User wins!")

            game_over = True

        elif check_win(board, "O"):

            st.error("Computer wins!")

            game_over = True

        elif all(all(cell != "-" for cell in row) for row in board):

            st.warning("It's a draw!")

            game_over = True

    st.button("Play Again", on_click=reset_game)

# Start the game

play_game()

