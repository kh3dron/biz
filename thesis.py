import numpy as np
import matplotlib.pyplot as plt

# plot a quadratic for FCC passing through (0,0), (.5, 1), and (1, 0)
x = np.linspace(0, 1, 100) # this generates 100 points between 0 and 1
y = -4 * (x - .5)**2 + 1
plt.plot(x, y, label='FCC')

# plot upward opening cubics for ICs
x = np.linspace(.15, .35, 100) # 100 points from .15 to .35
y = 25 * (x - .25)**2 + x + .25
plt.plot(x, y, label='IC1', color='red') # add to the "plot" object

x = np.linspace(.65, .85, 100)
y = 25 * (x - .75)**2 + 2 - 2*x
plt.plot(x, y, label='IC2', color='green')

# manually changable eprime
eprime = .2

# replot two IC curves with added eprime
x = np.linspace(.15, .35, 100)
y = 25 * (x - .25)**2 + x + .25 + eprime
plt.plot(x, y, label='IC1\'', color = 'red')

x = np.linspace(.65, .85, 100)
y = 25 * (x - .75)**2 + 2 - 2*x + eprime
plt.plot(x, y, label='IC2\'', color = 'green')


# adding more stuff to the plot
plt.title('Equilibrium with Risk-Averse Agents')
plt.xlabel('Incentive pay parameter (β)')
plt.ylabel('Output/Utility (α)')
plt.legend()
plt.grid(True)

plt.xlim(0, 1.2)
plt.ylim(0, 2)

plt.show() # finally, display the "plot" object
