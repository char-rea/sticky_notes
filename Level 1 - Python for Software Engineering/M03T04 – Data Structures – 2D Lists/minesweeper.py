#minesweeper game

minesweeper = [ ["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"] ]

#Return a grid where each dash is replaced by a digit, indicating the number ofmines immediately adjacent to the spot, i.e., horizontally, vertically, anddiagonally.
def count_mines(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "-":
                count = 0
                for x in range(max(0, i-1), min(len(grid), i+2)):
                    for y in range(max(0, j-1), min(len(grid[i]), j+2)):
                        if grid[x][y] == "#":
                            count += 1
                grid[i][j] = str(count)
    return grid

# Print the resulting grid
result = count_mines(minesweeper)
for row in result:
    print(" ".join(row))