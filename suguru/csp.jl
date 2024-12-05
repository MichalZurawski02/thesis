module CSPModule

using Random
using OrderedCollections


mutable struct CSP
    variables::Vector{Any}
    domains::Dict{Any, Vector{Any}}
    neighbors::Dict{Any, Vector{Any}}
    curr_domains::Union{Dict{Any, Vector{Any}}, Nothing}
    backtracking_counter::Int
    blocks::Any

    function CSP(variables, domains, neighbors, blocks)
        return new(variables, domains, neighbors, nothing, 0, blocks)
    end
end



# Inference Functions
function revise(csp::CSP, Xi, Xj, removals)
    revised = false
    for x in csp.curr_domains[Xi]
        conflict = true
        for y in csp.curr_domains[Xj]
            if x !== y
                conflict = false
                break
            end
        end

        if conflict
            deleteat!(csp.curr_domains[Xi], findall(==(x), csp.curr_domains[Xi]))
            if removals !== nothing
                push!(removals, (Xi, x))
            end
            revised = true
        end
    end

    return revised
end


function AC3(csp::CSP, queue=nothing, removals=nothing)
    if queue === nothing
        queue = Set([(Xi, Xj) for Xi in csp.variables, Xj in csp.neighbors[Xi]])
    end

    csp.curr_domains = csp.curr_domains === nothing ? Dict(v => copy(csp.domains[v]) for v in csp.variables) : csp.curr_domains

    while !isempty(queue)
        (Xi, Xj) = pop!(queue)

        revised = revise(csp, Xi, Xj, removals)

        if revised
            if isempty(csp.curr_domains[Xi])
                return false
            end

            for Xk in csp.neighbors[Xi]
                if Xk != Xj
                    push!(queue, (Xk, Xi))
                end
            end
        end
    end

    return true
end

function default(csp, var, value, assignment, removals)
    return true
end

function fc(csp::CSP, var, value, assignment, removals)
    csp.curr_domains = csp.curr_domains === nothing ? Dict(v => copy(csp.domains[v]) for v in csp.variables) : csp.curr_domains
    for X in csp.neighbors[var]
        if !(X in keys(assignment))
            for x in csp.curr_domains[X]
                if x == value
                    deleteat!(csp.curr_domains[X], findall(==(x), csp.curr_domains[X]))
                    if removals !== nothing
                        push!(removals, (X, x))
                    end
                end
            end
            if isempty(csp.curr_domains[X])
                return false
            end
        end
    end
    return true
end

function mac(csp, var, value, assignment, removals)
    arcs = Set([(X, var) for X in csp.neighbors[var]])
    return AC3(csp, arcs, removals)
end



function conflicts_num(csp::CSP, var, val, assignment)
    return sum((haskey(assignment, v) && val === assignment[v]) for v in csp.neighbors[var])
end



# Variable ordering
function num_unassigned_in_block(csp::CSP, var, assignment)
    block = find_block(csp, var)
    unassigned_vars = [v for v in block if !(v in keys(assignment))]
    return length(unassigned_vars)
end

function find_block(csp::CSP, var)
    for block in csp.blocks
        if var in block
            return block
        end
    end
    error("Variable not found in any block: $var")
end

function break_tie_by_block(csp::CSP, vars, assignment)
    key = var -> num_unassigned_in_block(csp, var, assignment)
    return break_tie_randomly(vars; key)
end

function break_tie_randomly(seq; key=identity)
    shuffled_seq = shuffle!(collect(seq))
    transformed_seq = map(key, shuffled_seq)
    min_index = argmin(transformed_seq)
    return shuffled_seq[min_index]
end

function num_legal_values(csp::CSP, var, assignment)
    return csp.curr_domains !== nothing ? 
            length(csp.curr_domains[var]) :
            sum(conflicts_num(csp, var, val, assignment) == 0 for val in csp.domains[var])
end


function no_variable_heurestic(assignment, csp::CSP)
    possible = [v for v in csp.variables if !(v in keys(assignment))]
    return isempty(possible) ? default : possible[1]
end

function mrv_blocks(assignment, csp::CSP)
    possible = [v for v in csp.variables if !(v in keys(assignment))]

    min_legal_values = minimum(num_legal_values(csp, var, assignment) for var in possible)
    candidates = [v for v in possible if num_legal_values(csp, v, assignment) == min_legal_values]

    if(length(candidates) > 1)
        return break_tie_by_block(csp, candidates, assignment)
    end

    return candidates[1]
end

function mrv_rand(assignment, csp::CSP)
    possible = [v for v in csp.variables if !(v in keys(assignment))]
    key = var -> num_legal_values(csp, var, assignment)
    return break_tie_randomly(possible; key)
end



# Value ordering
function no_value_heurestic(var, assignment, csp::CSP)
    return (csp.curr_domains !== nothing ? csp.curr_domains : csp.domains)[var]
end

function lcv(var, assignment, csp::CSP)
    return sort(no_value_heurestic(var, assignment, csp), by=val -> conflicts_num(csp, var, val, assignment))
end



# Backtracking
function backtracking_search(csp::CSP; variable_heurestic=no_variable_heurestic,
                            value_heurestic=no_value_heurestic, inference=default)
    function backtrack(assignment)
        if length(assignment) == length(csp.variables)
            return assignment
        end
        variable = variable_heurestic(assignment, csp)
        for value in value_heurestic(variable, assignment, csp)
            if conflicts_num(csp, variable, value, assignment) == 0
                assignment[variable] = value
                csp.curr_domains = csp.curr_domains === nothing ? Dict(v => copy(csp.domains[v]) for v in csp.variables) : csp.curr_domains
                removed = [(variable, a) for a in csp.curr_domains[variable] if a != value]
                csp.curr_domains[variable] = [value]

                if inference(csp, variable, value, assignment, removed)
                    result = backtrack(assignment)
                    if result !== nothing
                        return result
                    end
                    csp.backtracking_counter += 1
                end
                
                for (var, val) in removed
                    push!(csp.curr_domains[var], val)
                end
            end
        end
        delete!(assignment, variable)
        return nothing
    end
    return backtrack(Dict())
end

end