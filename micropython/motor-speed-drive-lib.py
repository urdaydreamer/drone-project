from machine import Pin, PWM


class MotorController:
    def __init__(self, in1_pin, in2_pin, enable_pin, freq=1000):
        self.in1_pin = Pin(in1_pin, Pin.OUT)
        self.in2_pin = Pin(in2_pin, Pin.OUT)
        self.enable_pin = PWM(Pin(enable_pin))
        self.enable_pin.freq(freq)
        self.enable_pin.duty(0)

    def set_speed(self, speed):
        if speed < 0:
            self.in1_pin.off()
            self.in2_pin.on()
            speed = -speed
        else:
            self.in1_pin.on()
            self.in2_pin.off()
        self.enable_pin.duty(speed)

    def forward(self):
        self.set_speed(1023)

    def backward(self):
        self.set_speed(-1023)

    def stop(self):
        self.set_speed(0)


#motor_controller = MotorController(in1_pin=1, in2_pin=2, enable_pin=0)
#motor_controller.set_speed(512)  # Set motor speed (0-1023)
#motor_controller.forward()  # Move motor forward
