import datetime
import pynput
import PySimpleGUI as sg
from pynput.keyboard import Key


def kb_press():
    kb = pynput.keyboard.Controller()
    kb.press(Key.f15)
    kb.release(Key.f15)


sg.theme('Dark Blue 3')

layout = [
    [sg.Text('Sends an f15 key press once every minute.')],
    [sg.Text('Program running:'), sg.Text('No ', key='status')],
    [sg.Button('Start'), sg.Button('Stop'), sg.Button('Exit')]
]

window = sg.Window('Keyboard Presser', layout)

next_press = datetime.datetime.now() + datetime.timedelta(minutes=1)
running = False
while True:
    event, values = window.read(timeout=3)

    if event in (None, 'Exit'):
        running = False
        break
    elif event == 'Start':
        running = True
        window['status'].Update('Yes')
    elif event == 'Stop':
        running = False
        window['status'].Update('No')

    if running and datetime.datetime.now() > next_press:
        next_press = datetime.datetime.now() + datetime.timedelta(minutes=1)
        kb_press()

window.close()
