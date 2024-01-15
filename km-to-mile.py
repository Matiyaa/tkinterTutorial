import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    km = entry_int.get()
    miles = km * 0.621371
    output_string.set(f"Miles: {miles: .2f}")


# window
window = ttk.Window(themename="darkly")
window.title("Converter")
# width x height
window.geometry("500x150")

# title
title_label = ttk.Label(
    master= window,
    text="Kilometers to Miles",
    font="Calibri, 24")
title_label.pack()

# input
input_frame = ttk.Frame(master=window)
input_label = ttk.Label(master=window, text="Enter kilometers: ")
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, width=50, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
input_label.pack()
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text="Miles: ",
    font='Calibri, 18',
    textvariable=output_string)
output_label.pack(pady=5)

# run
window.mainloop()
