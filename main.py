# This Python code is a demonstration of Markov Chain Monte Carlo sampling
# applied to a 1-dimensional potential energy surface:
# V(x) = (x-1)**2 * (x+1)**2
# To run in the terminal:
# python main.py

from plot_distribution import plot_distribution
from run_mcmc import metropolis_hastings

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Parameters
    kBT = .5 # Boltzmann's constant times temperature
    num_samples = 100000
    step_size = 0.5
    initial_position = 0.0

    # Generate samples
    samples = metropolis_hastings(num_samples, step_size, kBT=kBT, initial_position=initial_position)
    plot_distribution(samples, kBT=kBT)