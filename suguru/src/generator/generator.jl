include("suguru_solver.jl")
include("suguru_generator.jl")
using .SuguruSolver
using .SuguruGenerator

function parse_args()
    args = Base.ARGS
    if length(args) < 3
        println("Błąd wywołania. Poprawne użycie: julia generate_and_test.jl <size> <num_components> <num_grids>")
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
     
    for i in 1:quantity
        puzzle = SuguruGenerator.generate_voronoi_grid(size, components)
        
        puzzle_file_name = "$data_dir/$(size)_$(components)_$(i).txt"
        open(puzzle_file_name, "w") do file
            write(file, string(puzzle))
        end
    end

end

main()