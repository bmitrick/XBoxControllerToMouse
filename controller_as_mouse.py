'''import xbox_controller, pyautogui, time

controller = xbox_controller.XboxController()

running = True

while running:
    #Pull inputs
    controllerState = controller.read()

    LEFT_STICK_Y = controllerState[0]
    LEFT_STICK_X = controllerState[1]
    RIGHT_STICK_Y = controllerState[2]
    RIGHT_STICK_X = controllerState[3]
    LEFT_TRIGGER = controllerState[4]
    RIGHT_TRIGGER = controllerState[5]
    LEFT_BUMPER = controllerState[6]
    RIGHT_BUMPER = controllerState[7]
    A_BTN = controllerState[8]
    X_BTN = controllerState[9]
    Y_BTN = controllerState[10]
    B_BTN = controllerState[11]
    LEFT_THUMB = controllerState[12]
    RIGHT_THUMB = controllerState[13]
    BACK_BTN = controllerState[14]
    START_BTN = controllerState[15]
    LEFT_D_PAD = controllerState[16]
    RIGHT_D_PAD = controllerState[17]
    UP_D_PAD = controllerState[18]
    DOWN_D_PAD = controllerState[19]

    #A button = left click
    if A_BTN == 1:
        pyautogui.click(button='left')

    #B button = right click
    if B_BTN == 1:
        pyautogui.click(button='right')

    #Left stick controlls mouse
    if LEFT_STICK_Y >= 0.05:
        pyautogui.move(0, -5)
    if LEFT_STICK_Y <= -0.05:
        pyautogui.move(0, 5)
    if LEFT_STICK_X >= 0.05:
        pyautogui.move(5, 0)
    if LEFT_STICK_X <= -0.05:
        pyautogui.move(-5,0)

    print(controllerState)'''

import xbox_controller, mouse, time

controller = xbox_controller.XboxController()

def runController
    #Pull inputs
    controllerState = controller.read()

    LEFT_STICK_Y = controllerState[0]
    LEFT_STICK_X = controllerState[1]
    RIGHT_STICK_Y = controllerState[2]
    RIGHT_STICK_X = controllerState[3]
    LEFT_TRIGGER = controllerState[4]
    RIGHT_TRIGGER = controllerState[5]
    LEFT_BUMPER = controllerState[6]
    RIGHT_BUMPER = controllerState[7]
    A_BTN = controllerState[8]
    X_BTN = controllerState[9]
    Y_BTN = controllerState[10]
    B_BTN = controllerState[11]
    LEFT_THUMB = controllerState[12]
    RIGHT_THUMB = controllerState[13]
    BACK_BTN = controllerState[14]
    START_BTN = controllerState[15]
    LEFT_D_PAD = controllerState[16]
    RIGHT_D_PAD = controllerState[17]
    UP_D_PAD = controllerState[18]
    DOWN_D_PAD = controllerState[19]

    #A button = left click
    if A_BTN == 1:
        mouse.click('left')

    #B button = right click
    if B_BTN == 1:
        mouse.click('right')

    #Left stick controlls mouse
    if LEFT_STICK_Y >= 0.05:
        mouse.move(0, -1, absolute=False, duration = 0)
    if LEFT_STICK_Y <= -0.05:
        mouse.move(0, 1, absolute=False, duration = 0)
    if LEFT_STICK_X >= 0.05:
        mouse.move(1, 0, absolute=False, duration = 0)
    if LEFT_STICK_X <= -0.05:
        mouse.move(-1,0, absolute=False, duration = 0)

    #time.sleep(0)
    print(controllerState)
