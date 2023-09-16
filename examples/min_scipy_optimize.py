import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

f = lambda x: 0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4
viz_range = np.array([-6, 12])
max_iter = 100
min_tol = 1e-6
x_init = 12 # Try -2, 0, and 16/6

# Find the minimum by SciPy
result = minimize(f, x_init, tol=min_tol, options={'maxiter': max_iter, 'return_all': True})
print(result)

# Visualize all iterations
xs = np.linspace(*viz_range, 100)
plt.plot(xs, f(xs), 'r-', label='f(x)', linewidth=2)
xr = np.vstack(result.allvecs)
plt.plot(xr, f(xr), 'b.', label='Each step', markersize=12)
plt.legend()
plt.axis((*viz_range, *f(viz_range)))
plt.show()
