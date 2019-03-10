def display_board(board):
    print('\n'*100)
    print (' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print ('-----------')
    print (' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print ('-----------')
    print (' '+board[1]+' | '+board[2]+' | '+board[3]+' ')

def player_input():
    #Getting correct input from Player 1
    player_one = input("Player 1, please enter X or O: ")
    player_one = player_one.upper()
    while (player_one != 'X' and player_one != 'O'):
        player_one = input("Player 1, please enter X or O: ")
        player_one = player_one.upper()
    
    #Assigning Player 2
    if player_one == 'X':
        player_two = 'O'
    else:
        player_two = 'X'
            
    #Printing Player Selections
    print (f"Player 1 has selected: {player_one}")    
    print (f"Player 2 will be: {player_two}")
    
    return player_one, player_two

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return( (board[7] == board[8] == board[9] == marker) or #top row check
    (board[4] == board[5] == board[6] == marker) or #middle row check
    (board[1] == board[2] == board[3] == marker) or #bottom row check
    (board[7] == board[4] == board[1] == marker) or #left column check
    (board[8] == board[5] == board[2] == marker) or #middle column check
    (board[9] == board[6] == board[3] == marker) or #right row check
    (board[7] == board[5] == board[3] == marker) or #first diagonal check
    (board[9] == board[5] == board[1] == marker)) #second diagonal check

def choose_first(player_list):
    import random
    player_list = ["Player 1", "Player 2"]
    first_player = random.choice(player_list)
    print ("{0} will go first!".format(first_player))
    return first_player

def space_check(board, position):
    return (board[position] != 'X' and board[position] != 'O')

def full_board_check(board):
    for i in range(1,10):
        if board[i] == 'X' or board[i] == 'O':
            marker_count += marker_count + 1
    return (marker_count == 9)

def player_choice(board):
    position = int(input('Please enter a number 1-9: '))
    while space_check(board, position) != True:
        position = (int(input('Position taken, please enter another number 1-9: ')))
    return int(position)

def replay():
    player_response = input("Do you want to play again? (Y/N): ")
    player_response = player_response.upper()
    while player_response != 'Y' and player_response != 'N':
        player_response = input("Please enter a valid selection (Y/N): ")
        player_response = player_response.upper()
    
    if player_response == 'Y':
        return (player_response == 'Y')

print('Welcome to Tic Tac Toe!')

#asks the players which marker they would like to be and assigns variables
player1_marker, player2_marker = player_input()

#displays a new board
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(board)

#randomly selects which player will go first
player_list = ["Player 1", "Player 2"]
first_player = choose_first(player_list)

#First move    
if first_player == "Player 1":
    position = player_choice(board)
    board[position] = player1_marker
    place_marker(board,player1_marker,position)
    display_board(board)
    player1_turn = False
else:
    position = player_choice(board)
    board[position] = player2_marker
    place_marker(board,player2_marker,position)
    display_board(board)
    player1_turn = True

while (full_board_check(board) != True) and (win_check(board,player1_marker) != True or win_check(board,player2_marker)):
    if player1_turn == True:
        print ("Player 1's turn")
        position = player_choice(board)
        board[position] = player1_marker
        place_marker(board,player1_marker,position)
        display_board(board)
        if win_check(board,player1_marker) == True:
            print ("Player 1 wins!")
        player1_turn = False
    elif player1_turn == False:
        print ("Player 2's turn")
        position = player_choice(board)
        board[position] = player2_marker
        place_marker(board,player2_marker,position)
        display_board(board)
        if win_check(board,player2_marker) == True:
            print ("Player 2 wins!")
        player1_turn = True
    
if not replay():
    print ("Thanks for playing, come back again!")