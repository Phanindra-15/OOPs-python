

#we can create lab for the plots in this way

#labellng is done for both x-axis and y-axis


import numpy as np
import matplotlib.pyplot as plt

x = np.array([30, 45, 60, 75, 100, 115, 120, 140, 150, 185])
y = np.array([140, 150, 160, 170, 180, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("parent number")
plt.ylabel("student number ")

plt.show()
