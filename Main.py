# type: ignore
import time
import board
import digitalio
import pwmio

# Motor A (Left)
in1 = digitalio.DigitalInOut(board.D5)
in1.direction = digitalio.Direction.OUTPUT

in2 = digitalio.DigitalInOut(board.D6)
in2.direction = digitalio.Direction.OUTPUT

ena = pwmio.PWMOut(board.D8, frequency=1000)  # ENA = speed for motor A

# Motor B (Right)
in3 = digitalio.DigitalInOut(board.D3)
in3.direction = digitalio.Direction.OUTPUT

in4 = digitalio.DigitalInOut(board.D4)
in4.direction = digitalio.Direction.OUTPUT

enb = pwmio.PWMOut(board.D10, frequency=1000)  # ENB = speed for motor B

while True:
    print("Forward")
    in1.value = True
    in2.value = False
    ena.duty_cycle = int(0.5 * 65535)  # Motor A at 50%

    in3.value = True
    in4.value = False
    enb.duty_cycle = int(0.5 * 65535)  # Motor B at 50%

    time.sleep(2)
