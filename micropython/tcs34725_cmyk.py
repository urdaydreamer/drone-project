import time
import tcs34725
from machine import I2C, Pin
i2c = I2C(scl = Pin(22), sda = Pin(21))
print(hex(i2c.scan()[0]))
sensor = tcs34725.TCS34725(i2c)
sensor.gain(16)
sensor.integration_time(505)
while True:
    print("The rgb are {}".format(tcs34725.html_rgb(sensor.read('row'))))


