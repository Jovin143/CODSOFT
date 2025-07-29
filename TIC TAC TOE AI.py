# Project: TIC TAC TOE AI
# Created by: [NIBSHAN JOVIN JOSEPH]
# Date: [23-07-2025]


#In the game the player is being marked as 'X' and computer is being marked as 'O':


game_board = [" " for _ in range(9)]

player_score = 0
ai_score = 0
draws = 0

player_name = input("Entering your name: ")
print(f"\nHi {player_name}! You are playing as 'X'. The AI is playing as 'O'. Let’s begin!\n")

def display_board():
    for row in range(3):
        print(" ", game_board[row*3], "|", game_board[row*3+1], "|", game_board[row*3+2])
        if row < 2:
            print("----+-----+----")


def player_has_won(symbol):
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combos:
        if game_board[combo[0]] == symbol and game_board[combo[1]] == symbol and game_board[combo[2]] == symbol:
            return True
    return False

def is_board_full():
    return " " not in game_board

def minimax_decision(is_ai_turn):
    if player_has_won("O"):
        return 1
    if player_has_won("X"):
        return -1
    if is_board_full():
        return 0

    if is_ai_turn:
        best_score = -999
        for pos in range(9):
            if game_board[pos] == " ":
                game_board[pos] = "O"
                score = minimax_decision(False)
                game_board[pos] = " "
                if score > best_score:
                    best_score = score
        return best_score
    else:
        worst_score = 999
        for pos in range(9):
            if game_board[pos] == " ":
                game_board[pos] = "X"
                score = minimax_decision(True)
                game_board[pos] = " "
                if score < worst_score:
                    worst_score = score
        return worst_score

def ai_turn():
    best_score = -999
    move = -1
    for pos in range(9):
        if game_board[pos] == " ":
            game_board[pos] = "O"
            score = minimax_decision(False)
            game_board[pos] = " "
            if score > best_score:
                best_score = score
                move = pos
    game_board[move] = "O"

def user_turn():
    while True:
        try:
            move = int(input(f"{player_name}, choosing your move (0–8): "))
            if game_board[move] == " ":
                game_board[move] = "X"
                break
            else:
                print("That spot is already being taken. Try again.")
        except:
            print("Please enter a valid number between 0 and 8.")


def reset_board():
    for i in range(9):
        game_board[i] = " "

def start_game():
    global player_score, ai_score, draws
    playing = True

    while playing:
        reset_board()
        print("\n=== Starting a game of Tic-Tac-Toe ===")
        display_board()

        while True:
            user_turn()
            display_board()
            if player_has_won("X"):
                print(f"Congratulations {player_name}, you are beating the AI.")
                player_score += 1
                break
            if is_board_full():
                print("It's ending in a draw.")
                draws += 1
                break

            print("AI is thinking...\n")
            ai_turn()
            display_board()
            if player_has_won("O"):
                print("The AI is winning. Better luck next time.")
                ai_score += 1
                break
            if is_board_full():
                print("It's ending in a draw.")
                draws += 1
                break

        print(f"\nScoreboard:")
        print(f"{player_name}'s Wins: {player_score} | AI Wins: {ai_score} | Draws: {draws}")

        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing! Goodbye.")
            playing = False

# starting  the game
start_game()
