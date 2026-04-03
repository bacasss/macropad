from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.oled import OLED
import board
import busio
from adafruit_ssd1306 import SSD1306_I2C

keyboard = KMKKeyboard()
keyboard.row_pins = (board.GP1, board.GP2, board.GP3)        
keyboard.col_pins = (board.GP7, board.GP8, board.GP9, board.GP10)  
keyboard.diode_orientation = keyboard.DIODE_COL2ROW

keyboard.keymap = [
    [KC_1, KC_2, KC_3, KC_LSFT,
     KC_4, KC_5, KC_6, KC_LCTL,
     KC_7, KC_8, KC_9, KC_0]
]

encoder = EncoderHandler()
encoder.pins = [(board.GP4, board.GP11)]
encoder.map = {0: (KC_VOLU, KC_VOLD)}
keyboard.modules.append(encoder)

i2c = busio.I2C(scl=board.GP6, sda=board.GP5)
oled_display = SSD1306_I2C(128, 32, i2c)

class StaticOLED(OLED):
    def update(self, keyboard):
        self.oled.fill(0)
        self.oled.text("bacasss", 0, 0, 1)
        self.oled.show()

oled = StaticOLED(oled_display)
keyboard.modules.append(oled)

if __name__ == "__main__":
    keyboard.go()
