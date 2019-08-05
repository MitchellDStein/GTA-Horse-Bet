from directkeys import ReleaseKeyPynput, PressKeyPynput, W, A, S, D, Enter
import time
from pynput.mouse import Button, Controller
import pyautogui
from TkinterTest import changeOutput

mouse = Controller()

def Run(number, res1, res2):
    if number != 999:
        for x in range(0, number):
            autoBet(res1, res2)

    if number == 999:
        print('Running forever')
        while True:
            autoBet(res1, res2)

def autoBet(res1, res2):
    output="Starting game"
    changeOutput(output)

    mouse.position = (res1*0.755, res2*0.833)
    time.sleep(0.1)
    PressKeyPynput(Enter)
    time.sleep(0.1)
    ReleaseKeyPynput(Enter)

    time.sleep(1)

    print('Selecting horse')
    mouse.position = (res1*0.182, res2*0.324)
    time.sleep(0.1)
    PressKeyPynput(Enter)
    time.sleep(0.1)
    ReleaseKeyPynput(Enter)
    time.sleep(1)

    print('Creating bet')
    mouse.position = (res1*0.794, res2*0.481)
    time.sleep(0.1)
    PressKeyPynput(Enter)
    time.sleep(0.1)

    print('Starting race')
    mouse.position = (res1*0.677, res2*0.741)
    print("make this console active window and hit ctrl+c to stop program here")
    for x in range(0, 37):
        b = "Loading" + "." * x
        print(b, end="\r")
        time.sleep(1)
    ReleaseKeyPynput(Enter)


    print('Resetting')
    mouse.position = (res1*0.495, res2*0.926)
    time.sleep(0.1)
    PressKeyPynput(Enter)
    time.sleep(0.1)
    ReleaseKeyPynput(Enter)
