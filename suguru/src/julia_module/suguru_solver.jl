module SuguruSolver

export solve

include("csp.jl")
using .CSPModule



function add_variables_with_domains(grid::Vector{Set})
    variables = []
    domains = Dict()
    blocks = []
    for region in grid
        curr_block = []
        for cell in region
            variable = (cell[1], cell[2])
            push!(curr_block, variable)
            push!(variables, variable)
            if length(cell) == 2
                domains[variable] = collect(1:length(region))
            elseif length(cell) == 3
                domains[variable] = [cell[3]]
            end
        end
        push!(blocks, curr_block)
    end
    return variables, domains, blocks
end


function add_all_constraints(variables::Vector, grid::Vector{Set}, size_y, size_x)
    neighbors = Dict()
    for variable in variables
        neighbors[variable] = geometric_neighbors(variable, size_y, size_x)
    end
    block_neighbors!(neighbors, grid)
    return neighbors
end


function geometric_neighbors(variable, size_y, size_x)
    neighbors = []

    for cords in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        y1, x1 =  variable[1] + cords[1], variable[2] + cords[2]
        if y1 > 0 && y1 <= size_y && x1 > 0 && x1 <= size_x
            push!(neighbors, (y1, x1))
        end
    end

    return neighbors
end


function block_neighbors!(neighbors::Dict, grid::Vector{Set})
    for region in grid
        for cell in region
            curr_neighbor = []
            variable = (cell[1], cell[2])
            for c in region
                if c != cell
                    push!(curr_neighbor, (c[1], c[2]))
                end
            end
            neighbors[variable] = unique!(append!(neighbors[variable], curr_neighbor))
        end
    end
end


function solve(grid::Vector{Set}, size_y::Int64, size_x::Int64, display::Bool)
    variables, domains, blocks = add_variables_with_domains(grid)
    neighbors = add_all_constraints(variables, grid, size_y, size_x)
    csp = CSPModule.CSP(variables, domains, neighbors, blocks)

    start_time = time()
    solution = CSPModule.backtracking_search(csp, variable_heurestic=CSPModule.mrv_rand, inference=CSPModule.mac)
    stop_time = time()

    grid = to_grid(solution)
    
    solution = grid === nothing ? false : true

    if display
        try
            for row in 1:size_y
                println(join([length(cell) < 2 ? "0" * string(cell) : string(cell) for cell in grid[row, :]], " "))
            end
        catch e
            println("No solution.")
        end
        println(stop_time - start_time, "\n")
    end

    return grid, csp.backtracking_counter, stop_time-start_time, solution
end


function to_grid(data)
    if(data === nothing)
        return
    end
    rows = maximum(k[1] for k in keys(data))
    cols = maximum(k[2] for k in keys(data))
    
    grid = fill("", rows, cols)
    
    for ((row, col), value) in data
        grid[row, col] = string(value)
    end
    
    return grid
end

end