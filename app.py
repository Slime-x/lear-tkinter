import tkinter as tk
from tkinter import ttk



window = tk.Tk()
window.geometry('500x400')
window.title('HIM')

frame = ttk.Frame(window)


label = ttk.Label(frame, text = 'Are you a good boy?', font = 'Arial 18 bold italic')
label.pack(padx=10, pady=5)

button = ttk.Button(frame, text='YES',command = lambda: { print('SIMPPPPP')})
button.pack(side = 'left')
button = ttk.Button(frame, text='NO',command = lambda: { print('Good SoldierE')})
button.pack(side = 'right')
frame.pack(pady=20)


frame2 = ttk.Frame(window)
Some_text = tk.StringVar()
Magic = ttk.Label(frame2, text='Label', textvariable=Some_text)
Magic.pack()

Entry = ttk.Entry(frame2, textvariable=Some_text)
Entry.pack()

frame2.pack()

window.mainloop()