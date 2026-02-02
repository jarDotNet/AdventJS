'''
Challenge #23: 🎁 Gift route

Santa Claus 🎅 has to deliver presents in a town represented as a grid map.

Each cell on the map can be:

- 'S' → Santa's starting point (where the presents are)
- 'G' → House that must receive a present
- '.' → Free path
- '#' → Obstacle (cannot be crossed)

Santa makes independent deliveries for each present. He leaves from 'S', delivers the present to a house 'G', and immediately returns to 'S' to pick up the next one. However, for this challenge, we only want to calculate the sum of the minimum one-way distances from 'S' to each house 'G'.

🎯 Your goal

Write the function minStepsToDeliver(map) that returns the total number of steps required to reach all the houses with presents from the starting position.

Keep in mind:

You always start from the initial position 'S'.
For each present, you must calculate the minimum distance from 'S' to that house 'G'.
Obstacles ('#') cannot be crossed.
If any house with a present is unreachable, the function must return -1.

🧩 Examples

minStepsToDeliver([
  ['S', '.', 'G'],
  ['.', '#', '.'],
  ['G', '.', '.']
])
// Result: 4

/* 
Explanation:
- Minimum distance from S (0,0) to G (0,2): 2 steps
- Minimum distance from S (0,0) to G (2,0): 2 steps
- Total: 2 + 2 = 4
*/

minStepsToDeliver([
  ['S', '#', 'G'],
  ['#', '#', '.'],
  ['G', '.', '.']
])
// Result: -1
// (The house at (0,2) is unreachable due to obstacles)

minStepsToDeliver([['S', 'G']])
// Result: 1

🎯 Rules

- The map always contains exactly one 'S'.
- There can be zero or more houses with presents ('G').
- The order of deliveries doesn't matter, as each is measured independently from 'S'.
- You must return the sum of the minimum one-way distances.

🧠 Hint

- Calculate the shortest distance from 'S' to each 'G' (you can use a Breadth-First Search or BFS algorithm).
- If any present has no possible path, the total result is -1.
'''

from collections import deque

def min_steps_to_deliver(map):
    STARTING_POINT = 'S'
    HOUSE = 'G'
    OBSTACLE = '#'
    
    num_rows = len(map)
    num_columns = len(map[0])

    start = None
    houses = []
    
    for row in range(num_rows):
        for col in range(num_columns):
            if map[row][col] == STARTING_POINT:
                start = (row, col)
            elif map[row][col] == HOUSE:
                houses.append((row, col))
    
    if not start:
        return -1
    
    # Helper function: Perform BFS to find the shortest path from 'S' to a specific 'G'
    def bfs(start_row, start_col, target_row, target_col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        queue = deque([(start_row, start_col, 0)])  # (current_row, current_col, steps)
        visited = [[False]*num_columns for _ in range(num_rows)]  # Track visited cells
        visited[start_row][start_col] = True

        while queue:
            row, col, steps = queue.popleft()

            # If we reach the target house
            if (row, col) == (target_row, target_col):
                return steps

            # Explore neighbors
            for drow, dcol in directions:
                new_row, new_col = row + drow, col + dcol
                if (0 <= new_row < num_rows and 0 <= new_col < num_columns and
                    not visited[new_row][new_col] and map[new_row][new_col] != OBSTACLE):
                    queue.append((new_row, new_col, steps + 1))
                    visited[new_row][new_col] = True

        # If the target house is unreachable
        return -1

    # Calculate total steps required to reach all houses
    total_steps = 0
    for house_row, house_col in houses:
        distance = bfs(start[0], start[1], house_row, house_col)
        if distance == -1:  # If any house is unreachable, return -1
            return -1
        total_steps += distance

    return total_steps

# Main program
print(
  min_steps_to_deliver([
  ['S', '.', 'G'],
  ['.', '#', '.'],
  ['G', '.', '.']
]))

print(
  min_steps_to_deliver([
  ['S', '#', 'G'],
  ['#', '#', '.'],
  ['G', '.', '.']
]))

print(
  min_steps_to_deliver([['S', 'G']]))