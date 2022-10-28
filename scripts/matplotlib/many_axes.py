import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_axes((0.1, 0.65, 0.3, 0.3))
ax2 = fig.add_axes((0.2, 0.1, 0.3, 0.3), projection="polar")
ax2 = fig.add_axes((0.4, 0.3, 0.6, 0.6), projection="3d")
plt.show()
