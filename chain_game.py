from chain_game_rules import *
from time import sleep
from collections import defaultdict

PLAYERS_COLORS = [
    'Red', 'Green', 'Light Blue', 'Dark Blue', 'Orange', 'Pink', 'White', 'Yellow'
]



def print_board(board):
    print('**********************game state*********************')

    for row in board:
        print(*row)
    
    print()


def create_new_board():
    row_no, column_no = map(int, input('Enter row, column ').split())

    game_board = []
    for _ in range(row_no):
        row = []
        for _ in range(column_no):
            row.append(Player())
        game_board.append(row)

    return game_board


def get_player_no():
    player_no = int(input('Enter a player number:-\n'))
    
    if player_no < 2:
        print('Please enter again')
        return get_player_no()

    print(f'Playing with {player_no} players')
    return player_no


def get_ai_player(players):
    for index, player in enumerate(players, start=1):
        print(index, player)
    
    ai_player = int(input('Select which player will be the AI ')) - 1
    if ai_player > len(players) - 1 or ai_player < 0:
        print('Enter a valid choice')
        return get_ai_player()
    
    print(f'AI will play with {players[ai_player]}')
    return ai_player


def is_game_active(game_board, no_of_players):
    player_map = defaultdict()
    for row in game_board:
        for p in row:
            if p.name:
                if p.name in player_map:
                    player_map[p.name] += 1
                else:
                    player_map[p.name] = 1
    
    in_game = [player for player in player_map if player_map[player] != 0] or []
    if len(in_game) == 1:
        return False
    return True


def game():
    game_board = create_new_board()
    print_board(game_board)

    player_no = get_player_no()
    players = PLAYERS_COLORS[:player_no]
    ai_player = get_ai_player(players)

    for player in players:
            print(f'{player} turn')
            
            r, c = map(int, input('Enter row, column ').split())
            while not valid_move(game_board, player, r, c):
                print('Please Enter a valid position')
                try:
                    r, c = map(int, input('Enter row, column ').split())
                except:
                    print('Please Enter a valid position')
            
            increment_position(game_board, player, r, c, log)
            print_board(game_board)

    while True:
        for player in players:
            print(f'{player} turn ************************')
            
            r, c = map(int, input('Enter row, column ').split())
            while not valid_move(game_board, player, r, c):
                print('Please enter a valid position')
                r, c = map(int, input('Enter row, column ').split())
            
            increment_position(game_board, player, r, c, log)
            print_board(game_board)

            if not is_game_active(game_board, player_no):
                print('Game Over')
                return
