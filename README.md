# Candy-Clicker-IRL
You know my other project candy clicker? its basically that but in irl

# How 2 play:
press the button --> get candies
every 10 candies --> get +0.01 clickingPower
every 100 candies --> get +0.01 candyPerSecond

# Ingredients:
 - Raspberry pi pico (RP 2040)
 - button
 - quapass 1602a 16x2 lcd screen
 - lcm 1602 IIC (lcd backpack)
 - wires
 - breadboard

# Assembly
 - wire the lcd in:
 - <img width="1188" height="740" alt="Schematic" src="https://github.com/user-attachments/assets/fe872254-52ca-4aa2-a35d-3acbfadcbed6" />
 - wire the button to: 3.3v and pin 14
# Drivers:
 - install Thonny and circuitpython
 - Save this guy's drivers to the pico with thonny (not the test one):
 - https://github.com/T-622/RPI-PICO-I2C-LCD
 - run the pico_i2c_lcd_test.py
 - if it works download and run candyClicker in Thonny
