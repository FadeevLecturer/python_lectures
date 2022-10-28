import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.cos(x)

fig, ax = plt.subplots()

circle = plt.Circle((6000, -4000), 1000, color="red")
image = plt.imread("cat.jpg")

ax.imshow(image)
ax.add_patch(circle)
(line,) = ax.plot(x * 1000, y * 5000)
plt.show()
