import utime

PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
ACCEL_CONFIG = 0x1C
TEMP_OUT_H = 0x41
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43

def init_mpu6050(i2c, address=0x68):
    i2c.writeto_mem(address, PWR_MGMT_1, b'\x00')
    utime.sleep_ms(100)
    i2c.writeto_mem(address, SMPLRT_DIV, b'\x07')
    i2c.writeto_mem(address, CONFIG, b'\x00')
    i2c.writeto_mem(address, GYRO_CONFIG, b'\x00') # Set Gyro Full Scale Range to ±250deg/s
    i2c.writeto_mem(address, ACCEL_CONFIG, b'\x18') # Set Accelerometer Full Scale Range (+-2g = 0x00 +-4g=0x08 +-8g=0x10, +-16g = 0x18)
 
def read_raw_data(i2c, addr, address=0x68):
    high = i2c.readfrom_mem(address, addr, 1)[0]
    low = i2c.readfrom_mem(address, addr + 1, 1)[0]
    value = high << 8 | low
    if value > 32768:
        value = value - 65536
    return value
 
def get_mpu6050_data(i2c):
    temp = read_raw_data(i2c, TEMP_OUT_H) / 340.0 + 36.53
    accel_x =  read_raw_data(i2c, ACCEL_XOUT_H) / 2048 # 16384.0 for +- 2g, 8192.0 for +- 4g, 4096.0 for +- 8g, 2048.0 for +- 16g
    accel_y = read_raw_data(i2c, ACCEL_XOUT_H + 2) / 2048
    accel_z = read_raw_data(i2c, ACCEL_XOUT_H + 4) / 2048
    gyro_x = read_raw_data(i2c, GYRO_XOUT_H) / 131.0
    gyro_y = read_raw_data(i2c, GYRO_XOUT_H + 2) / 131.0
    gyro_z = read_raw_data(i2c, GYRO_XOUT_H + 4) / 131.0
 
    return {
        "temp": temp,
        "accel": {
            "x": accel_x,
            "y": accel_y,
            "z": accel_z,
        },
        "gyro": {
            "x": gyro_x,
            "y": gyro_y,
            "z": gyro_z,
        }}