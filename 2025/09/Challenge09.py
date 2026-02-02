'''
Challenge #9: 🦌 The reno robot aspirator

The elves have built a robot vacuum reindeer 🦌 (@) to tidy up the workshop a bit before Christmas.

The reindeer moves on a board to pick things up off the floor (*) and must avoid obstacles (#).

You will receive two parameters:

- board: a string that represents the board.
- moves: a string with the movements: 'L' (left), 'R' (right), 'U' (up), 'D' (down).

Movement rules:

- If the reindeer picks something up off the floor (*) during the moves → return 'success'.
- If the reindeer goes off the board or crashes into an obstacle (#) → return 'crash'.
- If the reindeer neither picks anything up nor crashes → return 'fail'.

Keep in mind that if the reindeer picks something up off the floor, it is already 'success', regardless of whether in later moves it crashes into an obstacle or goes off the board.

Important: Keep in mind that in the board the first and last lines are blank and must be discarded.

Example:

const board = `
.....
.*#.*
.@...
.....
`

moveReno(board, 'D')
// ➞ 'fail' -> it moves but doesn't pick anything up

moveReno(board, 'U')
// ➞ 'success' -> it picks something up (*) right above

moveReno(board, 'RU')
// ➞ 'crash' -> it crashes into an obstacle (#)

moveReno(board, 'RRRUU')
// ➞ 'success' -> it picks something up (*)

moveReno(board, 'DD')
// ➞ 'crash' -> it crashes into the bottom of the board

moveReno(board, 'UUU')
// ➞ 'success' -> it picks something up off the floor (*) and then crashes at the top

moveReno(board, 'RR')
// ➞ 'fail' -> it moves but doesn't pick anything up
'''

from typing import List, Literal

def move_reno_original(board: str, moves: str) -> Literal['fail', 'crash', 'success']:
  REINDEER = "@"
  OBJECT = "*"
  OBSTACLE = "#"
  
  board_2darray = [list(row[0]) for row in (line.split() for line in board.split('\n')) if len(row) > 0]

  num_rows = len(board_2darray)
  num_columns = len(board_2darray[0])
  reindeer_position = next(
    (x, y) for x in range(num_rows) for y in range(num_columns) if board_2darray[x][y] == REINDEER
  )

  current_pos = reindeer_position
  for move in moves:
      col = current_pos[0]
      row = current_pos[1]
      match move:
        case "L":
          if row - 1 <= 0:
            return 'crash'
          elif board_2darray[col][row - 1] == OBJECT:
            return 'success'
          elif board_2darray[col][row - 1] == OBSTACLE:
            return 'crash'
          else:
            current_pos = (col, row - 1)
        case "R":
          if row + 1 >= num_columns:
            return 'crash'
          elif board_2darray[col][row + 1] == OBJECT:
            return 'success'
          elif board_2darray[col][row + 1] == OBSTACLE:
            return 'crash'
          else:
            current_pos = (col, row + 1)
        case "U":
          if col - 1 <= 0:
            return 'crash'
          elif board_2darray[col - 1][row] == OBJECT:
            return 'success'
          elif board_2darray[col - 1][row]  == OBSTACLE:
            return 'crash'
          else:
            current_pos = (col - 1, row)
        case "D":
          if col + 1 >= num_rows:
            return 'crash'
          elif board_2darray[col + 1][row] == OBJECT:
            return 'success'
          elif board_2darray[col + 1][row]  == OBSTACLE:
            return 'crash'
          else:
            current_pos = (col + 1, row)

  return 'fail'

from typing import List, Literal, Tuple

def move_reno(board: str, moves: str) -> Literal['fail', 'crash', 'success']:
    REINDEER = "@"
    OBJECT = "*"
    OBSTACLE = "#"

    board_2darray = [list(row) for row in board.split('\n') if row]

    reindeer_position = next(
        (x, y) for x, row in enumerate(board_2darray) for y, cell in enumerate(row) if cell == REINDEER
    )

    directions = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0),
    }

    current_pos = reindeer_position

    for move in moves:
        if move not in directions:
            continue

        dx, dy = directions[move]
        new_col, new_row = current_pos[0] + dx, current_pos[1] + dy

        if not (0 <= new_col < len(board_2darray) and 0 <= new_row < len(board_2darray[0])):
            return 'crash'

        cell = board_2darray[new_col][new_row]
        if cell == OBJECT:
            return 'success'
        elif cell == OBSTACLE:
            return 'crash'
        
        current_pos = (new_col, new_row)

    return 'fail'

# Main program
board = """
.....
.*#.*
.@...
.....
"""

print(move_reno(board, 'D'))
print(move_reno(board, 'U'))
print(move_reno(board, 'RU'))
print(move_reno(board, 'RRRUU'))
print(move_reno(board, 'DD'))
print(move_reno(board, 'UUU'))
print(move_reno(board, 'RR'))