import picokeypad as pads

RED = 0
BLUE = 1
GREEN = 2
YELLOW = 3
PINK = 4
    
NUM_PADS = pads.get_num_pads()

def setColor(button, keypadColor):
    if keypadColor == RED:
        pads.illuminate(button, 0xff, 0x00, 0x00)
    elif keypadColor == BLUE:
        pads.illuminate(button, 0x00, 0x00, 0xff)
    elif keypadColor == GREEN:
        pads.illuminate(button, 0x00, 0xff, 0x00)
    elif keypadColor == PINK:
        pads.illuminate(button, 0xff, 0x00, 0xff)
    elif keypadColor == YELLOW:
        pads.illuminate(button, 0xff, 0x80, 0x00)
        

def clear():    
    for button in range (0, NUM_PADS):
        pads.illuminate(button, 0,0,0)
        pads.update()
        
def single_button_from_button_states(button_states):
    # returns button number between 0 and 15
    # will ignore multiple buttons
    if button_states == 1: return 0
    if button_states == 2: return 1
    if button_states == 4: return 2
    if button_states == 8: return 3
    if button_states == 16: return 4
    if button_states == 32: return 5
    if button_states == 64: return 6
    if button_states == 128: return 7
    if button_states == 256: return 8
    if button_states == 512: return 9
    if button_states == 1024: return 10
    if button_states == 2048: return 11
    if button_states == 4096: return 12
    if button_states == 8192: return 13
    if button_states == 16384: return 14
    if button_states == 32768: return 15
    else: return -1

def all_buttons_from_button_states(button_states):
    # return array of values, either 0 or 1 
    # refreshes on button ups however many buttons are pressed
    if NUM_PADS == 16: #assuming this to keep it small and fast
        return [
            button_states & 1,
            button_states>>1 & 1,
            button_states>>2 & 1,
            button_states>>3 & 1,
            button_states>>4 & 1,
            button_states>>5 & 1,
            button_states>>6 & 1,
            button_states>>7 & 1,
            button_states>>8 & 1,
            button_states>>9 & 1,
            button_states>>10 & 1,
            button_states>>11 & 1,
            button_states>>12 & 1,
            button_states>>13 & 1,
            button_states>>14 & 1,
            button_states>>15 & 1,
            ]
    else:
        raise Exception('Keypad must have 16 buttons')