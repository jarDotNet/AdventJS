'''
Challenge #18: 🎄 Lights in line with diagonals

The Christmas lights panel 🎄✨ in the workshop has been a total success. But the elves want to go one step further: now they want to detect whether there is a line of 4 lights of the same color also on a diagonal.

The panel is still a matrix where each cell can be:

- '.' → light off
- 'R' → red light
- 'G' → green light

Now your function must return true if there is a line of 4 lights of the same color that are on and aligned, whether horizontally ↔, vertically ↕ or diagonally ↘↙.

hasFourInARow([
  ['R', '.', '.', '.'],
  ['.', 'R', '.', '.'],
  ['.', '.', 'R', '.'],
  ['.', '.', '.', 'R']
])
// true → there are 4 red lights in a ↘ diagonal

hasFourInARow([
  ['.', '.', '.', 'G'],
  ['.', '.', 'G', '.'],
  ['.', 'G', '.', '.'],
  ['G', '.', '.', '.']
])
// true → there are 4 green lights in a ↙ diagonal

hasFourInARow([
  ['R', 'R', 'R', 'R'],
  ['G', 'G', '.', '.'],
  ['.', '.', '.', '.'],
  ['.', '.', '.', '.']
])
// true → there are 4 red lights in a horizontal line

hasFourInARow([
  ['R', 'G', 'R'],
  ['G', 'R', 'G'],
  ['G', 'R', 'G']
])
// false → there are no 4 consecutive lights of the same color

Note: The board can be any size.
'''

def has_four_in_a_row(board: list[list[str]]) -> bool:
    LIGHT_OFF = "."

    ROWS = len(board)
    COLS = len(board[0])

    four_in_a_row = False

    for row in range(ROWS):
        for col in range(COLS):
            # Check horizontal (left-to-right)
            if col + 3 < COLS and (board[row][col] is not LIGHT_OFF):
                if (board[row][col] == board[row][col + 1] == 
                    board[row][col + 2] == board[row][col + 3]):
                    four_in_a_row = True
                    break

            # Check vertical (top-to-bottom)
            if row + 3 < ROWS and (board[row][col] is not LIGHT_OFF):  
                if (board[row][col] == board[row + 1][col] == 
                    board[row + 2][col] == board[row + 3][col]):
                    four_in_a_row = True
                    break

            # Check diagonal (top-left to bottom-right)
            if row + 3 < ROWS and col + 3 < COLS and (board[row][col] is not LIGHT_OFF):
                if (board[row][col] == board[row + 1][col + 1] == 
                    board[row + 2][col + 2] == board[row + 3][col + 3]):
                    four_in_a_row = True
                    break

            # Check diagonal (top-right to bottom-left)
            if row + 3 < ROWS and col - 3 >= 0 and (board[row][col] is not LIGHT_OFF):
                if (board[row][col] == board[row + 1][col - 1] == 
                    board[row + 2][col - 2] == board[row + 3][col - 3]):
                    four_in_a_row = True
                    break

    return four_in_a_row

# Main program
print(
  has_four_in_a_row([
    ['R', '.', '.', '.'],
    ['.', 'R', '.', '.'],
    ['.', '.', 'R', '.'],
    ['.', '.', '.', 'R']
  ]))

print(
  has_four_in_a_row([
    ['.', '.', '.', 'G'],
    ['.', '.', 'G', '.'],
    ['.', 'G', '.', '.'],
    ['G', '.', '.', '.']
  ]))

print(
  has_four_in_a_row([
    ['R', 'R', 'R', 'R'],
    ['G', 'G', '.', '.'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.']
  ]))

print(
  has_four_in_a_row([
    ['R', 'G', 'R'],
    ['G', 'R', 'G'],
    ['G', 'R', 'G']
  ]))