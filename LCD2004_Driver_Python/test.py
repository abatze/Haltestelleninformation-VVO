import lcddriver
from time import *

lcd = lcddriver.lcd()

lcd.lcd_display_string("********************", 1)
lcd.lcd_display_string("*  Funktioniert!   *", 2)
lcd.lcd_display_string("*  auctoritas.ch   *", 3)
lcd.lcd_display_string("********************", 4)
