from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorGrid(BoxLayout):
    def __init__(self, **kwargs):
        super(CalculatorGrid, self).__init__(orientation='vertical', **kwargs)
        
        # Crear el campo de texto para mostrar el resultado
        self.result = TextInput(font_size=32, readonly=True, halign="right", size_hint=(1, 0.2))
        self.add_widget(self.result)
        
        # Crear un GridLayout para los botones
        buttons_layout = GridLayout(cols=4, size_hint=(1, 0.8))
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            '='
        ]
        
        for button_text in buttons:
            button = Button(text=button_text, font_size=24)
            button.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(button)
        
        self.add_widget(buttons_layout)

    def on_button_press(self, instance):
        text = instance.text
        if text == '=':
            try:
                result = str(eval(self.result.text))
                self.result.text = result
            except Exception:
                self.result.text = "Error"
        elif text == 'C':
            self.result.text = ""
        else:
            self.result.text += text

class CalculatorApp(App):
    def build(self):
        return CalculatorGrid()

if __name__ == "__main__":
    CalculatorApp().run()