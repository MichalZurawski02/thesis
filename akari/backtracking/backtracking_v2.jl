include("utils.jl")
using .Utils

module SmartBacktracking
export smart_solve
using ..Utils: State, EMPTY, FULL, CELL0, CELL1, CELL2, CELL3, CELL4, LIGHT
using Combinatorics


mutable struct ConstrainedCell
    num
    y
    x
    allneighbors
    possibility_num
    free_bulbs_num
end

function deleteFirst!(list, object)
    i = findfirst(o -> o == object, list)
    if i !== nothing
        deleteat!(list, i)
    end
end


function neighbors(puzzle, y, x)
    neighbors = []

    for (dy, dx) in [(1, 0), (-1, 0), (0, 1), (0, -1)]
        y1, x1 =  y + dy, x + dx
        if y1 > 0 && y1 <= length(puzzle[1]) && x1 > 0 && x1 <= length(puzzle) && puzzle[y1][x1] == EMPTY
            push!(neighbors, (y1, x1))
        end
    end

    return neighbors
end

function is_solved(puzzle, unlit, solution)
    if !isempty(unlit)
        return false
    end
    for y in 1:length(puzzle)
        for x in 1:length(puzzle[y])
            if 2 < Int(puzzle[y][x]) < 7
                allneighbors = neighbors(puzzle, y, x)      
                if count(n -> n in solution, allneighbors) != Int(puzzle[y][x]) - 2
                    return false
                end
            end
        end
    end
    return true
end

function can_be_solved(puzzle, solution, possible)
    for y in 1:length(puzzle)
        for x in 1:length(puzzle[y])
            if 2 < Int(puzzle[y][x]) < 7
                allneighbors = neighbors(puzzle, y, x)
                count_bulbs = count(n -> n in solution, allneighbors)
                possible_bulbs = count(n -> n in possible, allneighbors)
                expected_bulbs = Int(puzzle[y][x]) - 2 
                if count_bulbs > expected_bulbs || expected_bulbs - count_bulbs > possible_bulbs
                    return false
                end
            end
        end
    end
    
    return true
end


function light_up(puzzle, y, x, unlit, possible, solution)
    deleteFirst!(unlit, (y, x))
    deleteFirst!(possible, (y, x))

    for (dy, dx) in [(1, 0), (-1, 0), (0, 1), (0, -1)]
        y1, x1 = y + dy, x + dx
        if y1 > 0 && y1 <= length(puzzle) && x1 > 0 && x1 <= length(puzzle[1]) 
            if puzzle[y1][x1] == EMPTY
                while y1 > 0 && y1 <= length(puzzle) && x1 > 0 && x1 <= length(puzzle[1]) && puzzle[y1][x1] == EMPTY
                    deleteFirst!(unlit, (y1, x1))
                    deleteFirst!(possible, (y1, x1))
                    y1 += dy
                    x1 += dx
                end
            else
                if puzzle[y1][x1] == FULL
                    continue
                end
                allneighbors = neighbors(puzzle, y1, x1)
                placed = count(n -> n in solution, allneighbors)
                if Int(puzzle[y1][x1]) - Int(CELL0) == Int(placed)
                    for neighbor in allneighbors
                        deleteFirst!(possible, neighbor)
                    end
                end
            end
        end
    end
end


function update_constraints_cells(constrained_cells, possible, solution)
    for cell in constrained_cells
        possibility, free = 0, cell.num
        for neighbor in cell.allneighbors
            if neighbor in solution
                free -= 1
            elseif neighbor in possible
                possibility += 1
            end
        end
        cell.free_bulbs_num = free
        cell.possibility_num = binomial(possibility, free)
        if cell.free_bulbs_num == 0
            deleteFirst!(constrained_cells, cell)
        end
    end
end


