include("csp.jl")
using Random
using OrderedCollections
using .CSPModule

# Constraint function to check if queens do not attack each other
function nqueen_constraint(A, a, B, b)
    # Ensure queens are not in the same column
    if a == b
        return false
    end
    # Ensure queens are not in the same diagonal
    if abs(A - B) == abs(a - b)
        return false
    end
    return true
end

# Solve the N-Queens problem using backtracking search
function solve(N::Int)
    println("$N-Queens Solution:")

    variables = 1:N
    println(variables)
    domains = Dict(var => 1:N for var in variables)
    neighbors = Dict(var => [i for i in variables if i != var] for var in variables)
    println(neighbors)
    # Create a CSP object with necessary components
    csp = CSPModule.CSP(variables, domains, neighbors, nqueen_constraint)

    start_time = time()

    # Use CSPModule backtracking search
    solution = CSPModule.backtracking_search(csp, select_unassigned_variable=CSPModule.mrv, inference=CSPModule.forward_checking)

    # Display the solution
    display(solution)
    println("Solved in ", time() - start_time, " seconds.\n")
end

# Display the solution in a readable format
function display(assignment)
    N = length(assignment)
    for row in 1:N
        line = ""
        for col in 1:N
            if col == get(assignment, row, -1)
                line *= " Q "
            else
                line *= " . "
            end
        end
        println(line)
    end
    println("\n")
end

solve(4)
solve(8)
solve(50)