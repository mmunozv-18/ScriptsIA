import remi.gui as gui
from remi import start, App

class Calculator(App):
    def __init__(self, *args):
        super(Calculator, self).__init__(*args)

    def main(self):
        main_container = gui.VBox(width=300, height=400)
        self.result = gui.TextInput(width=290, height=40)
        main_container.append(self.result)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"],
            ["", "", "=", ""]
        ]

        for row in buttons:
            hbox = gui.HBox(width=300)
            for button_text in row:
                if button_text == "":
                    continue
                button = gui.Button(button_text, width=70, height=70)
                button.onclick.do(self.on_click)
                hbox.append(button)
            main_container.append(hbox)

        return main_container

    def on_click(self, widget):
        text = widget.get_text()
        if text == "=":
            try:
                result = eval(self.result.get_value())
                self.result.set_value(str(result))
            except Exception:
                self.result.set_value("Error")
        elif text == "C":
            self.result.set_value("")
        else:
            self.result.set_value(self.result.get_value() + text)

start(Calculator)