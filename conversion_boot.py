import tkinter as tk
import ttkbootstrap as ttk
#from tkinter import ttk

def convert():
    miles = entry_int.get()
    km = miles * 1.61
    output_string.set(km)

#window
window=ttk.Window(themename='journal')
window.title('Scale')
window.geometry('300x150')

#title
title_label = ttk.Label(master=window,
                        text='Miles to kilometer',
                        font='Calibri 24 bold')
title_label.pack()

#input
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame,
                  textvariable=entry_int)
button = ttk.Button(master=input_frame,
                    text='Convert',
                    command=convert)
entry.pack(side='left',padx=10)
button.pack(side='left')
input_frame.pack(pady=5)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                         text='Output',
                         font='Calibri 24',
                         textvariable=output_string)
output_label.pack()

window.mainloop()