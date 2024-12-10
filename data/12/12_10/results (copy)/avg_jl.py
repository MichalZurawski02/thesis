# Script to calculate average, min, and max time for the new file format

def calculate_time_stats_new_format(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Extracting time values
        total_time = 0.0
        count = 0
        min_time = float('inf')
        max_time = float('-inf')
        
        for line in lines:
            try:
                parts = line.split(';')
                if len(parts) >= 3:
                    time_value = float(parts[2])  # 3rd column is the time
                    
                    # Update total, min, and max
                    total_time += time_value
                    count += 1
                    min_time = min(min_time, time_value)
                    max_time = max(max_time, time_value)
            except ValueError:
                print(f"Skipping line due to parsing error: {line.strip()}")
        
        # Check if any valid time entries were found
        if count == 0:
            print("No valid time entries found.")
            return None, None, None
        
        # Calculate average
        average_time = total_time / count
        return average_time, min_time, max_time

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None, None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None

file_path = "./data/50/50_300/results/results.txt"

average_time, min_time, max_time = calculate_time_stats_new_format(file_path)
if average_time is not None:
    print(f"{average_time:.8f}, {min_time:.8f}, {max_time:.8f}")
