include("suguru_solver.jl")
include("suguru_generator.jl")
using .SuguruSolver
using .SuguruGenerator

function parse_args()
    args = Base.ARGS
    if length(args) < 3
        println("Błąd wywołania. Poprawne użycie: julia generate_and_test.jl <initial_grid_size> <num_components> <num_grids>")
        exit(1)
    end
    return parse(Int, args[1]), parse(Int, args[2]), parse(Int, args[3])
end

# Main program
function main()
    size, components, quantity = parse_args()

    data_dir = "data/$(size)_$(components)"
    if !isdir(data_dir)
        mkpath(data_dir)
    end
    results_file = "$data_dir/$(size)_$(components)_res.txt"  

    
    open(results_file, "w") do results        
        for i in 1:quantity
            puzzle = SuguruGenerator.generate_voronoi_grid(size, components)
            
            puzzle_file_name = "$data_dir/$(size)_$(components)_$(i).txt"
            open(puzzle_file_name, "w") do file
                write(file, string(puzzle))
            end
            grid, backtracking_counter, time, sol = SuguruSolver.solve(puzzle, size, size, true)
            write(results, "$backtracking_counter; $time; $sol\n")
        end
    end
end

main()