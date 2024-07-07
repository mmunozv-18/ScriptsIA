from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora PyQt")
        self.setGeometry(100, 100, 300, 400)
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout()
        self.result = QLineEdit()
        layout.addWidget(self.result)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"],
            ["", "", "=", ""]
        ]
        
        grid = QGridLayout()
        for row, row_values in enumerate(buttons):
            for col, button_text in enumerate(row_values):
                if not button_text:
                    continue
                button = QPushButton(button_text)
                button.clicked.connect(self.on_click)
                grid.addWidget(button, row, col)
        
        layout.addLayout(grid)
        self.setLayout(layout)

    def on_click(self):
        button = self.sender()
        text = button.text()
        if text == "=":
            try:
                result = eval(self.result.text())
                self.result.setText(str(result))
            except Exception:
                self.result.setText("Error")
        elif text == "C":
            self.result.clear()
        else:
            self.result.setText(self.result.text() + text)

if __name__ == "__main__":
    app = QApplication([])
    window = Calculator()
    window.show()
    app.exec_()