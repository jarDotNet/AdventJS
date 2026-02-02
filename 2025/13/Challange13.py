'''
Challenge #13: 🏭 The assembly line

Simulate the path of a gift inside a factory and return how it ends. To do this, you must create a function runFactory(factory).

factory is a string[] where each cell can be:

- > < ^ v movements
- . correct exit

Keep in mind that all rows have the same length and that there will be no other symbols.

The gift always starts at position (0,0) (top left). At each step it reads the current cell and moves according to the direction. If it reaches a cell with a dot (.) it means it has correctly exited the factory.

Result

Return one of these values:

- 'completed' if it reaches a .
- 'loop' if it visits a position twice
- 'broken' if it goes outside the board

Examples

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
'''

def run_factory_original(factory: list[str]) -> str:
  RIGHT = ">" 
  LEFT = "<"
  UP = "^"
  DOWN = "v"
  CORRECT_EXIT = "."
  
  current_position = (0, 0)
  visited_positions = []

  factory_2darray = [list(row) for row in factory]
  num_rows = len(factory_2darray)
  num_columns = len(factory_2darray[0])
  
  running = True
  completed = loop = broken = False

  while running:
    (posx, posy) = current_position

    if (posx < 0 or posy < 0 or posx >= num_rows or posy >= num_columns):
      broken = True
    elif (current_position in visited_positions):
      loop = True
    else:
      cell = factory_2darray[posx][posy]

      if (cell == CORRECT_EXIT):
        completed = True
      else:
        match cell:
          case _ if cell == RIGHT:
            current_position = (posx, posy + 1)
          case _ if cell == LEFT:
            current_position = (posx, posy - 1)
          case _ if cell == UP:
            current_position = (posx - 1, posy)
          case _ if cell == DOWN:
            current_position = (posx + 1, posy)

    visited_positions.append((posx, posy))
    running = not completed and not loop and not broken

  return 'completed' if completed else ('loop' if loop else 'broken')

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
        
# Main program
print(
  run_factory([
    '>>.'
  ]))

print(
  run_factory([
    '>>>'
  ]))

print(
  run_factory([
    '>><'
  ]))

print(
  run_factory([
    '>>v',
    '..<'
  ]))

print(
  run_factory([
    '>>v',
    '<<<'
  ]))

print(
  run_factory([
    '>v.',
    '^..'
  ]))

print(
  run_factory([
    'v.',
    '^.'
  ]))