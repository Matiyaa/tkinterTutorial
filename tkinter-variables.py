import tkinter as tk
from tkinter import ttk


# window
window = tk.Tk()
window.title("Tkinter Variables")

# tkinter variable
string_var = tk.StringVar()

# widgets
label = ttk.Label(window, text="A label", textvariable=string_var)
entry = ttk.Entry(window, textvariable=string_var)

label.pack()
entry.pack()

# run
window.mainloop()