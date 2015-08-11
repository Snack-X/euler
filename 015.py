SIZE = 20

grid = [[1 for _ in range(SIZE + 1)] for _ in range(SIZE + 1)]

for i in range(2, (SIZE + 1) * 2):
  for x in range(1, i):
    y = i - x

    if x >= SIZE + 1 or y >= SIZE + 1:
      continue

    grid[x][y] = grid[x - 1][y] + grid[x][y - 1]

print grid[SIZE][SIZE]

###
# C(40, 20) = 20! / 40!(40-20)!

import math

print math.factorial(SIZE * 2) // (math.factorial(SIZE) * math.factorial(SIZE))
