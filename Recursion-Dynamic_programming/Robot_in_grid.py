"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
"""
# r = row idx
# c = column idx
g = [
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 1]
]
# (r, c) = row 0, column 0 => top left corner
r = (0, 0)
t = (len(g)-1, len(g[0])-1)

"""
def robot_in_a_grid(grid, robot, target, path=[]):
    # robots coordinates:
    row = robot[0]
    col = robot[1]
    # available movement options for robot at his coords
    right = (row, col+1)
    down = (row+1, col)
    # end conditions:
    if right == target:
        path.append('right')
        return path
    elif down == target:
        path.append('down')
        return path
    # at the right edge
    elif right[1] > len(grid[0]) - 1:
        if grid[down[0]][down[1]] != 1:
            new_path = path.copy()
            new_path.append('down')
            robot_in_a_grid(grid, down, target, new_path)
    # bottom edge
    elif down[0] > len(grid) - 1:
        if grid[right[0]][right[1]] != 1:
            new_path = path.copy()
            new_path.append('right')
            robot_in_a_grid(grid, right, target, new_path)
    # if right and down grid value is 1 ==> its off limits cell
    # stop the loop
    elif grid[right[0]][right[1]] == 1 and grid[down[0]][down[1]] == 1:
        return None
    elif grid[right[0]][right[1]] == 1:
        new_path = path.copy()
        new_path.append('down')
        robot_in_a_grid(grid, down, target, new_path)
    elif grid[down[0]][down[1]] == 1:
        new_path = path.copy()
        new_path.append('right')
        robot_in_a_grid(grid, right, target, new_path)
    else:
        right_path = path.copy()
        right_path.append('right')

        down_path = path.copy()
        down_path.append('down')
        robot_in_a_grid(grid, right, target, right_path)
        robot_in_a_grid(grid, down, target, down_path)
    return path
"""


def getPath(grid, row, col, path):
    # if row or col < 0 ==> coordinates are outside of grid
    # if grid[row][col] = 0 ==> false; not false == true
    # so if its true (coordinates have 0 value ==> forbiden cell)
    # return False ==> there is no path
    if row < 0 or col < 0 or not grid[row][col]:
        return False

    # check if we're at starting position
    isStartPos = True if row == 0 and col == 0 else False

    if isStartPos or getPath(grid, row-1, col, path) or getPath(grid, row, col-1, path):
        path.append((row, col))
        return path
    return False


def game(grid):
    path = []
    # start looking for path at target location (bottom right corner)
    if getPath(grid, len(grid)-1, len(grid[0])-1, path):
        # HOW DO I GET PATH HERE????
        return path

    return None


print(game(g))
