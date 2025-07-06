import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (12, 8))
n = np.arange(1, 1e2)
plt.plot(np.log(n), label = 'log(n)')
plt.plot(n, label = 'n')
plt.plot(n*np.log(n), label = 'nlog(n)')
plt.plot(n**2, label = '$n^2$')
plt.plot(2**n, label = '$2^n$')
plt.yscale('log')
plt.legend()
plt.show()