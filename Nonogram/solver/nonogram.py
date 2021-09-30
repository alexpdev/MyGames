import itertools
import functools

class IndexOver(Exception):
    pass

class DimensionError(Exception):
    pass

class Grid:

    def __init__(self, width, height, elem):
        self.width = width
        self.height = height
        self.elem = elem
        self.grid = [["x" for _ in range(width)] for _ in range(height)]

    def __str__(self):
        return str(self.grid)

    def __len__(self):
        return len(self.grid)

    def __repr__(self):
        return repr(self.grid)

    @property
    def output(self):
        return tuple([tuple(i) for i in self.grid])

    @property
    def size(self):
        return (self.width, self.height)

    def cell(self,r,c):
        if r > max(self.size) < c:
            raise IndexOver
        return self.grid[r][c]

    def setCell(self,r,c,val):
        if r > max(self.size) < c:
            raise IndexOver
        self.grid[r][c] = val

    def row(self,r):
        if r > max(self.size):
            raise IndexOver
        return self.grid[r][:]

    def setRow(self,r,lst):
        if r > max(self.size):
            raise IndexOver
        for i, val in enumerate(lst):
            self.grid[r][i] = val

    def col(self, c):
        if c > max(self.size):
            raise IndexOver
        return [i[c] for i in self.grid]

    def setCol(self, c, lst):
        if c > max(self.size):
            raise IndexOver
        for i, val in enumerate(lst):
            self.grid[i][c] = val

    def checkCell(self, r, c):
        if c > max(self.size) < r:
            raise IndexOver
        return self.cell(r,c) == self.elem

    def __iter__(self):
        return iter(self.grid)


class Nonogram:

    def __init__(self,clues,*args):
        if len(args) > 0:
            print(args)
            self.clues = [clues[1],clues[0]]
        else:
            self.clues = clues
        self.cclues = dict()
        self.cclues.update([(k,v) for k,v in enumerate(clues[0])])
        self.rclues = dict()
        self.rclues.update([(k,v) for k,v in enumerate(clues[1])])
        self.size = (len(self.cclues), len(self.rclues))
        self.grid = Grid(*self.size, "_")
        self.solve()

    def get_cell(self, r, c):
        return self.grid.cell(r, c)

    def set_cell(self, r, c, val):
        self.grid.setCell(r, c, val)

    def get_row(self, r):
        return self.grid.row(r)

    def set_row(self, r, lst):
        self.grid.setRow(r, lst)

    def get_col(self, c):
        return self.grid.col(c)

    def set_col(self, c, lst):
        self.grid.setCol(c, lst)

    def get_seq(self, dim, index):
        if dim in ["c", "col"]:
            return self.get_col(index)
        elif dim in ["r", "row"]:
            return self.get_row(index)
        else:
            raise DimensionError

    def set_seq(self, dim, index, lst):
        if dim in ["c", "col"]:
            return self.set_col(index, lst)
        elif dim in ["r", "row"]:
            return self.set_row(index, lst)
        else:
            raise DimensionError

    def solving(self):
        for dim, clues in [("row",self.rclues),("col",self.cclues)]:

            for k,v in clues.items():
                row = self.get_seq(dim, k)
                r = tuple(row)
                if self.row_is_solved(row): continue
                solution = check_possible(v, row)
                if tuple(solution) == r: continue
                self.set_seq(dim, k, solution)

    def row_is_solved(self,row):
        if "_" not in row:
            return True
        return False

    def grid_is_solved(self):
        for row in self.grid:
            if "_" in row:
                return False
        return True

    def solve(self):
        while not self.grid_is_solved():
            self.solving()
        return self.grid.output

def check_possible(clue, row):
    solutions, start, sums = [], 0, sum(clue)
    comb(clue, row, solutions, start, sums)
    solution = find_common(solutions, row, clue)
    return solution

def check_constraint(cluerange, row, n):
    first, last = cluerange[0], cluerange[-1]
    if any([row[i] == 0 for i in cluerange]):
        return False
    if first != 0 and row[first - 1] == 1:
        return False
    if last != n - 1 and row[last + 1] == 1:
        return False
    return True

def find_common(solutions, row, clues):
    if len(solutions) == 1:
        return [i if i == 1 else 0 for i in solutions[0]]

    for i in range(len(row)):
        i_list = [sol[i] for sol in solutions]
        if i_list.count(i_list[0]) == len(i_list):
            if i_list[0] == 1:
                row[i] = 1
            else:
                row[i] = 0

    if sum([i for i in row if i == 1]) == sum(clues):
        return [i if i == 1 else 0 for i in row]
    return row

def comb(clues, row, solutions, start, sums):
    if len(clues) == 0:
        if row.count(1) <= sums:
            solutions.append(row)
        return
    pool = tuple(row)
    n = len(pool)
    for _ in range(start,n):
        clue = clues[0]
        if start + sum(clues) > n:
            return
        idx = list(range(start, clue + start))
        if check_constraint(idx, pool, n):
            nrow = [1 if i in idx else x for i,x in enumerate(pool)]
            comb(clues[1:], nrow, solutions, clue + start + 1, sums)
        start += 1
