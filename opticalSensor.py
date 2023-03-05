class OpticalSensor:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.IN)
        self.count = 0
        self.pin.irq(handler=self.callback, trigger=Pin.IRQ_FALLING)

    def callback(self, pin):
        self.count += 1

    def get_count(self):
        return self.count
