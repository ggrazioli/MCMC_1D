import numpy as np

def potential_energy(x):
    return (x - 1)**2 * (x + 1)**2

def metropolis_hastings(num_samples, step_size=0.5, kBT=.5, initial_position=0.0):
    samples = [initial_position]  # Start sampling at x = 0
    for _ in range(num_samples):
        x_current = samples[-1]
        x_proposed = x_current + np.random.uniform(-step_size, step_size)

        # Compute acceptance probability
        delta_V = potential_energy(x_proposed) - potential_energy(x_current)
        acceptance_prob = np.exp(-delta_V / kBT)

        # Metropolis criterion
        if np.random.rand() < acceptance_prob:
            samples.append(x_proposed)
        else:
            samples.append(x_current)

    return np.array(samples)

