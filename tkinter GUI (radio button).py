from tkinter import *

def vehicle_type():
    choice.config(text = f'Your choice is {set_value.get()}')

root = Tk()
root.geometry("300x300")

set_value = StringVar(value = 'Petrol')

# ------------------------whenever selected option, default variable value is set to radiobutton value------------------
radio1 = Radiobutton(root, text = 'Petrol', variable = set_value, value = 'Petrol', command = vehicle_type)
radio2 = Radiobutton(root, text = 'Diesel', variable = set_value, value = 'Diesel', command = vehicle_type)
radio3 = Radiobutton(root, text = 'Electric', variable = set_value, value = 'Electric', command = vehicle_type)
radio1.pack()
radio2.pack()
radio3.pack()
#---------------------------------------------to add a message below----------------------------------------------------
choice = Label(root)
choice.pack()

root.mainloop()
