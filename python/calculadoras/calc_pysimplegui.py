import PySimpleGUI as sg

layout = [
    [sg.Input(size=(20, 1), key="-INPUT-", justification='right')],
    [sg.Button("7"), sg.Button("8"), sg.Button("9"), sg.Button("/")],
    [sg.Button("4"), sg.Button("5"), sg.Button("6"), sg.Button("*")],
    [sg.Button("1"), sg.Button("2"), sg.Button("3"), sg.Button("-")],
    [sg.Button("0"), sg.Button("."), sg.Button("C"), sg.Button("+")],
    [sg.Button("=")]
]

window = sg.Window("Calculadora PySimpleGUI", layout)

expression = ""

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event in "0123456789./*-+":
        expression += event
        window["-INPUT-"].update(expression)
    elif event == "=":
        try:
            result = eval(expression)
            window["-INPUT-"].update(result)
            expression = str(result)
        except Exception:
            window["-INPUT-"].update("Error")
            expression = ""
    elif event == "C":
        expression = ""
        window["-INPUT-"].update("")

window.close()