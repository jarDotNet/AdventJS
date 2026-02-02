'''
Challenge #22: 🎄 The sleigh maze

Santa Claus 🎅 is testing a new sleigh simulator inside a maze in the workshop. The maze is represented as a matrix of characters.

Your task is to implement a function that determines if it is possible to reach the exit (E) starting from the initial position (S).

Maze rules:

- S: Santa's initial position.
- E: Maze exit.
- .: Free path.
- #: Wall (blocks the path).
- Allowed movements: up, down, left, and right.
- There is only one S and one E.

canEscape([
  ['S', '.', '#', '.'],
  ['#', '.', '#', '.'],
  ['.', '.', '.', '.'],
  ['#', '#', '#', 'E']
])
// → true

canEscape([
  ['S', '#', '#'],
  ['.', '#', '.'],
  ['.', '#', 'E']
])
// → false

canEscape([
  ['S', 'E']
])
// → true

canEscape([
  ['S', '.', '.', '.', '.'],
  ['#', '#', '#', '#', '.'],
  ['.', '.', '.', '.', '.'],
  ['.', '#', '#', '#', '#'],
  ['.', '.', '.', '.', 'E']
])
// → true

canEscape([
  ['S', '.', '.'],
  ['.', '.', '.'],
  ['#', '#', '#'],
  ['.', '.', 'E']
])
// → false

Things to keep in mind:

- You don't need to return the path, just if it is possible to arrive.
- Santa cannot leave the boundaries of the maze.
- You can pass through the same cell multiple times.

Tip: This problem can be solved in several ways, but search algorithms like BFS (Breadth-First Search) or DFS (Depth-First Search) are ideal for these types of challenges.
'''

from collections import deque

def can_escape(maze: list[list[str]]) -> bool:
  INITIAL_POSITION = "S"
  MAZE_EXIT = "E"
  WALL = "#"

  num_rows = len(maze)
  num_columns = len(maze[0])
  initial_position = next(
    (x, y) for x in range(num_rows) for y in range(num_columns) if maze[x][y] == INITIAL_POSITION
  )

  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  (start_row, start_col) = initial_position
  queue = deque([(start_row, start_col)])
  visited = [[False]*num_columns for _ in range(num_rows)]
  visited[start_row][start_col] = True

  while queue:
    row, col = queue.popleft()
    if maze[row][col] == MAZE_EXIT:
      return True
    
    for drow, dcol in directions:
        new_row, new_col = row + drow, col + dcol
        if (0 <= new_row < num_rows and 0 <= new_col < num_columns and
            not visited[new_row][new_col] and maze[new_row][new_col] != WALL):
            queue.append((new_row, new_col))
            visited[new_row][new_col] = True

  return False

# Main program
print(
  can_escape([
  ['S', '.', '#', '.'],
  ['#', '.', '#', '.'],
  ['.', '.', '.', '.'],
  ['#', '#', '#', 'E']
]))

print(
  can_escape([
  ['S', '#', '#'],
  ['.', '#', '.'],
  ['.', '#', 'E']
]))

print(
  can_escape([
  ['S', 'E']
]))

print(
  can_escape([
  ['S', '.', '.', '.', '.'],
  ['#', '#', '#', '#', '.'],
  ['.', '.', '.', '.', '.'],
  ['.', '#', '#', '#', '#'],
  ['.', '.', '.', '.', 'E']
]))

print(
  can_escape([
  ['S', '.', '.'],
  ['.', '.', '.'],
  ['#', '#', '#'],
  ['.', '.', 'E']
]))