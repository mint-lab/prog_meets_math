import numpy as np
import matplotlib.pyplot as plt

# Generate a population with normal distribution
np.random.seed(0)
population = np.random.normal(loc=170, scale=15, size=2000)
true_variance = np.var(population) # Population variance

# Configure the experiment
n_values = range(2, 101)
num_trials = 1000

# Estimate sample variances with different `n`
biased_vars = []    # Divided by `n`
unbiased_vars = []  # Divided by `n-1`
for n in n_values:
    biased_trials = []
    unbiased_trials = []
    for _ in range(num_trials):
        sample = np.random.choice(population, size=n, replace=False)
        sample_mean = np.mean(sample)

        biased_var = np.sum((sample - sample_mean)**2) / n
        unbiased_var = np.sum((sample - sample_mean)**2) / (n - 1)

        biased_trials.append(biased_var)
        unbiased_trials.append(unbiased_var)

    biased_vars.append(np.mean(biased_trials))
    unbiased_vars.append(np.mean(unbiased_trials))

# Plot the results
plt.figure()

plt.plot(n_values, biased_vars, color='blue', label='Biased sample variance (divided by $n$)')
plt.plot(n_values, unbiased_vars, color='green', label='Unbiased sample variance (divided by $n-1$)')
plt.plot(n_values, [true_variance]*len(n_values), color='red', label='True population variance')
# Shorter version:
# plt.axhline(y=true_variance, color='red', label='True population variance')

plt.title('Biased vs. Unbiased Sample Variance by Sample Size $n$')
plt.xlabel('Sample Size $n$') # No penalty for skipping LaTeX formatting
plt.ylabel('Average Sample Variance')
plt.xlim(2, 100)
plt.legend()
plt.grid()
plt.show()