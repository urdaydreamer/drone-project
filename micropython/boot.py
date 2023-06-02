# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
#cfrom machine import WDT
from time import sleep
#wdt = WDT(timeout=4000)
sleep(3)
#wdt.feed()