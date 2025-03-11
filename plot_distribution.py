import matplotlib.pyplot as plt
from run_mcmc import potential_energy
import numpy as np

def plot_distribution(samples, xmin=-2.5, xmax=2.5, bins=100, kBT=.5):
    x_values = np.linspace(xmin, xmax, 10000) #10000 points in x for plotting PES
    dx = x_values[1] - x_values[0] # step in x for numerical integration of partition function
    Z = sum(np.exp(-potential_energy(x_values) / kBT)) * dx # discrete partition function
    PDF = 1/Z * np.exp(-potential_energy(x_values) / kBT) # normalized probability density function
    plt.figure(figsize=(10, 6))
    plt.hist(samples, bins=bins, density=True, alpha=0.6, label='MCMC Samples')
    plt.plot(x_values, PDF, label='True Distribution', color='red')
    plt.title('MCMC Sampling of $V(x) = (x-1)^2 (x+1)^2$')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.savefig('mcmc_sampling.jpg', dpi=300)
    plt.show()
