from directkeys import ReleaseKeyPynput, PressKeyPynput, W, A, S, D, Enter
import time
from pynput.mouse import Button, Controller
import pyautogui
mouse = Controller()

print("Welcome to Craz3's Auto-Bet program!")
print("Type in '999' to run program forever")

length = int(input("# to run program: "))

print('Starting Script in 5 seconds')
for i in range(0, 5):
    print(5-i)
    time.sleep(1)


def autoBet():
    print('Starting game')
    mouse.position = (1450, 900)
    time.sleep(0.1)
    PressKeyPynput(Enter)
    time.sleep(0.1)
    ReleaseKeyPynput(Enter)

    time.sleep(1)

    print('Selecting horse')
    mouse.position = (350, 350)
    time.sleep(0.1)
    PressKeyPynput(Enter)
    time.sleep(0.1)
    ReleaseKeyPynput(Enter)
    time.sleep(1)

    print('Creating bet')
    mouse.position = (1525, 520)
    time.sleep(0.1)
    PressKeyPynput(Enter)
    time.sleep(0.1)

    print('Starting race')
    mouse.position = (1300, 800)
    print("make this console active window and hit ctrl+c to stop program here")
    for x in range(0, 37):
        b = "Loading" + "." * x
        print(b, end="\r")
        time.sleep(1)
    ReleaseKeyPynput(Enter)


    print('Resetting')
    mouse.position = (950, 1000)
    time.sleep(0.1)
    PressKeyPynput(Enter)
    time.sleep(0.1)
    ReleaseKeyPynput(Enter)

if length != 999:
    for x in range(0, length):
        autoBet()

if length == 999:
    print('Running forever')
    while True:
        autoBet()

print('done')
