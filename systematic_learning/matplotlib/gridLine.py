import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 240, 255, 270, 280, 253, 300, 570, 230, 330])

font1 = {"family": "serif", "color": "blue", "size": 20}
font2 = {"family": "serif", "color": "darkred", "size": 15}

plt.plot(x, y, "m^--", ms=10, mfc="c")

plt.xlabel("x-axis", fontdict=font2)
plt.ylabel("y-axis", fontdict=font2)
plt.title("NB Plot", fontdict=font1, loc="left")

plt.grid(color="green", linestyle = '-.', linewidth = 0.5)

plt.show()
