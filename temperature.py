import tkinter as tk
from tkinter import ttk
window = tk.Tk()
fahrenheit_var = tk.StringVar()

lbl_result = tk.Label(
    master=window,
    text='Enter your number',
)


def convert_fahrenheit_to_celsius(*args):
    fahrenheit_input = fahrenheit_var.get()
    try:
        fahrenheit_val = float(fahrenheit_input)
        lbl_result['text'] = (fahrenheit_val - 32) * 5 / 9
    except ValueError:
        if fahrenheit_input != '':
            lbl_result['text'] = 'You should enter a number'
        else:
            lbl_result['text'] = 'Your input is empty'


window.bind('<Return>', convert_fahrenheit_to_celsius)
lbl_fahrenheit = tk.Label(
    master=window,
    text='Fahrenheit : ',
)
ent_fahrenheit = tk.Entry(
    master=window,
    width=50,
    textvariable=fahrenheit_var,
)

btn_calc = ttk.Button(
    master=window,
    text='calculate',
    command=convert_fahrenheit_to_celsius,
)

lbl_fahrenheit.grid(row=0, column=0, padx=10, pady=10)
ent_fahrenheit.grid(row=0, column=1)
btn_calc.grid(row=0, column=2, padx=10, pady=10)

lbl_celsius = tk.Label(
    master=window,
    text='Celsius : '
)

lbl_celsius.grid(row=1, column=0, pady=(10, 20))
lbl_result.grid(row=1, column=1, pady=(10, 20))

window.title('temperature converter')
window.mainloop()
