from inputs import get_gamepad
import pyautogui as mouse
mouse.FAILSAFE = True

screenWidth, screenHeight = mouse.size()
mouse.moveTo(screenWidth/2, screenHeight/2, 1)


def getevent():
    events = get_gamepad()
    if events is None:
        return None
    return events[0]

registeredEvent = None
while 1:
    event = getevent()
    if event is not None and event.code[:3] != "SYN":
        registeredEvent = event
        print event.code[:3], event.state

    if registeredEvent is not None:
        if registeredEvent.code == "ABS_HAT0Y":
            if registeredEvent.state == -1:
                mouse.moveRel(0, -10)
            if registeredEvent.state == 1:
                mouse.moveRel(0, 10)

        if registeredEvent.code == "ABS_HAT0X":
            if registeredEvent.state == -1:
                mouse.moveRel(-10, 0)
            if registeredEvent.state == 1:
                mouse.moveRel(10, 0)
