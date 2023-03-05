from machine import Pin, PWM

class MX1508:
    def __init__(self, pin_in1, pin_in2, pin_in3, pin_in4):
        self.pin_in1 = Pin(pin_in1, Pin.OUT)
        self.pin_in2 = Pin(pin_in2, Pin.OUT)
        self.pin_in3 = Pin(pin_in3, Pin.OUT)
        self.pin_in4 = Pin(pin_in4, Pin.OUT)
        self.pwm_a = PWM(self.pin_in1, freq=1000, duty=0)
        self.pwm_b = PWM(self.pin_in2, freq=1000, duty=0)
        self.pwm_c = PWM(self.pin_in3, freq=1000, duty=0)
        self.pwm_d = PWM(self.pin_in4, freq=1000, duty=0)
        self.direction = None
        self.speed = 0

    def stop(self):
        self.pwm_a.duty(0)
        self.pwm_b.duty(0)
        self.pwm_c.duty(0)
        self.pwm_d.duty(0)
        self.direction = None
        self.speed = 0

    def set_speed(self, speed):
        if speed > 0:
            self.pwm_a.duty(speed)
            self.pwm_b.duty(0)
            self.pwm_c.duty(speed)
            self.pwm_d.duty(0)
            self.direction = "forward"
            self.speed = speed
        elif speed < 0:
            self.pwm_a.duty(0)
            self.pwm_b.duty(abs(speed))
            self.pwm_c.duty(0)
            self.pwm_d.duty(abs(speed))
            self.direction = "backward"
            self.speed = abs(speed)
        else:
            self.stop()

    def turn_left(self, speed):
        self.pwm_a.duty(0)
        self.pwm_b.duty(speed)
        self.pwm_c.duty(speed)
        self.pwm_d.duty(0)
        self.direction = "left"
        self.speed = speed

    def turn_right(self, speed):
        self.pwm_a.duty(speed)
        self.pwm_b.duty(0)
        self.pwm_c.duty(0)
        self.pwm_d.duty(speed)
        self.direction = "right"
        self.speed = speed

    def go_forward(self, speed):
        self.set_speed(speed)
        self.direction = "forward"

    def go_backward(self, speed):
        self.set_speed(-speed)
        self.direction = "backward"


        #Example:
# создание экземпляра моторного драйвера
#motor = MX1508(IN1_PIN, IN2_PIN, IN3_PIN, IN4_PIN)

# движение вперед со скоростью 50
#motor.go_forward(50)

# поворот налево со скоростью 30
#motor.turn_left(30)

# движение назад со скоростью 70
#motor.go_backward(70)

# остановка моторов
#motor.stop()
