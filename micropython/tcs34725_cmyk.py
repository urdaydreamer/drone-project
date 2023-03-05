import time
import adafruit_tcs34725
from adafruit_tcs34725 import INTEGRATION_TIME_50MS, GAIN_4X

class TCS34725_CMYK:
    def __init__(self, scl_pin, sda_pin):
        i2c = machine.I2C(scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin))
        self.sensor = adafruit_tcs34725.TCS34725(i2c)
        self.sensor.integration_time = INTEGRATION_TIME_50MS
        self.sensor.gain = GAIN_4X

    def read_color(self):
        r, g, b = self.sensor.color_rgb_bytes
        c = 1 - r / 255
        m = 1 - g / 255
        y = 1 - b / 255
        k = min(c, m, y)
        if k == 1:
            c, m, y = 0, 0, 0
        else:
            c = (c - k) / (1 - k)
            m = (m - k) / (1 - k)
            y = (y - k) / (1 - k)
        return c, m, y, k
