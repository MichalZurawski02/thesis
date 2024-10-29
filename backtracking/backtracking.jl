include("utils.jl")
using .Utils

module Backtracking
export solve
using ..Utils: State, EMPTY, FULL, CELL0, CELL1, CELL2, CELL3, CELL4, LIGHT



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
        if y1 > 0 && y1 <= length(puzzle[1]) && x1 > 0 && x1 <= length(puzzle)
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
                allneighbors = neighbors(puzzle, x, y)                
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
                allneighbors = neighbors(puzzle, x, y)
                number = Int(puzzle[y][x]) - 2 - count(n -> n in solution, allneighbors)

                if number > count(n -> n in possible, allneighbors)
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

function backtrack(puzzle, unlit, possible, solution)
    if is_solved(puzzle, unlit, solution)
        print(solution)
        println()
        return
    end

    if isempty(possible) || !can_be_solved(puzzle, solution, possible)
        return
    end

    eval_y, eval_x = pop!(possible)
    unlit_copy, possible_copy = copy(unlit), copy(possible)

    light_up(puzzle, eval_y, eval_x, unlit, possible, solution)

    push!(solution, (eval_y, eval_x))
    backtrack(puzzle, unlit, possible, solution)

    pop!(solution)
    backtrack(puzzle, unlit_copy, possible_copy, solution)
end



function solve(puzzle)
    unlit = []
    possible = []

    for i in 1:length(puzzle)
        for j in 1:length(puzzle[i])
            if(puzzle[i][j] == EMPTY)
                push!(unlit, (i, j))
                push!(possible, (i, j))
            end
        end
    end
    light_up(puzzle,)

    #backtrack(puzzle, unlit, possible, [])

end


end