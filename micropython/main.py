import machine
import time
import adafruit_tcs34725
from mx1508 import MX1508
from tcs34725_cmyk import TCS34725_CMYK
from vl53l0x import VL53L0X  

# создаем объекты датчиков
color_recognition = TCS34725_CMYK(scl_pin=22, sda_pin=21)
i2c = machine.I2C(scl=machine.Pin(26), sda=machine.Pin(25))
distance_recognition = VL53L0X(i2c)

# чтение цветов и вывод значений CMYK и расстояния
while True:
    c, m, y, k = color_recognition.read_color()
    distance = distance_recognition.read()
    print("Cyan: {:.2f}, Magenta: {:.2f}, Yellow: {:.2f}, Black: {:.2f}, Distance: {} mm".format(c, m, y, k, distance))
    time.sleep(0.5)
