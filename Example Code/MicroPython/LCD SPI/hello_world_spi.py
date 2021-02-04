from LCD_SPI import *    #import LCD_SPI library

# SPI LCD Display

lcd = LCD(sck=2, scl=3)  # Create LCD object with LCD's sck pin connected to PICO's sck pin 2, LCD's sda pin connected to Pico's tx pin 3
lcd.set_cursor(0,0)          # Set the cursor at first column, first row
lcd.write("Hello World")     # Write string to the LCD   