import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry.get() + text)

root = tk.Tk()
root.title("Calculadora Tkinter")
root.geometry("400x500")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="lucida 20 bold")
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["", "", "=", ""]
]

for row in buttons:
    frame = tk.Frame(root)
    for button_text in row:
        if button_text == "":
            continue
        button = tk.Button(frame, text=button_text, font="lucida 15 bold", padx=20, pady=20)
        button.pack(side=tk.LEFT, padx=10, pady=10)
        button.bind("<Button-1>", click)
    frame.pack()

root.mainloop()