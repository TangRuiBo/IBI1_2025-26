import numpy as np
import matplotlib.pyplot as plt


N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

vaccine_ratios = np.arange(0, 1.1, 0.1)

plt.figure(figsize=(9, 5), dpi=150)


for vac_ratio in vaccine_ratios:
    initial_vaccinated = int(N * vac_ratio)
    S = [N - 1 - initial_vaccinated]
    I = [1]
    R = [initial_vaccinated]

   
    for _ in range(time_steps):
        current_S = S[-1]
        current_I = I[-1]
        current_R = R[-1]

       
        inf_prob = beta * current_I / N
        new_infected = 0
        if current_S > 0:
            new_infected = np.sum(np.random.choice([0, 1], size=current_S, p=[1-inf_prob, inf_prob]))

       
        new_recovered = 0
        if current_I > 0:
            new_recovered = np.sum(np.random.choice([0, 1], size=current_I, p=[1-gamma, gamma]))

     
        S.append(current_S - new_infected)
        I.append(current_I + new_infected - new_recovered)
        R.append(current_R + new_recovered)

   
    plt.plot(I, label=f'Vaccine: {int(vac_ratio*100)}%')

plt.xlabel('Time Steps')
plt.ylabel('Number of Infected Individuals')
plt.title('SIR Model with Different Vaccination Rates (Total Population = 10000)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') 
plt.tight_layout()
plt.grid(alpha=0.3)
plt.show()