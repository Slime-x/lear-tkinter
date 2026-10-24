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
_2frame = ttk.Frame(frame2) 


_2text = ttk.Label(_2frame, text='Your Name:', font='Calibri 16 bold')
_2text.pack(side='left', pady=10)
Entry = ttk.Entry(_2frame, textvariable=Some_text)
Entry.pack(side='right')


_2frame.pack()

_3frame = ttk.Frame(frame2)
Magic = ttk.Label(_3frame, text='Label', textvariable=Some_text)
Magic.grid(row=1,column=0)



frame2.pack()

window.mainloop()