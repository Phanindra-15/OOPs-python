

#to plot some points without line by specific symbol



import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 9])
ypoints = np.array([1, 10])

plt.plot(xpoints, ypoints, 's')
plt.show()
