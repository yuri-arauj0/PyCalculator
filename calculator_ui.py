from tkinter import font
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Column

sg.theme('BrightColors')

WIN_W = 50
WIN_H = 5

def _button(label: str):
    return sg.Button(label, key="button_%s" %label, size=(7,3), font=("Consolas", 10))

def _col(*components):
    return sg.Column([[component] for component in components])

layout = [
    # ============ 1 row ============
    #until 50 char per line, with 5 lines
    [sg.Text('', font=('Consolas', 10), size=(WIN_W, WIN_H))], 

    # ============ 2 row ============
    [ 
    _col(_button("7"), _button("4"), _button("1"), _button("+/-")), # 1 col
    _col(_button("8"), _button("5"), _button("2"), _button("0")),   # 2 col
    _col(_button("9"), _button("6"), _button("3"), _button(",")),   # 3 col
    _col(_button("+"), _button("-"), _button("x"), _button("/")),   # 4 col
    sg.Button("=", key="equal", size=(7,15), font=("Consolas", 10)) # 5 col
    ],
]

window = sg.Window('Calculadora do Yu', layout=layout, resizable=True, finalize=True, margins=(0, 0), grab_anywhere=False)

while True:
    event, values = window.read()

    if event in('Exit', None):
        break
