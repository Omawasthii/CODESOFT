import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        expression = display.get()
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button_text in buttons:
    tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 16), command=lambda t=button_text: button_click(t) if t != '=' else calculate()).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

clear_button = tk.Button(root, text='C', width=5, height=2, font=("Arial", 16), command=clear)
clear_button.grid(row=row, column=col, padx=5, pady=5)

root.configure(bg="lightblue")
root.mainloop()
