#!/usr/bin/env python3

import gpiozero as gp
import time

blue = gp.LED(4)
button1 = gp.Button(17)
button2 = gp.Button(27)
red = gp.LED(22)

if __name__ == "__main__":
    print("Flashing blue LED (LED 1)...")
    time.sleep(1)
    blue.blink(n=3, background=False)
    time.sleep(2)

    print("Flashing red LED (LED 2)...")
    time.sleep(1)
    red.blink(n=3, background=False)
    time.sleep(2)

    print("Press Button 1...")
    button1.wait_for_press()
    print("Input good")
    time.sleep(2)

    print("Press Button 2...")
    button2.wait_for_press()
    print("Input good")
    time.sleep(2)
