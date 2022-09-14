
#to mark each point with circle

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
xpoints = np.array([1, 5, 1, 9])

plt.plot(ypoints, marker = 'o')
plt.plot(xpoints, marker = 's')
plt.show()
