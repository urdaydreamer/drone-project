import machine
import time
import adafruit_tcs34725
from mx1508 import MX1508
from tcs34725_cmyk import TCS34725_CMYK

# создаем объект датчика TCS34725 в формате CMYK
color_recognition = TCS34725_CMYK(scl_pin=22, sda_pin=21)   #Использовать другие пины

# чтение цветов и вывод значений CMYK
while True:
    c, m, y, k = color_recognition.read_color()
    print("Cyan: {:.2f}, Magenta: {:.2f}, Yellow: {:.2f}, Black: {:.2f}".format(c, m, y, k))
    time.sleep(0.5)



