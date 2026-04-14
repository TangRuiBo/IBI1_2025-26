import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

"""1.Create 100x100 grid, all susceptible
   2.Set one random cell to infected
   3.Define 8 surrounding neighbors
   For each simulation day:
   4.Copy current grid to avoid update conflicts
   5.Infect susceptible neighbors of infected cells
   6.Let infected cells recover randomly
   7.Replace grid with new state
   8.Draw heat map with day number
   9.Show color legend for states
   10.Pause 0.5 seconds for display"""


GRID_SIZE = 100
INFECTION_RATE = 0.3
RECOVERY_RATE = 0.05
TIME_STEPS = 101

population = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

x0, y0 = np.random.randint(0, GRID_SIZE, 2)
population[x0, y0] = 1

neighbors = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),          (0, 1),
             (1, -1),  (1, 0), (1, 1)]

plt.figure(figsize=(7, 7), dpi=120)
plt.ion()

for day in range(TIME_STEPS):
    new_pop = population.copy()
    infected_cells = np.argwhere(population == 1)

    for (x, y) in infected_cells:
        for dx, dy in neighbors:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                if population[nx, ny] == 0:
                    if np.random.random() < INFECTION_RATE:
                        new_pop[nx, ny] = 1

    for (x, y) in infected_cells:
        if np.random.random() < RECOVERY_RATE:
            new_pop[x, y] = 2

    population = new_pop

    plt.clf()
    im = plt.imshow(population, cmap='viridis', vmin=0, vmax=2)
    
    plt.title(f'Spatial SIR Model | Day {day}', fontsize=14)
    
    purple_patch = mpatches.Patch(color='#440154', label='Susceptible')
    green_patch = mpatches.Patch(color='#21918c', label='Infected')
    yellow_patch = mpatches.Patch(color='#fde725', label='Recovered')
    plt.legend(handles=[purple_patch, green_patch, yellow_patch], loc='upper right')
    
    plt.axis('off')
    plt.pause(0.5)

plt.ioff()
plt.show()