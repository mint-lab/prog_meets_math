import numpy as np
import matplotlib.pyplot as plt

hist_pts = 10000
hist_bins = 100
dice_range = (1, 6)
n = 100 # Please decrease and increase `n`

# Acquire multiple sample means
samples = []
for i in range(hist_pts):
    samples.append(np.mean(np.random.randint(dice_range[0], dice_range[1]+1, n)))

# Visualize the distribution of sample means
plt.title(f'Sample Mean (n = {n})')
plt.hist(samples, bins=hist_bins, range=dice_range, density=True, align='mid')
plt.xlim(dice_range[0]-0.5, dice_range[1]+0.5)
plt.yticks([])
plt.show()