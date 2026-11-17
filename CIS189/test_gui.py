"""
* Name         : M9 T3: Basic GUI Assignment
* Author       : Noah Goche
* Created      : 7/16/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Program creates a gui to select a meal option that displays a message
reflecting what you choose.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

import tkinter

def pick_first_breakfast():
    label.config(text="First Breakfast")

def pick_second_breakfast():
    label.config(text="Second Breakfast")

def pick_lunch():
    label.config(text="Lunch!")

def pick_dinner():
    label.config(text="Dinner!")

m = tkinter.Tk() # where m is the name of the main window object
m.title("Favorite Meal")

label = tkinter.Label(m, text="Waiting")
label.grid(row=5)

var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_first_breakfast).grid(row=1)

var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_second_breakfast).grid(row=2)

var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text = "Lunch", variable=var3, command=pick_lunch).grid(row=3)

var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text = "Dinner", variable=var4, command=pick_dinner).grid(row=4)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)

m.mainloop()  # infinite loop that waits for events to happen