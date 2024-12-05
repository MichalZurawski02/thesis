from docplex.cp.model import CpoModel, CpoParam, CpoParameters

class suguru_solver_ilog:
    def __init__(self, m, n, blocks):
        self.width = n
        self.length = m
        self.blocks = blocks
        self.variables = {}
        self.model = CpoModel()

    def neighbors(self, y, x):
        neighbors = []
        for (dy, dx) in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]:
            y1, x1 = y + dy, x + dx
            if 1 <= y1 <= self.length and 1 <= x1 <= self.width:
                neighbors.append((y1, x1))
        return neighbors

    def add_variables(self):
        for block in self.blocks:
            block_variables = []
            l = len(block)
            for cell in block:
                if len(cell) == 2:
                    y, x = cell
                    var = self.model.integer_var(1, l, name=f'C_{y}_{x}')
                    self.variables[(y, x)] = var
                    block_variables.append(var)
                elif len(cell) == 3:
                    y, x, value = cell
                    var = self.model.integer_var(value, value, name=f'C_{y}_{x}')
                    self.variables[(y, x)] = var
                    block_variables.append(var)
            
            self.model.add(self.model.all_diff(block_variables))

    def add_neighborhood_constraints(self):
        for (y, x), var in self.variables.items():
            for neighbor in self.neighbors(y, x):
                if neighbor in self.variables:
                    neighbor_var = self.variables[neighbor]
                    self.model.add(var != neighbor_var)

    def solve(self):
        self.add_variables()
        self.add_neighborhood_constraints()
        param=CpoParameters()
        param.Workers=1
        self.model.set_parameters(param)


        solution = self.model.solve(execfile='/opt/ibm/ILOG/CPLEX_Studio2211/cpoptimizer/bin/x86-64_linux/cpoptimizer')
        
        if solution:
            print("Solution:")
            for y in range(1, self.length + 1):
                row = []
                for x in range(1, self.width + 1):
                    if (y, x) in self.variables:
                        row.append(str(solution[self.variables[(y, x)]]))
                    else:
                        row.append(".")
                print(" ".join(row))
        else:
            print("No solution found.")