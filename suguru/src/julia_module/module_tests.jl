include("suguru_solver.jl")

using .SuguruSolver
using Serialization
using FileIO

function load_puzzles_from_folder(folder_path::String)
    puzzle_files = readdir(folder_path; join=true)
    puzzles = []
    for file in puzzle_files
        if endswith(file, ".txt")
            content = open(file, "r") do f
                read(f, String)
            end
            push!(puzzles, (file, eval(Meta.parse(content))))
        end
    end
    return puzzles
end

function process_puzzles(folder_path::String, size::Int)
    puzzles = load_puzzles_from_folder(folder_path)
    results = []
    
    for (file_path, puzzle) in puzzles
        _, backtracking_counter, time, solution = SuguruSolver.solve(puzzle, size, size, false)
        push!(results, "$(basename(file_path));$backtracking_counter;$time;$solution")
    end
    
    results_folder = joinpath(folder_path, "results")
    if !isdir(results_folder)
        mkdir(results_folder)
    end
    
    output_file = joinpath(results_folder, "results.txt")
    open(output_file, "w") do f
        for result in results
            println(f, result)
        end
    end
end

function parse_args()
    args = Base.ARGS
    if length(args) < 2
        println("Błąd wywołania. Poprawne użycie:  julia module_tests.jl <ścieżka> <rozmiar>")
        exit(1)
    end
    return args[1], parse(Int, args[2])
end

function main()
    path, size = parse_args()
    process_puzzles(path, size)
end

main()
