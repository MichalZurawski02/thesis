from ortools.sat.python import cp_model

class suguru_solver_ortools:
    def __init__(self, m, n, blocks):
        self.width = n
        self.length = m
        self.blocks = blocks
        self.variables = {}
        self.model = cp_model.CpModel()

    def neighbors(self, y, x):
        neighbors = []
        for (dy, dx) in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]:
                y1, x1 =  y + dy, x + dx
                if y1 > 0 and y1 <= self.length and x1 > 0 and x1 <= self.width:
                    neighbors.append((y1, x1))
        return neighbors
    
    def add_variables(self):
        for block in self.blocks:
            block_variables = []
            l = len(block)
            for cell in block:
                if len(cell) == 2:
                    y, x = cell
                    var = self.model.NewIntVar(1, l, f'C_{y}_{x}')
                    self.variables[(y, x)] = var
                    block_variables.append(var)
                elif len(cell) == 3:
                    y, x, value = cell
                    var = self.model.NewIntVar(value, value, f'C_{y}_{x}')
                    self.variables[(y, x)] = var
                    block_variables.append(var)
            
            self.model.AddAllDifferent(block_variables)
    
    def add_neighborhood_constraints(self):
        for (y, x), var in self.variables.items():
            for neighbor in self.neighbors(y, x):
                if neighbor in self.variables:
                    neighbor_var = self.variables[neighbor]
                    self.model.Add(var != neighbor_var)

    def solve(self):
        self.add_variables()
        self.add_neighborhood_constraints()
        solver = cp_model.CpSolver()
        self.model.AddDecisionStrategy(
        self.variables.values(),
        cp_model.CHOOSE_MIN_DOMAIN_SIZE,
        cp_model.SELECT_MAX_VALUE 
    )
        status = solver.solve(self.model)
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            # print("Solution:")
            # for y in range(1, self.length + 1):
            #     row = []
            #     for x in range(1, self.width + 1):
            #         if (y, x) in self.variables:
            #             row.append(str(solver.Value(self.variables[(y, x)])))
            #         else:
            #             row.append(".")
            #     print(" ".join(row))
            return True
        else:
            return False
