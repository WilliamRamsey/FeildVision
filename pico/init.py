import internet
import websock
import mpu6050
from machine import Pin, I2C


# Defines network ID and password
ssid = 'Airwaves'
password = 'nowisthetime'

# Connects to the internet
internet.connect(ssid, password)

# Defines the IP address and port for communicating with the on feild computer
HOST = internet.connect(ssid, password)
PORT = 5500

# Connercts to on feild computer (the pico acts as a web server and the on field computer a client)
connection, client_address = websock.TCPServer(HOST, PORT).connect_socket()
conn = websock.TCPConnection(connection)

# Connects to MPU-6050
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
print(i2c)
mpu6050.init_mpu6050(i2c)
data = mpu6050.get_mpu6050_data(i2c)

# Streams data to computer
while True:
    rec = conn.receive()
    data = mpu6050.get_mpu6050_data(i2c)
    conn.send(str(data).encode('utf-8'))
    
    
