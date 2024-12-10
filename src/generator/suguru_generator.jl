module SuguruGenerator

using Random

function generate_voronoi_grid(grid_size::Int, blocks_num::Int)
    available_cells = [(x, y) for x in 1:grid_size, y in 1:grid_size]
    available_cells = shuffle(available_cells)
    centers = available_cells[1:blocks_num]

    block_idx = 1:blocks_num
    center_map = Dict(centers[i] => block_idx[i] for i in 1:blocks_num)

    grid = zeros(Int, grid_size, grid_size)
    for x in 1:grid_size
        for y in 1:grid_size
            distances = [abs(x - cx) + abs(y - cy) for (cx, cy) in centers]
            nearest_center = centers[argmin(distances)]
            grid[x, y] = center_map[nearest_center]
        end
    end

    return create_grid_dictionary(grid)
end

function print_grid(grid)
    for row in eachrow(grid)
        println(join([string(cell) * " " for cell in row]))
    end
end

function create_grid_dictionary(grid)
    grid_dict = Dict{Int, Set}()
    for x in 1:size(grid, 1)
        for y in 1:size(grid, 2)
            value = grid[x, y]
            if !(value in keys(grid_dict))
                grid_dict[value] = Set([(y,x)])
            else
                push!(grid_dict[value], (y, x))
            end
        end
    end
    res = Vector{Set}([])
    for x in grid_dict
        push!(res, x[2])
    end
    return res
end

end