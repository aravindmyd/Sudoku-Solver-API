# grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#         [5, 2, 0, 0, 0, 0, 0, 0, 0],
#         [0, 8, 7, 0, 0, 0, 0, 3, 1],
#         [0, 0, 3, 0, 1, 0, 0, 8, 0],
#         [9, 0, 0, 8, 6, 3, 0, 0, 5],
#         [0, 5, 0, 0, 9, 0, 6, 0, 0],
#         [1, 3, 0, 0, 0, 0, 2, 5, 0],
#         [0, 0, 0, 0, 0, 0, 0, 7, 4],
#         [0, 0, 5, 2, 0, 6, 3, 0, 0]]


class SudokuSolver:
    def print_board(self, board):
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            if row % 3 == 0:
                print("- - - - - - - - - - - -")
            for col in range(cols):
                if col % 3 == 0 and col != 0:
                    print("|", end=" ")
                print(board[row][col], end=" ")
            print("|", end=" ")
            print()

    def empty_spot(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    return (row, col)
        return False

    def valid_number(self, grid, pos, num):
        x_pos = pos[0]
        y_pos = pos[1]
        # Check the row
        for row in range(len(grid[0])):
            if grid[x_pos][row] == num and pos == (x_pos, y_pos):
                return False
        # Check the column
        for col in range(len(grid)):
            if grid[col][y_pos] == num and pos == (x_pos, y_pos):
                return False
        # Check the inner grid
        box_x = x_pos // 3
        box_y = y_pos // 3
        for row in range(box_x * 3, box_x * 3 + 3):
            for col in range(box_y * 3, box_y * 3 + 3):
                if grid[row][col] == num and pos == (x_pos, y_pos):
                    return False
        return True

    def solve(self, grid):
        # Find the empty spot to fill
        pos = self.empty_spot(grid)
        if not pos:
            return grid
        dx,dy = pos
        # Try some number and validate if it is correct or not
        for num in range(1, 10):
            if self.valid_number(grid,pos,num):
                grid[dx][dy] = num
                if self.solve(grid):
                   return grid
                grid[dx][dy] = 0
        # If correct move on to next cell else backtrack and reset previous cell to zero
        return False

#
# obj = SudokuSolver()
# obj.print_board(grid)
#
# print()
#
# print("-----------------After Solving-----------------------")
# obj.solve(grid)
# obj.print_board(grid)
