import board
import busio
import time
import digitalio
import rotaryio

import adafruit_character_lcd.character_lcd as characterlcd

from adafruit_pn532.adafruit_pn532 import MIFARE_CMD_AUTH_A
from adafruit_pn532.adafruit_pn532 import MIFARE_CMD_AUTH_B
from adafruit_pn532.uart import PN532_UART
from adafruit_debouncer import Debouncer

from materials import Materials
from filament_colors import FilamentColors

currentFilament=[0x0, 0x0]

mat=Materials()

fil=FilamentColors()

encoder = rotaryio.IncrementalEncoder(board.GP27, board.GP28)
last_position = None

"""
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
    last_position = position
"""
pin = digitalio.DigitalInOut(board.GP26)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP
switch = Debouncer(pin)

uart = busio.UART(board.GP0, board.GP1, baudrate=115200, timeout=0.1)
pn532 = PN532_UART(uart, debug=False)

pn532.SAM_configuration()

lcd_columns = 16
lcd_rows = 2

lcd_rs = digitalio.DigitalInOut(board.GP15)
lcd_en = digitalio.DigitalInOut(board.GP14)
lcd_d7 = digitalio.DigitalInOut(board.GP10)
lcd_d6 = digitalio.DigitalInOut(board.GP11)
lcd_d5 = digitalio.DigitalInOut(board.GP12)
lcd_d4 = digitalio.DigitalInOut(board.GP13)
lcd_backlight = digitalio.DigitalInOut(board.GP9)
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight
)

STATE_IDLE = 0
STATE_FIL = 1
STATE_COLOR = 2
STATE_MAT = 3
STATE_WRITE = 4
STATE_READ = 5
state=STATE_IDLE
lcd.clear()
stateChanged=True

debug=True
def setMessage(line1, line2):
    if (debug):
        print(line1)
        print(line2)
    lcd.clear()
    lcd.message = "{}\n{}".format(line1, line2)

def authenticate(uid):
    key = b"\xff\xff\xff\xff\xff\xff"
    authenticated = False
    authenticated = pn532.mifare_classic_authenticate_block(
            uid, 4, MIFARE_CMD_AUTH_A, key
        )
    if (authenticated is False):
        authenticated = pn532.mifare_classic_authenticate_block(
            uid, 4, MIFARE_CMD_AUTH_B, key
        )
    return authenticated

def readBlock(block):
    setMessage("Waiting for card to read", "")
    while True:
        # Check if a card is available to read
        uid = pn532.read_passive_target(timeout=0.5)
        # Try again if no card is available.

        if uid is not None:
            print(authenticate(uid))
            return pn532.mifare_classic_read_block(block)
            break
        time.sleep(0.5)

def writeBlock(block, data):
    global state
    global stateChanged
    wrote=False

    while (state==STATE_WRITE):
        try:
            setMessage("Waiting for card to write", "Hold when done")
            # Check if a card is available to read
            uid = pn532.read_passive_target(timeout=0.5)
            # Try again if no card is available.
            if uid is not None:
                authenticate(uid)
                wrote=pn532.mifare_classic_write_block(block, data)
                if (wrote):
                    setMessage("Wrote to NFC","")
                else:
                    setMessage("Write failed","")
                time.sleep(1)
                """
                counter=0
                while (state==STATE_WRITE and counter<40):
                    time.sleep(0.1)
                    counter=counter+1
                """
            switch.update()
            fell=switch.fell
            #print("{}: {}".format(time.time(),fell))
            if (fell):
                state=STATE_IDLE
                stateChanged=True
        except Exception as e:
            setMessage("Error occurred.", "Try again.")
            time.sleep(1)




while True:
    if (state==STATE_IDLE):
        if (stateChanged):
            stateChanged=False
            setMessage("  Qidi Box NFC","     Writer")
        switch.update()
        if (switch.fell):
            state=STATE_FIL
            stateChanged=True
    if (state==STATE_FIL):
        if(stateChanged):
            stateChanged=False
            encoder.position=0
            last_position=0
            setMessage("Pick a color",fil.colors[encoder.position][fil.colorName])
        position=encoder.position
        if (position!=last_position):
            last_position=position
            if (last_position>=fil.length):
                last_position=0
                encoder.position=last_position
            elif (last_position<0):
                last_position=fil.length-1
                encoder.position=last_position
            setMessage("Pick a color",fil.colors[encoder.position][fil.colorName])

            #set neopixel color to fil.colors[encoder.position][fil.colorValue]
        switch.update()
        if (switch.fell):
            currentFilament[0]=fil.colors[encoder.position][fil.colorCode]
            stateChanged=True
            state=STATE_MAT
    if (state==STATE_MAT):
        if(stateChanged):
            stateChanged=False
            encoder.position=0
            last_position=0
            setMessage("Pick a filament",mat.materials[encoder.position][mat.materialName])
        position=encoder.position
        if (position!=last_position):
            last_position=position
            if (last_position>=mat.length):
                last_position=0
                encoder.position=last_position
            elif (last_position<0):
                last_position=mat.length-1
                encoder.position=last_position
            setMessage("Pick a filament",mat.materials[encoder.position][mat.materialName])

        switch.update()
        if (switch.fell):
            currentFilament[1]=mat.materials[encoder.position][mat.materialCode]
            stateChanged=True
            state=STATE_WRITE
    if(state==STATE_WRITE):
        if (stateChanged):
            stateChanged=False
            material=currentFilament[1]
            color=currentFilament[0]
            manufacturer=1
            data = bytearray(16)
            data[0:16] = b"\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            data[0]=material
            data[1]=color
            """
                writeBlock will set the state to STATE_IDLE when done
                and won't return until then
            """
            writeBlock(4,data)