function backtrack(puzzle, unlit, possible, constrained_cells, solution, counter)
    if is_solved(puzzle, unlit, solution)
        print_puzzle(puzzle, solution)
        println(counter)
        return
    end

    if isempty(possible) || !can_be_solved(puzzle, solution, possible)
        return
    end

    if !isempty(constrained_cells) 
        # posortowanie ponumerowanych komórek po:
        # a) liczbie możliwości
        # b) liczbie żarówek do zapalenia
        update_constraints_cells(constrained_cells,possible,solution)
        constrained_cells = sort(constrained_cells, by = c -> (-c.possibility_num, c.free_bulbs_num))
        cell = pop!(constrained_cells)
        available = []
        for neighbor in cell.allneighbors
            if neighbor in possible
                push!(available, neighbor)
            end
        end

        if cell.free_bulbs_num <= 0 || length(available) <= 0 || cell.free_bulbs_num > length(available) 
            return
        end

        placements = collect(combinations(available, cell.free_bulbs_num))
        
        for placement in placements
            unlit_copy, possible_copy, constrained_cells_copy = copy(unlit), copy(possible), copy(constrained_cells)
            for place in placement

                (place_y, place_x) = place
                light_up(puzzle, place_y, place_x, unlit_copy, possible_copy, solution)
                push!(solution, place)

            end
            backtrack(puzzle, unlit_copy, possible_copy, constrained_cells_copy, solution, counter)
            counter += 1

            for _ in placement
                pop!(solution)
            end
        end
    else
        eval_y, eval_x = pop!(possible)
        unlit_copy, possible_copy, constrained_cells_copy = copy(unlit), copy(possible), copy(constrained_cells)

        light_up(puzzle, eval_y, eval_x, unlit, possible, solution)
    
        push!(solution, (eval_y, eval_x))

        backtrack(puzzle, unlit, possible, constrained_cells, solution, counter)
        counter += 1
    
        pop!(solution)
        backtrack(puzzle, unlit_copy, possible_copy, constrained_cells, solution, counter)
        counter += 1
    end
end


function to_char(state::State)::Char
    if state == EMPTY
        return ' '
    elseif state == CELL0
        return '0'
    elseif state == CELL1
        return '1'
    elseif state == CELL2
        return '2'
    elseif state == CELL3
        return '3'
    elseif state == CELL4
        return '4'
    elseif state == FULL
        return '#'
    elseif state == LIGHT
        return '*'
    else
        throw(ArgumentError("Invalid state: $state"))
    end
end

function print_puzzle(puzzle, solution)
    for i in 1:length(puzzle)
        for j in 1:length(puzzle[i])
            if puzzle[i][j] == EMPTY
                if (i, j) in solution
                    print("[*] ")
                else
                    print("[ ] ") 
                end
            else
                print("[" * string(to_char(puzzle[i][j])) * "] ")
            end
        end
        println()
        println()
    end
end

function smart_solve(puzzle)
    unlit = []
    possible = []
    constrained_cells = []
    solution = []

    for i in 1:length(puzzle)
        for j in 1:length(puzzle[i])
            if puzzle[i][j] == EMPTY
                push!(unlit, (i, j))
                push!(possible, (i, j))
            end
        end
    end

    for i in 1:length(puzzle)
        for j in 1:length(puzzle[i])
            if puzzle[i][j] == CELL0
                allneighbors = neighbors(puzzle, i, j)
                for neighbor in allneighbors
                    deleteFirst!(possible, neighbor)
                end
            elseif puzzle[i][j] == CELL1
                allneighbors = neighbors(puzzle, i, j)
                push!(constrained_cells, ConstrainedCell(1, i, j, allneighbors, 0, 0))
            elseif puzzle[i][j] == CELL2
                allneighbors = neighbors(puzzle, i, j)
                push!(constrained_cells, ConstrainedCell(2, i, j, allneighbors, 0, 0))
            elseif puzzle[i][j] == CELL3
                allneighbors = neighbors(puzzle, i, j)
                push!(constrained_cells, ConstrainedCell(3, i, j, allneighbors, 0, 0))
            elseif puzzle[i][j] == CELL4
                allneighbors = neighbors(puzzle, i, j)
                for neighbor in allneighbors
                    light_up(puzzle, neighbor[0], neighbor[1], unlit, possible, solution)
                    #push
                end
            end
        end
    end

    backtrack(puzzle, unlit, possible, constrained_cells, solution, 0)

end


end