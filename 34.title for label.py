#in the same way we can give title to this library function as same as giving
#label for both the axis we can give title to it in this way

import numpy as np
import matplotlib.pyplot as plt


x = np.array([30, 45, 60, 75, 100, 115, 120, 140, 150, 185])
y = np.array([140, 150, 160, 170, 180, 290, 300, 310, 320, 330])


plt.plot(x, y)

plt.title("Student and Parent data with their register number")
plt.xlabel("Student registration number")
plt.ylabel("Parent regisdtrstion number")

plt.show()
