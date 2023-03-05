import machine
import time
import adafruit_tcs34725
from mx1508 import MX1508

# настройки I2C
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21)) #Это рандомные пины, поставить те, что будут использваоться

# создаем объект датчика TCS34725
color_sensor = adafruit_tcs34725.TCS34725(i2c)

# настройки датчика
color_sensor.integration_time = adafruit_tcs34725.INTEGRATION_TIME_50MS
color_sensor.gain = adafruit_tcs34725.GAIN_4X

# цикл чтения цветов
while True:
    r, g, b = sensor.color_rgb_bytes
    print("Red: {}, Green: {}, Blue: {}".format(r, g, b))
    time.sleep(0.5)
