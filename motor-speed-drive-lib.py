from machine import Pin, PWM

class MotorController:
    def __init__(self, enable_pin, in1_pin, in2_pin, freq=1000):
        self.enable_pin = enable_pin
        self.in1_pin = in1_pin
        self.in2_pin = in2_pin
        self.freq = freq

        self.enable_pwm = PWM(Pin(enable_pin), freq=freq)
        self.in1_pin = Pin(in1_pin, Pin.OUT)
        self.in2_pin = Pin(in2_pin, Pin.OUT)

    def set_speed(self, speed):
        self.enable_pwm.duty(speed)

    def forward(self):
        self.in1_pin.on()
        self.in2_pin.off()

    def backward(self):
        self.in1_pin.off()
        self.in2_pin.on()

    def stop(self):
        self.in1_pin.off()
        self.in2_pin.off()


                #Example code:
#motor_controller = MotorController(enable_pin=0, in1_pin=1, in2_pin=2)
#motor_controller.set_speed(512)  # Set motor speed (0-1023)
#motor_controller.forward()  # Move motor forward
