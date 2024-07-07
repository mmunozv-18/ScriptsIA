import wx

class Calculator(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Calculadora wxPython", size=(300, 400))
        panel = wx.Panel(self)

        self.result = wx.TextCtrl(panel, style=wx.TE_RIGHT)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"],
            ["", "", "=", ""]
        ]

        grid = wx.GridSizer(5, 4, 10, 10)
        for row in buttons:
            for button_text in row:
                if button_text == "":
                    continue
                button = wx.Button(panel, label=button_text)
                button.Bind(wx.EVT_BUTTON, self.on_click)
                grid.Add(button, 0, wx.EXPAND)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.result, 0, wx.EXPAND | wx.ALL, 10)
        vbox.Add(grid, 1, wx.EXPAND | wx.ALL, 10)
        panel.SetSizer(vbox)

              
    def on_click(self, event):
            button = event.GetEventObject()
            text = button.GetLabel()
            if text == "=":
                try:
                    result = eval(self.result.GetValue())
                    self.result.SetValue(str(result))
                except Exception:
                    self.result.SetValue("Error")
            elif text == "C":
                self.result.Clear()
            else:
                self.result.SetValue(self.result.GetValue() + text)

if __name__ == "__main__":
    app = wx.App(False)
    frame = Calculator()
    frame.Show()
    app.MainLoop()                 