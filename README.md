Use your gamepad/controller to control your mouse for laptop/PC.
Only available for Linux platforms now. All development has been carried on Ubuntu 14.04.

Major libraries used:
inputs 0.1
pyautogui
micropython-fcntl

Note - I have modified the inputs library to make the get_gamepad() method work in a non-blocking fashion(that's why fcntl library is used).
Modifications - get_gamepad() returns None if there is no gamepad event, instead of waiting for an event to occur.
