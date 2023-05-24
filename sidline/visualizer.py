import websock
import json
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# Opens TCP connection
sock = websock.TCPClient("192.168.0.47", 5500).r()
conn = websock.TCPConnection(sock)

# Configure plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d') # Set plot to 3d mode

def update(i):
    # Sends message to server asking for data
    conn.send("s".encode("utf-8"))
    # Sends the data
    data = conn.receive()
    data = data.replace("'", '"')
    data = json.loads(data)["accel"]

    plt.cla()
    X = 0
    Y = 0
    Z = 0
    U = data['x']
    V = data['y']
    W = data['z']
    print(U,V,W)
    ax.set_xlim(-16, 16)
    ax.set_ylim(-16, 16)
    ax.set_zlim(-16, 16)
    ax.quiver(X, Y, Z, U, V, W)

ani = FuncAnimation(fig, update, interval=1, cache_frame_data=False)
plt.show()
