# Challenge 11: 📹 Unwatched gifts

**Difficulty:** 🟢 Easy

**View:** [adventjs.dev/en/challenges/2025/11](https://adventjs.dev/en/challenges/2025/11)

## Instructions

The Grinch wants to steal the Christmas presents from the warehouse. To do this, he needs to know **which presents are not under surveillance**.

The warehouse is represented as an array of strings (`string[]`), where **each present (`*`) is protected if its position is next to a camera (`#`)**. Each empty space is represented with a **dot (`.`)**.

Your task is to **count how many presents are not under surveillance**, meaning they do not have any adjacent camera (up, down, left, or right).

**Keep in mind:** _only the 4 cardinal directions are considered "adjacent", not diagonals_.

Presents in the corners or at the edges can be unguarded, as long as they do not have cameras directly next to them.

## 🧩 Examples

```javascript
findUnsafeGifts([
  '.*.',
  '*#*',
  '.*.'
]) // ➞ 0

// All presents are next to a camera

findUnsafeGifts([
  '...',
  '.*.',
  '...'
]) // ➞ 1

// This present has no cameras around

findUnsafeGifts([
  '*.*',
  '...',
  '*#*'
]) // ➞ 2
// The presents in the top corners have no cameras around

findUnsafeGifts([
  '.....',
  '.*.*.',
  '..#..',
  '.*.*.',
  '.....'
]) // ➞ 4

// The four presents have no cameras, because they are diagonal to the camera
```

## Solution

<details hide>

<summary><h3>Spoiler</h3></summary>

``` python
def find_unsafe_gifts(warehouse: list[str]) -> int:
    PRESENT = "*"
    CAMERA = "#"
    
    warehouse_2darray = [list(row) for row in warehouse]

    num_rows = len(warehouse_2darray)
    num_columns = len(warehouse_2darray[0])

    surveillance = set()
    for x in range(num_rows):
        for y in range(num_columns):
            if warehouse_2darray[x][y] == CAMERA:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
                    surveillance.add((x + dx, y + dy))

    unsafe_gifts = 0
    for x in range(num_rows):
        for y in range(num_columns):
            if warehouse_2darray[x][y] == PRESENT and (x, y) not in surveillance:
                unsafe_gifts += 1

    return unsafe_gifts
```

</details>
