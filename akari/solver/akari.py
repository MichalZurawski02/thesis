from enum import Enum
from docplex.cp.model import CpoModel

from akari_io import parse_file, print_puzzle
from akari_model import Akari, State


file_path = '../akari_data/akari14.txt'

puzzle = Akari(parse_file(file_path))

model = CpoModel()

lights = [[model.binary_var(name=f'light_{row}_{col}') for col in range(puzzle.width)] for row in range(puzzle.height)]

def constraint_double_light(model, puzzle, lights, x, y, dx, dy, length, max_length):
    i = 0
    while i < length:
        count = puzzle.count_state_in_direction(x + i * dx, y + i * dy, dx, dy, State.EMPTY)
        if count > 1:
            cells = [(x + i * dx, y + i * dy) for i in range(i, i + count)]
            model.add(model.sum(lights[j][k] for j, k in cells) <= 1)
        i += count

for i in range(puzzle.height):
    for j in range(puzzle.width):
        state = puzzle.puzzle[i][j]
        if puzzle.puzzle[i][j] == State.EMPTY:
            model.add(model.sum(lights[k][l] for k, l in puzzle.visible(i, j)) > 0)
        else:
            model.add(lights[i][j] == 0)
        if state in {State.CELL0, State.CELL1, State.CELL2, State.CELL3, State.CELL4}:
            lights_number = state.value - State.CELL0.value
            model.add(model.sum(lights[k][l] for k, l in puzzle.neighbors(i, j)) == lights_number)
        
for i in range(puzzle.height):
    constraint_double_light(model, puzzle, lights, i, 0, 0, 1, puzzle.width, puzzle.height)

for i in range(puzzle.width):
    constraint_double_light(model, puzzle, lights, 0, i, 1, 0, puzzle.height, puzzle.width)

lights_num = model.integer_var(0, puzzle.height * puzzle.width, name="lights_num")
model.add(lights_num == sum(lights[i][j] for i in range(puzzle.width) for j in range(puzzle.height)))
#model.add(model.minimize(lights_num))

solution = model.solve(execfile='/opt/ibm/ILOG/CPLEX_Studio_Community2211/cpoptimizer/bin/x86-64_linux/cpoptimizer')

if solution:
    for i in range(puzzle.height):
        for j in range(puzzle.width):
            if puzzle.puzzle[i][j] == State.EMPTY:
                puzzle.puzzle[i][j] = State.LIGHT if solution[lights[i][j]] > 0 else State.EMPTY
    print_puzzle(puzzle.puzzle)