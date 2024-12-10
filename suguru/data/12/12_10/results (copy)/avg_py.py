# Script to calculate average, min, and max time from the file

def calculate_time_stats(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        total_time = 0.0
        count = 0
        min_time = float('inf')
        max_time = float('-inf')
        
        for line in lines:
            try:
                parts = line.split(", Time: ")
                if len(parts) == 2:
                    time_str = parts[1].strip().replace(" seconds", "")
                    time_value = float(time_str)
                    
                    total_time += time_value
                    count += 1
                    min_time = min(min_time, time_value)
                    max_time = max(max_time, time_value)
            except ValueError:
                print(f"Skipping line due to parsing error: {line.strip()}")
        
        if count == 0:
            print("No valid time entries found.")
            return None, None, None
        
        average_time = total_time / count
        return average_time, min_time, max_time

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None, None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None


file_path = "./data/12/12_30/results/ortools_results.txt"

average_time, min_time, max_time = calculate_time_stats(file_path)
if average_time is not None:
    print(f"{average_time:.4f}, {min_time:.4f}, {max_time:.4f}")
