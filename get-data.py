import tkinter as tk
from tkinter import ttk


def button_func():
    # get the entry widget's contents
    text = entry.get()

    # update the label widget's contents
    label.config(text=text)
    # or
    label['text'] = text
    entry['state'] = 'disabled'


def reset():
    entry['state'] = 'enabled'
    label['text'] = "A label"


# window
window = tk.Tk()
window.title("Getting and setting widgets")

# widgets
label = ttk.Label(window, text="A label")
entry = ttk.Entry(window)
button = ttk.Button(window, text="Get entry", command=button_func)
button2 = ttk.Button(window, text="Set entry", command=reset)

label.pack()
entry.pack()
button.pack()
button2.pack()

# run
window.mainloop()
