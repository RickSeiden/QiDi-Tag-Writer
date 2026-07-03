# QiDi-Tag-Writer

This device, based on a Raspberry Pi Pico of any variety, writes RFID Tags for use with the QiDi Box.
<p></p>
<img src="QiDi Tag Writer.png"/>
<p></p>

**BOM:**

* Raspberry Pi Pico, Pico W, Pico 2 or Pico 2W
* Rotary Encoder with button
* 10K Pot
* PN532 NFC RFID Module
* 16x2 LCD display
* 3D printed case


The code is written in CircuitPython instead of MicroPython because of some Adafruit libraries that made it easier to code with.  You can download the latest version of CircuitPython [here](https://circuitpython.org/downloads).  Instructions for using CircuitPython are found [here](https://docs.circuitpython.org/en/latest/README.html).  Note that the Adafruit libraries are maintained and owned by Adafruit and are provided here for completness of the code needed for this project.  There have been no changes made to the Adafruit code provided here.

To use it, press the button of the rotary encoder and the tag writer will ask you for a color. Use the rotary encoder to select your color and press the button again.  Then you can use the rotary encoder to pick your filament and press the button.  Then you can tap your tag to the top of the device, and it will write your tag.  Hold the button on the rotary encoder down to return to the "title screen."
