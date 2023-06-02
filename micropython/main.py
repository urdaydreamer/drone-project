import machine
import time
from tcs34725 import TCS34725
from mx1508 import MX1508
from vl53l0x import VL53L0X  
wdt = WDT(timeout=1111)                                       #Запускаем watchdog timer, не забыть wdt.feed(), чтобы его сбрасывать, а то устройство перезагрузится

# создаем объекты датчиков

timer = machine.Timer(0)
timer.init(period=7, mode=machine.Timer.PERIODIC, callback=)  #инициализируем таймер, который каждые 7 мс будет вызывать функцию в callback'е
color_recognition = TCS34725(scl_pin=22, sda_pin=21)     #инициализируем наш датчик, который определяет цвета
i2c = machine.I2C(scl=machine.Pin(26), sda=machine.Pin(25))   #инициализируем порты для лазерного датчика (датчик расстояния)
distance_recognition = VL53L0X(i2c)                           #датчик расстояния
optical_sensor = OpticalSensor(11)                            #Пин оптического сенсора

# чтение цветов и вывод значений CMYK и расстояния

while True:
    c, m, y, k = color_recognition.read_color()
    distance = distance_recognition.read()
    print("Cyan: {:.2f}, Magenta: {:.2f}, Yellow: {:.2f}, Black: {:.2f}, Distance: {} mm".format(c, m, y, k, distance))
    count = optical_sensor.get_count() #
    if count >= 100  #Подобрать значения


