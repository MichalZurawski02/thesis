include("utils.jl")
include("backtracking.jl")
using .Utils
using .Backtracking

puzzle = parse_file("../akari_data/akari10.txt")
solve(puzzle)
print_puzzle(puzzle)