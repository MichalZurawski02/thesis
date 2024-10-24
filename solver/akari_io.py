from akari_model import State


def to_enum(c):
    if c == ' ':
        return State.EMPTY
    elif c == '0':
        return State.CELL0
    elif c == '1':
        return State.CELL1
    elif c == '2':
        return State.CELL2
    elif c == '3':
        return State.CELL3
    elif c == '4':
        return State.CELL4
    elif c == '#':
        return State.FULL
    else:
        raise ValueError(f"Unknown character: {c}")

def to_char(e):
    if e == State.EMPTY:
        return ' '
    elif e == State.CELL0:
        return '0'
    elif e == State.CELL1:
        return '1'
    elif e == State.CELL2:
        return '2'
    elif e == State.CELL3:
        return '3'
    elif e == State.CELL4:
        return '4'
    elif e == State.FULL:
        return '#'
    elif e == State.LIGHT:
        return '*'
    else:
        raise ValueError(f"Unknown token: {e}")

def get_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    enum_array = []
    for line in lines:
        enum_row = [to_enum(c) for c in line.rstrip('\n')]
        enum_array.append(enum_row)

    return enum_array

def print_puzzle(puzzle):
    for row in puzzle:
        for cell in row:
            print("[" + to_char(cell) + "] ", end='')
        print("\n")