'''
Challenge #20: 🎁 Vertical warehouse

In Santa's workshop, the elves are storing gifts 🎁 in a vertical warehouse. The gifts are dropped one by one through a column and start stacking up.

The warehouse is a matrix with # gifts and . empty spaces. You must create a dropGifts function that receives the warehouse state and an array with the columns where the gifts are dropped.

Falling rules:

- The gift falls through the indicated column from the top.
- It is placed in the lowest empty cell (.) of that column.
- If the column is full, the gift is ignored.

dropGifts(
  [
    ['.', '.', '.'],
    ['.', '#', '.'],
    ['#', '#', '.']
  ],
  [0]
)
/*
[
  ['.', '.', '.'],
  ['#', '#', '.'],
  ['#', '#', '.']
]
*/

dropGifts(
  [
    ['.', '.', '.'],
    ['#', '#', '.'],
    ['#', '#', '#']
  ],
  [0, 2]
)
/*
[
  ['#', '.', '.'],
  ['#', '#', '#'],
  ['#', '#', '#']
]
*/

dropGifts(
  [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
  ],
  [0, 1, 2]
)
/*
[
  ['.', '.', '.'],
  ['.', '.', '.'],
  ['#', '#', '#']
]
*/

dropGifts(
  [
    ['#', '#'],
    ['#', '#']
  ],
  [0, 0]
)
/*
[
  ['#', '#']
  ['#', '#']
]
'''

def drop_gifts_original(warehouse: list[list[str]], drops: list[int]) -> list[list[str]]:
  EMPTY = "."
  GIFT = "#"

  num_columns = len(warehouse)

  for col in drops:
    for row in range(num_columns):
      match row:
        case 0 if warehouse[row][col] == GIFT:
          break
        case _ if row > 0 and warehouse[row][col] == GIFT:
          warehouse[row-1][col] = GIFT
        case _ if row == num_columns - 1 and warehouse[row][col] == EMPTY:
          warehouse[row][col] = GIFT

  return warehouse

def drop_gifts(warehouse: list[list[str]], drops: list[int]) -> list[list[str]]:
    EMPTY = "."
    GIFT = "#"

    num_rows = len(warehouse)

    for col in drops:
        for row in reversed(range(num_rows)):
            if warehouse[row][col] == EMPTY:
                warehouse[row][col] = GIFT
                break

    return warehouse

# Main program
print(
  drop_gifts(
    [
      ['.', '.', '.'],
      ['.', '#', '.'],
      ['#', '#', '.']
    ],
    [0]
  ))

print(
  drop_gifts(
    [
      ['.', '.', '.'],
      ['#', '#', '.'],
      ['#', '#', '#']
    ],
    [0, 2]
  ))

print(
  drop_gifts(
    [
      ['.', '.', '.'],
      ['.', '.', '.'],
      ['.', '.', '.']
    ],
    [0, 1, 2]
  ))

print(
  drop_gifts(
    [
      ['#', '#'],
      ['#', '#']
    ],
    [0, 0]
  ))