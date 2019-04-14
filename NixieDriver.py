import RPi.GPIO as GPIO

class Nixie:
    def __init__(self):
        self.Nixie_pinout = [[12, 16, 18, 22],
                [24, 26, 32, 36],
                [38, 40, 37, 35],
                [33, 31, 29, 23],
                [21, 19, 15, 13],
                [11, 7, 5, 3]]
        self.Neon_pins = [10,8]
        GPIO.setmode(GPIO.BOARD)
        for Nixie_pins in self.Nixie_pinout:
            GPIO.setup(Nixie_pins, GPIO.OUT)
        GPIO.setup(self.Neon_pins, GPIO.OUT)

    def display_number(self, Number, leading_zeros=True):
        num_str = str(Number)
        while len(num_str) < 6:
            if leading_zeros:
                num_str = '0' + num_str
            else:
                num_str = 'A' + num_str
        i = 0
        for digit in num_str:
            if digit == 'A':
                binary = '{0:04b}'.format(15)
            else:
                num_digit = int(digit)
                binary = '{0:04b}'.format(num_digit)
            binary = map(int, binary)
            GPIO.output(self.Nixie_pinout[i], binary)
            i += 1

    def setNeon(self, state):
        GPIO.output(self.Neon_pins, state)

    def toggleNeon(self):
        if GPIO.input(self.Neon_pins[0]):
            GPIO.output(self.Neon_pins, [0, 0])
        else:
            GPIO.output(self.Neon_pins, [1, 1])