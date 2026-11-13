import board
import digitalio
import audiobusio
import audiocore
import time
import audiomp3
import touchio
from board import *

touch_pin = touchio.TouchIn(board.GP0)

audio = audiobusio.I2SOut(
    bit_clock=board.GP2,
    word_select=board.GP3,
    data=board.GP4,
)

mp3 = audiomp3.MP3Decoder("acoustic-guitar.mp3")
previous = True
last_press = 0.0
DEBOUNCE = 0.04

while True:
    if touch_pin.value:
        print("touched")
        audio.play(mp3)