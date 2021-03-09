#Author: Chris Todd
#Date: March 9, 2021
#Description: It's the game that everyone knows and loves, now executable in Python!!!



import random


#Function to create the display board:

def display_board(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#Function to prompt player 1 to choose 'X' or 'O':

def player_input():
    
    marker = ''
    
    while (marker != 'X' and marker != 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
        if marker != 'X' and marker != 'O':
            print("Sorry, you have entered an invalid character. Please enter either 'X' or 'O'.")

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#Function takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board

def place_marker(board, marker, position):
    board[position] = marker

#Check to see if the mark has won:

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

#Randomly choose the starting player:

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#Determine whether a space is available:

def space_check(board, position):
    
    return board[position] == ' '

#Check if the board is full:

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False #board is not full
    
    return True

#Allow player to select a board space, and validate if outside of range:

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        if position not in range(1,10):
            print("Invalid selection. You entered a value outside the accepted range.")
            print("Please make another selection.")
    
    return position

#Prompt players if they would like to play again:

def replay():
    
    return input('Do you want to play again? Enter Y or N: ').lower().startswith('y')





#Implement the above functions:

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Y or N.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        print("Thanks for playing!")
        break
