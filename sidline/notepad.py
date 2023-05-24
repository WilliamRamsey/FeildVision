from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


# Configure plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d') # Set plot to 3d mode

def update(i):
    plt.cla()
    X = 0
    Y = 0
    Z = 0
    U = 10
    V = 12
    W = 12
    print(U,V,W)
    ax.set_xlim(-16, 16)
    ax.set_ylim(-16, 16)
    ax.set_zlim(-16, 16)
    ax.quiver(X, Y, Z, U, V, W)

ani = FuncAnimation(fig, update, interval=1, cache_frame_data=False)
plt.show()
