board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']


def game():
    game_on = True
    player = "X"
    display_board()
    while game_on:
        move(player)
        if check_if_win(player):
            print("Player {} win!".format(player))
            game_on = False
        elif check_if_tie():
            print("Tie!")
            game_on = False
        player = change_players(player)


def check_if_tie():
    if ' ' not in board:
        return True
    else:
        return False


def check_if_win(player):
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] == player:
            return True
        elif board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    elif board[2] == board[4] == board[6] == player:
        return True
    else:
        return False


def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def move(player):
    not_taken = True
    while not_taken:
        choice = int(input('{} move (1-9): '.format(player))) - 1
        print(board[choice])
        if board[choice] == ' ':
            board[choice] = player
            not_taken = False
        else:
            print("Bad move!")
        display_board()


def change_players(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'


game()
