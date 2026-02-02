# Challenge 13: 🏭 The assembly line

**Difficulty:** 🟡 Medium

**View:** [adventjs.dev/en/challenges/2025/13](https://adventjs.dev/en/challenges/2025/13)

## Instructions

Simulate the path of a gift inside a factory and return how it ends. To do this, you must create a function `runFactory(factory)`.

`factory` is a `string[]` where each cell can be:

- `>` `<` `^` `v`: movements.
- `.`: correct exit.

Keep in mind that **all rows have the same length** and that **there will be no other symbols**.

The gift **always starts at position (0,0)** (top left). At each step, it reads the current cell and moves according to the direction.

If it reaches a cell with a dot (`.`), it means it has correctly exited the factory.

**Result:**

Return one of these values:

- `'completed'`: if it reaches a `.`.
- `'loop'`: if it visits a position twice.
- `'broken'`: if it goes outside the board.

## 🧩 Examples

```javascript
runFactory([
  '>>.'
]) // 'completed'

runFactory([
  '>>>'
]) // 'broken'

runFactory([
  '>><'
]) // 'loop'

runFactory([
  '>>v',
  '..<'
]) // 'completed'

runFactory([
  '>>v',
  '<<<'
]) // 'broken'

runFactory([
  '>v.',
  '^..'
]) // 'completed'

runFactory([
  'v.',
  '^.'
]) // 'loop'
```

## Solution

<details hide>

<summary><h3>Spoiler</h3></summary>

``` python
def run_factory(factory: list[str]) -> str:
    directions = {
        ">": (0, 1),  
        "<": (0, -1),  
        "^": (-1, 0),  
        "v": (1, 0)  
    }
    CORRECT_EXIT = "."

    current_position = (0, 0)
    visited_positions = set()
    factory_grid = [list(row) for row in factory]
    num_rows, num_columns = len(factory_grid), len(factory_grid[0])

    while True:
        x, y = current_position

        if x < 0 or y < 0 or x >= num_rows or y >= num_columns:
            return "broken"

        if current_position in visited_positions:
            return "loop"

        visited_positions.add(current_position)

        cell = factory_grid[x][y]
        if cell == CORRECT_EXIT:
            return "completed" 
        elif cell in directions:
            dx, dy = directions[cell]
            current_position = (x + dx, y + dy) 
        else:
            return "broken"
```

</details>
