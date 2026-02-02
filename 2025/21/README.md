# Challenge 21: 🤖 The cleaning robot

**Difficulty:** 🟡 Medium

**View:** [adventjs.dev/en/challenges/2025/21](https://adventjs.dev/en/challenges/2025/21)

## Instructions

Santa's vertical warehouse has been modernized! Now, in addition to stacking gifts, there's a **robot 🤖** in the warehouse that picks up the gifts if there is a complete row.

The warehouse is a matrix with `#` gifts and `.` empty spaces. You must create a `clearGifts` function that receives the state of the warehouse and an array with the columns where the gifts are dropped.

### Drop rules

- The gift falls down the indicated column from the top.
- It is placed in the **lowest empty cell** (`.`) of that column.
- If the column is full, the gift is ignored.

### Cleaning robot rule

- If when placing a gift, a row becomes completely filled with gifts (`#`), that row **disappears**.
- All the rows that were above the removed row **move down one position**.
- When a row is removed, a new empty row (`.`) appears at the top to keep the warehouse size.

## 🧩 Examples

```javascript
clearGifts(
  [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['#', '.', '#']
  ],
  [1]
)
/*
1. The gift falls in column 1
2. Row 2 becomes [# # #].
3. Row 2 is complete, the robot clears it.
6. A new empty row is added at position 0.

Result:
[
  ['.', '.', '.'],
  ['.', '.', '.'],
  ['.', '.', '.']
]
*/

clearGifts(
  [
    ['.', '.', '#'],
    ['#', '.', '#'],
    ['#', '.', '#']
  ],
  [0, 1, 2]
)

/*
1. The gift falls in column 0
2. The gift falls in column 1
3. Row 2 becomes [# # #]
4. Row 2 is complete, the robot clears it

For now it looks like this:
[
  ['.', '.', '.']
  ['#', '.', '#'],
  ['#', '.', '#'],
]

5. The gift falls in column 2

Result:
[
  ['.', '.', '#'],
  ['#', '.', '#'],
  ['#', '.', '#']
]
*/
```

## Solution

<details hide>

<summary><h3>Spoiler</h3></summary>

``` python
def clear_gifts(warehouse: list[list[str]], drops: list[int]) -> list[list[str]]:
  EMPTY = "."
  GIFT = "#"

  if not warehouse:
    return warehouse

  num_rows = len(warehouse)
  num_cols = len(warehouse[0])

  empty_row = [EMPTY for _ in range(num_cols)]
  full_row = [GIFT for _ in range(num_cols)]

  for col in drops:
    for row in reversed(range(num_rows)):
        if warehouse[row][col] == EMPTY:
            warehouse[row][col] = GIFT

            if warehouse[row] == full_row:
                warehouse.pop(row)
                warehouse.insert(0, empty_row.copy())
            break

  return warehouse
```

</details>
