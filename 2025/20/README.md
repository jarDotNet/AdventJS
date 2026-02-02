# Challenge 20: 🎁 Vertical warehouse

**Difficulty:** 🟢 Easy
**View:** [adventjs.dev/en/challenges/2025/20](https://adventjs.dev/en/challenges/2025/20)

## Instructions

In Santa's workshop, the elves are storing gifts 🎁 in a **vertical warehouse**. The gifts are dropped one by one through a column and start stacking up.

The warehouse is represented as a **matrix** where:

- `#` represents a gift.
- `.` represents an empty space.

You must create a `dropGifts` function that receives the current warehouse state and an array with the indices of the columns where the gifts are dropped.

**Falling rules:**

- The gift falls through the indicated column from the top.
- It is placed in the **lowest empty cell** (`.`) of that column.
- If the column is already full (no empty spaces), the gift is ignored and not added.

## 🧩 Examples

```javascript
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
    ['#', '#']
    ['#', '#']
  ],
  [0, 0]
)
/*
[
  ['#', '#']
  ['#', '#']
]
```

## Solution

<details hide>

<summary><h3>Spoiler</h3></summary>

``` python
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
```

</details>
