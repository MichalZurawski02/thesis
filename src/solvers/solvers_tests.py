import os
from suguru_ortools import suguru_solver_ortools
from solvers.suguru_ilog import suguru_solver_ilog
import time


def read_grid_from_file(file_path):
    if not os.path.isfile(file_path):
        raise ValueError(f"Błąd")
    
    with open(file_path, 'r') as file:
        file_content = file.read().strip()
        
        file_content = file_content[3:]
        file_content = file_content.replace('Set([', '{').replace('])', '}')
        
        try:
            grids = eval(file_content)
        except Exception as e:
            raise ValueError(f"Błąd wczytywania {e}")
        
        return grids


def solve_puzzles_from_directory():
    directory_path = input("Ścieżka: ")
    if not os.path.isdir(directory_path):
        return
    
    size = int(input("Rozmiar: "))
    
    ortools_results = []
    ilog_results = []

    for file_name in os.listdir(directory_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory_path, file_name)
            try:
                grid = read_grid_from_file(file_path)

                solver = suguru_solver_ortools(size, size, grid)
                start_time = time.time()
                result = solver.solve()
                ortools_time = time.time() - start_time
                ortools_results.append((file_name, result, ortools_time))
                
                solver = suguru_solver_ilog(size, size, grid)
                start_time = time.time()
                result = solver.solve() 
                ilog_time = time.time() - start_time
                ilog_results.append((file_name, result, ilog_time))
            
            except Exception as e:
                print(f"Błąd wczytywania pliku {file_name}: {e}")

    results_directory = os.path.join(directory_path, 'results')
    os.makedirs(results_directory, exist_ok=True)

    save_results_to_file(ortools_results, os.path.join(results_directory, 'ortools_results.txt'))
    save_results_to_file(ilog_results, os.path.join(results_directory, 'ilog_results.txt'))


def save_results_to_file(results, output_path):
    with open(output_path, 'w') as output_file:
        for file_name, result, time_taken in results:
            output_file.write(f"{file_name}: {result}, {time_taken:.4f}\n")


if __name__ == "__main__":
    solve_puzzles_from_directory()
