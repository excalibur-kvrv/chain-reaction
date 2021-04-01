from collections import deque


class Player:
    def __init__(self, name=None, value=0):
        self.name = name
        self.value = value
        self.reactive = False
    
    def __repr__(self):
        return f'{self.name}({self.value}, {self.reactive})'

def get_player(game_board, row, column):
    return game_board[row][column].name


def out_of_bounds(game_board, row, column):
    return (row > len(game_board) - 1 or row < 0) or (column > len(game_board[0]) - 1 or column < 0)


def valid_move(game_board, player, row, column):
    if not out_of_bounds(game_board, row, column):
        occupied_player, value = game_board[row][column]
        return occupied_player.name is None or occupied_player.name == player
    return False


def increment_position(game_board, player, row, column, fn=None):
    queue = deque()
    queue.append((row, column, player))

    while queue:
        r, c, p = queue.popleft()
        
        neighbors = get_neighbors(game_board, r, c)
        
        if is_reactive_position(game_board, r, c, len(neighbors)):
            game_board[r][c] = Player()

            for neighbor in neighbors:
                queue.append((*neighbor, get_player(game_board, *neighbor)))    
        else:
            game_board[r][c].name = player
            game_board[r][c].value += 1
        
        if fn:
            fn(game_board)
       


def is_reactive_position(game_board, row, column, no_of_neighbors):
    return game_board[row][column].value + 1 == no_of_neighbors


def get_neighbors(game_board, row, column):
    neighbors = []

    if not out_of_bounds(game_board, row + 1, column):
        neighbors.append((row + 1, column))
    
    if not out_of_bounds(game_board, row - 1, column):
        neighbors.append((row - 1, column))
    
    if not out_of_bounds(game_board, row, column + 1):
        neighbors.append((row, column + 1))
    
    if not out_of_bounds(game_board, row, column - 1):
        neighbors.append((row, column - 1))
    
    return neighbors