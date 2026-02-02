'''
Challenge #17: 🎄 The Christmas lights panelChallenge #17: 🎄 The Christmas lights panel

At the North Pole, they’ve set up a panel of Christmas lights 🎄✨ to decorate the workshop. Each light can be on with a color, or off.

The panel is represented as a matrix where each cell can be:

- '.' → light off
- 'R' → red light
- 'G' → green light

The elves want to know if there is a line of 4 lights of the same color that are on and aligned on the panel (only horizontal ↔ or vertical ↕). Lights that are off ('.') don’t count.

hasFourLights([
  ['.', '.', '.', '.', '.'],
  ['R', 'R', 'R', 'R', '.'],
  ['G', 'G', '.', '.', '.']
])
// true → there are 4 red lights horizontally

hasFourLights([
  ['.', 'G', '.', '.'],
  ['.', 'G', '.', '.'],
  ['.', 'G', '.', '.'],
  ['.', 'G', '.', '.']
])
// true → there are 4 green lights vertically

hasFourLights([
  ['R', 'G', 'R'],
  ['G', 'R', 'G'],
  ['G', 'R', 'G']
])
// false → there are no 4 lights of the same color in a row

Note: The board can be any size. No diagonals.
'''

def has_four_lights(board: list[list[str]]) -> bool:
    LIGHT_OFF = "."
    RED_LIGHT = "R"
    GREEN_LIGHT = "G"

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

    return four_in_a_row

# Main program
print(
  has_four_lights([
    ['.', '.', '.', '.', '.'],
    ['R', 'R', 'R', 'R', '.'],
    ['G', 'G', '.', '.', '.']
  ]))

print(
  has_four_lights([
    ['.', 'G', '.', '.'],
    ['.', 'G', '.', '.'],
    ['.', 'G', '.', '.'],
    ['.', 'G', '.', '.']
  ]))

print(
  has_four_lights([
    ['R', 'G', 'R'],
    ['G', 'R', 'G'],
    ['G', 'R', 'G']
  ]))