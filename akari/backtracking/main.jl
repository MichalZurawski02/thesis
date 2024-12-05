include("utils.jl")
include("backtracking_v2.jl")
using .Utils
using .SmartBacktracking

puzzle = parse_file("../akari_data/akari20.txt")
print_puzzle(puzzle)
println()
println()
smart_solve(puzzle)