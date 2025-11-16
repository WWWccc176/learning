import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 240, 255, 270, 280, 253, 300, 570, 230, 330])

font1 = {"family": "serif", "color": "blue", "size": 20}
font2 = {"family": "serif", "color": "darkred", "size": 15}

plt.plot(x, y, "m^--", ms=10, mfc="c")

plt.xlabel("x-axis", fontdict=font2)
plt.ylabel("y-axis", fontdict = font2)
plt.title("plot", fontdict = font1)

plt.show()
