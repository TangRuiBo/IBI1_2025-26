import numpy as np
import matplotlib.pyplot as plt

N = 10000          #total population
beta = 0.3         
gamma = 0.05       
time_steps = 1000  #time consumption

S = [N - 1]
I = [1]
R = [0]

for t in range(time_steps):
    s = S[-1]
    i = I[-1]
    r = R[-1]
    
    
    new_inf = 0
    for _ in range(s):
        inf_prob = beta * (i / N)
        # Choose 1 = infected, 0 = not
        result = np.random.choice([0, 1], p=[1 - inf_prob, inf_prob])
        new_inf += result

    new_rec = 0
    for _ in range(i):
        result = np.random.choice([0, 1], p=[1 - gamma, gamma])
        new_rec += result

    S.append(s - new_inf)
    I.append(i + new_inf - new_rec)
    R.append(r + new_rec)


plt.figure(figsize=(8, 5), dpi=150)
plt.plot(S, label='Susceptible', color='blue')
plt.plot(I, label='Infected', color='red')
plt.plot(R, label='Recovered', color='green')

plt.xlabel("Time Steps")
plt.ylabel("Population")
plt.title("Stochastic SIR Model ")
plt.legend()
plt.grid(alpha=0.3)
plt.show()