module Utils
export State, parse_file, print_puzzle

@enum State begin
    EMPTY = 1
    CELL0 = 2
    CELL1 = 3
    CELL2 = 4
    CELL3 = 5
    CELL4 = 6
    FULL = 7
    LIGHT = 8
end

function parse_file(filepath::String)::Vector{Vector{State}}
    lines = readlines(filepath)
    
    states = Vector{Vector{State}}()
    
    for line in lines
        row = [to_state(char) for char in line]
        push!(states, row)
    end
    return states
end


function print_puzzle(states::Vector{Vector{State}})
    for row in states
        for state in row
            print("[" * string(to_char(state)) * "] ")
        end
        println()
        println()
    end
end


function to_state(char::Char)::State
    if char == ' '
        return EMPTY
    elseif char in '0'
        return CELL0
    elseif char in '1'
        return CELL1
    elseif char in '2'
        return CELL2
    elseif char in '3'
        return CELL3
    elseif char in '4'
        return CELL4
    elseif char == '#'
        return FULL
    else
        throw(ArgumentError("Invalid char: $char"))
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

end