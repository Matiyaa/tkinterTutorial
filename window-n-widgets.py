import tkinter as tk
from tkinter import ttk


def button_click():
    print("Button clicked!")
    label["text"] = "Button clicked!"


def hello():
    print("Hello!")
    label2["text"] = "Hello!"


# create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

# ttk.Label
label = ttk.Label(master=window, text="This is a test!")
label.pack()

# tk.Text
text = tk.Text(master=window)
text.pack()

# ttk.Entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk.Label 2
label2 = ttk.Label(master=window, text="My label")
label2.pack()

# ttk.Button
button = ttk.Button(master=window, text="Click me!", command=button_click)
button.pack()

# ttk.Button 2
button2 = ttk.Button(master=window, text="Click me!", command=hello)
button2.pack()

# run the window
window.mainloop()
