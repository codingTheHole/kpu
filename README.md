# kpu: Keypad Utility
Utilities for the Pimoroni RGB Keypad

## Installation
Use Thonny (or whatever tool you use) to add the kpu.py file, and if desired the kpu_demo.py file, to your Pimoroni RGB Keypad

## Use
import picokeypad as keypad
import kpu

keypad.init()
keypad.set_brightness(1.0)
last_button_states = 0
logging=True

def handle_button_states(button_states):
    kpu.clear()
    single_button = kpu.single_button_from_button_states(button_states)
    if single_button >= 0: # -1 indicates multiple buttons
       handle_single_button(single_button)
    handle_all_buttons(kpu.all_buttons_from_button_states(button_states))   

def handle_single_button(button):
    if logging: print(button)
    kpu.setColor(button, kpu.PINK)
    keypad.update()
    
def handle_all_buttons(buttons_array):
    if logging: print(buttons_array)

while True: 
    button_states = keypad.get_button_states()
    if last_button_states != button_states:
        last_button_states = button_states
        handle_button_states(button_states)
