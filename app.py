import tkinter as tk
from tkinter import ttk


# ---------------------------- Window thingie ----------------------------
window = tk.Tk()
window.geometry('500x400')
window.title('HIM')




# ---------------------------- Frame ----------------------------
frame = ttk.Frame(window)


label = ttk.Label(frame, text = 'Are you a good boy?', font = 'Arial 18 bold italic')
label.pack(padx=10, pady=5)

# Side ways button. Using pack()
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
Magic.pack()


_3frame.pack()
frame2.pack()



# ---------------------------- BUTTONS ----------------------------


Btn_frame = ttk.Frame(window)

# Button can have variables too. 
button_string = tk.StringVar(value ='Print above data')
_2button = ttk.Button(Btn_frame, text='this gets overwritten', command=lambda: print(Some_text.get()), textvariable=button_string)
_2button.pack(pady=5)


def button(name):
    print(name, Some_text.get())
# If i want to send arguments in the fuction while using a button ot anyything
x = 'SLIME'
_3button = ttk.Button(Btn_frame, text='Nickname + Name', command=lambda: button(x))
_3button.pack()


# ------- Tick / Check button -------

check_var = tk.StringVar()                     # Need this to know whether the button is checked or not | use Boolean mostly here. Using str just cause
check = ttk.Checkbutton(
    Btn_frame,
    text='Alcohal', 
    command=lambda:print(check_var.get()),  #lambda is very imp. Learn abt it is I haven't
    variable = check_var,                   # Not named textvar cause it doesn't change the text. It is just a variable
    onvalue= 'You can drink my guy',                           # The value given to {variable} when button is on
    offvalue= 'Are you a girl? Hit me up...',                         # The value given to {variable} when button is off


    )
check.pack()
 
# Another example
check_var2 = tk.IntVar(value='10') # Default is on.                   
check2 = ttk.Checkbutton(
    Btn_frame, 
    text='Lays and Coke', 
    command=lambda:print(check_var2.get()),
    variable = check_var2,                 
    onvalue= 10,                         
    offvalue= -10,   
    )                       
check2.pack()


# -------- RADIO BUTTON ----------

_var_radio = tk.StringVar()
radio1 = ttk.Radiobutton(
    Btn_frame, 
    text='Furry', 
    value = 'meow',                         # Must have a unique value, else it will tweak out
    variable=_var_radio,
    command=lambda: print(_var_radio.get())
    )
radio2 = ttk.Radiobutton(
    Btn_frame, 
    text='Diddy', 
    value = 2,
    variable=_var_radio,
    command=lambda: print(_var_radio.get())
    )
radio1.pack()
radio2.pack()

Btn_frame.pack()


window.mainloop()