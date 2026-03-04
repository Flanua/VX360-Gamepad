import vgamepad as vg
from pynput import keyboard
import time

g = vg.VX360Gamepad()

# Separate loop at the beginning that taps the Start button to claim the "Player 1" slot
print("Claiming Player 1 slot...")
for _ in range(5):
    g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    g.update()
    time.sleep(0.1)
    g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    g.update()
    time.sleep(0.1)

# Global state to keep track of held keys
active_keys = set()

def update_controller():
    # --- JOYSTICKS (IJKL instead of WASD) ---
    # I=Up, K=Down, J=Left, L=Right
    lx = (1.0 if 'l' in active_keys else 0.0) - (1.0 if 'j' in active_keys else 0.0)
    ly = (1.0 if 'i' in active_keys else 0.0) - (1.0 if 'k' in active_keys else 0.0)
    g.left_joystick_float(x_value_float=lx, y_value_float=ly)
    
    # Map Arrow Keys to Right Joystick (Camera)
    rx = (1.0 if 'right' in active_keys else 0.0) - (1.0 if 'left' in active_keys else 0.0)
    ry = (1.0 if 'up' in active_keys else 0.0) - (1.0 if 'down' in active_keys else 0.0)
    g.right_joystick_float(x_value_float=rx, y_value_float=ry)

    # --- STICK CLICKS (L3/R3) ---
    # V = Left Stick Click (Run/Crouch) | B = Right Stick Click (Lock-on)
    if 'v' in active_keys: g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    else: g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)

    if 'b' in active_keys: g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
    else: g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)

    # --- SHOULDER BUTTONS (LB/RB) ---
    # Q = LB (Left Bumper) | E = RB (Right Bumper)
    if 'q' in active_keys:
        g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    else:
        g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)

    if 'e' in active_keys:
        g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    else:
        g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

    # --- ANALOG TRIGGERS ---
    # LT (Z) = Left Trigger, RT (C) = Right Trigger
    lt_val = 1.0 if 'z' in active_keys else 0.0
    rt_val = 1.0 if 'c' in active_keys else 0.0
    g.left_trigger_float(value_float=lt_val)
    g.right_trigger_float(value_float=rt_val)
    
    # --- Enter to (Start) Button ---
    if 'enter' in active_keys:
        g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    else:
        g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_START)

    # --- BACKSPACE = (Back) Button (Map/Scoreboard) ---
    if 'backspace' in active_keys:
        g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    else:
        g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

    # --- MAIN FACE BUTTONS ---
    # Space = (A) Button (Confirmation/Jumping)
    if 'space' in active_keys:
        g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    else:
        g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

    # U = (X) Button (Attack/Interact)
    if 'u' in active_keys:
        g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    else:
        g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

    # O = (B) Button (Dodge/Cancel)
    if 'o' in active_keys:
        g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    else:
        g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

    # P = (Y) Button (Special/Heavy)
    if 'p' in active_keys:
        g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    else:
        g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

    # --- D-PAD / HATS (Keys 1, 2, 3, 4) ---
    if '1' in active_keys: g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    else: g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    
    if '2' in active_keys: g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    else: g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    
    if '3' in active_keys: g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    else: g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    
    if '4' in active_keys: g.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    else: g.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    
    g.update()

def on_press(key):
    try:
        k = key.char if hasattr(key, 'char') else key.name
        active_keys.add(k)
        update_controller()
    except: pass

def on_release(key):
    try:
        k = key.char if hasattr(key, 'char') else key.name
        if k in active_keys: active_keys.remove(k)
        update_controller()
    except: pass

print("Active! You can now click on your game window and play.")
print("Press Ctrl+C in THIS console to disconnect safely.")

# We use a loop instead of .join() so Windows can 'hear' Ctrl+C
try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        while listener.running:
            time.sleep(0.1)  # Keeps the script alive and responsive to Ctrl+C
except KeyboardInterrupt:
    print("\nCtrl+C detected. Stopping...")
finally:
    print("Disconnecting virtual controller and resetting buttons...")
    g.reset()
    g.update()
    time.sleep(0.5)