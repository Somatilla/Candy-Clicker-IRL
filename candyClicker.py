import utime
import machine
from machine import I2C
from machine import Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 26
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

candies = 0
clickingPower = 1
candyPerSecond = 0
buttonpress = 0
buttonpress2 = 0
cps = True

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

previousButtonState = button.value()

lcd.putstr("candies:")
while True:
    if candyPerSecond > 0:
        candies += candyPerSecond/1000
        lcd.move_to(9,0)
        lcd.putstr(str(candies))
    currentButtonState = button.value()
    lcd.hide_cursor()
    lcd.blink_cursor_off()
    if currentButtonState != previousButtonState:
        utime.sleep(0.02)
        if button.value() == currentButtonState:
            if currentButtonState == 1:
                print("buttonpress:" + str(buttonpress), str(buttonpress2))
                candies = candies + (1 * clickingPower)
                buttonpress += 1
                buttonpress2 += 1
                lcd.move_to(9,0)
                lcd.putstr(str(candies))
    
    previousButtonState = currentButtonState
    
    if buttonpress % 10 == 0:
        print(clickingPower)
        clickingPower += 0.01
        clickingPower = round(clickingPower, 2)
        buttonpress += 1
        lcd.move_to(0,1)
        lcd.putstr("CP:" + str(clickingPower))
    elif buttonpress2 % 100 == 0:
        candyPerSecond += 0.01
        candyPerSecond = round(candyPerSecond, 2)
        print("CPS:" + str(candyPerSecond))
        buttonpress2 += 1
        lcd.move_to(8,1)
        lcd.putstr("CPS:" + str(candyPerSecond))
    
        
        
