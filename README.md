# VX360-Gamepad
A virtual Xbox 360 gamepad mounting python script file that is ready to use and easy to edit and adapt.

These use the Microsoft XInput standards so it will work in any game that supports an Xbox 360 controller.

You have:
Movement: IJKL (Left Stick)
Camera: Arrows (Right Stick)
Actions: Space (A), O (B), U (X), P (Y)
Combat: Q/E (LB/RB), Z/C (LT/RT)
Movement+: V/B (L3/R3 Stick Clicks)
Shortcuts: 1-4 (D-Pad)
System: Enter/Backspace (Start/Back)

Requirements:
Driver Requirement: You must have the ViGEmBus driver installed on your Windows machine for the connection to happen.
Library requirement: Pygame (You can install that library by using: python pip install pygame)

Pygame requires small window to be the active (focused) window to capture your keyboard presses. 
The Problem: When you click on your game, the Pygame window loses focus and stops sending the controller signals.
The Fix: You must run the game in Windowed or Borderless Windowed mode so you can keep the Pygame window "on top" or use a library that captures "Global" inputs like pynput. This allows you to click into your game and play while the script runs in the background—you won't need to keep the Pygame window focused anymore.
You can install that library by using: python pip install pynput

As soon as you start the VX360Gamepad.py via powershell, the virtual controller is connected to your system via the ViGEmBus driver. It will appear to your computer and games exactly like a real physical Xbox 360 controller. 
To ensure it stays connected so you can use it, keep these points in mind:
Script Lifetime: The controller remains connected only as long as your Python script is running. If the script finishes or you close the terminal, the virtual device will "unplug". 
(You can also now Ctrl+C to safely disconnect it at CMD window)

Verification: You can verify it is connected by typing joy.cpl into your Windows Run box (Win + R). You should see an Xbox 360 Controller listed there while your script is active.
Game Detection: Most games will pick up the virtual controller automatically, but some may require you to select "Controller" in their internal settings menus.
