from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorGrid(GridLayout):
    def __init__(self, **kwargs):
        super(CalculatorGrid, self).__init__(**kwargs)
        self.cols = 4
        self.result = TextInput(font_size=32, readonly=True, halign="right")
        self.add_widget(self.result)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            "="
        ]

        for button_text in buttons:
            button = Button(text=button_text, font_size=24)
            button.bind(on_press=self.on_button_press)
            self.add_widget(button)

    def on_button_press(self, instance):
        text = instance.text
        if text == "=":
            try:
                result = str(eval(self.result.text))
                self.result.text = result
            except Exception:
                self.result.text = "Error"
        elif text == "C":
            self.result.text = ""
        else:
            self.result.text += text

class CalculatorApp(App):
    def build(self):
        return CalculatorGrid()

if __name__ == "__main__":
    CalculatorApp().run()