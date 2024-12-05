import matplotlib.pyplot as plt
import numpy as np

# Data
problem_sizes = ['4x4', '6x6', '8x8', '8x10', '10x15', '20x20', '30x30', '50x50']
num_variables = [11, 30, 53, 65, 112, 400, 900, 2500]
csp_julia = [0.04738900661468506, 0.15750885009765625, 0.012356042861938477, 
             0.0024590492248535156, 0.05565905570983887, 1.78, 7.782, 16.91697096824646]
ortools_cp = [0.005732629, 0.005390743, 0.006541158, 0.002894472, 
              0.012758982, 1.814487559, 7.80879523, 20.319582319000002]
ibm_ilog_cp = [0.005, 0.005, 0.012, 0.006, 0.004, 0.060307, 0.133843, 0.392880]

# Create the plot
plt.figure(figsize=(12, 6))

# Plot the solver times
plt.plot(problem_sizes, csp_julia, marker='o', color='#D2D2FF', label='CSP Julia')
plt.plot(problem_sizes, ortools_cp, marker='s', color='#E3C7F9', label='ORtools CP')
plt.plot(problem_sizes, ibm_ilog_cp, marker='^', color='#9ED7F4', label='IBM ILOG CP Optimizer')

plt.gcf().set_facecolor('#29293D')  # Light gray background
plt.gca().set_facecolor('#29293D')  # Same color for plot area



plt.title('Wyniki modułów rozwiązujących w skali logarytmicznej', color='#F5F5F5')
plt.xlabel('Rozmiar układanki', color='#F5F5F5')
plt.ylabel('Czas w sekundach', color='#F5F5F5')
plt.yscale('log')
plt.tick_params(colors='#F5F5F5')
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.xticks(rotation=45)
plt.legend(facecolor='#29293D', edgecolor='white', framealpha=0.8, labelcolor='#F5F5F5')


plt.tight_layout()
plt.show()