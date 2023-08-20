'''Please order your coffee with or without 👇'''

from tkinter import *

def coffee():
    if sugar_check_value.get():
        sugar_value = 'with sugar'
    else:
        sugar_value = 'without sugar'

    if ice_check_value.get():
        ice_value = 'with ice'
    else:
        ice_value = 'without ice'

    if milk_check_value.get():
        milk_value = 'with milk'
    else:
        milk_value = 'without milk'

# ----------------------------------.config() is used to edit Label() created inside the application-----------------
    preference.config(text = f' Please confirm your order:\n{sugar_value} \n{ice_value} \n{milk_value} ')

def order():
    order_label.config(text ='Sorry! we are on vacation🤪. Visit us next time. Thankyou !!')


# ----------------------------------application-----------------------------------------
root = Tk()
root.geometry("430x310")

# ---------------------------------Label for text------------------------------------
question = Label(root, text='How would you like your coffee?',
                 fg = 'brown',
                 bg = 'cyan',
                 font = ('Arial', 15))

# ---------------------------boolean flags assignment-----------------------------------
sugar_check_value = BooleanVar()
ice_check_value = BooleanVar()
milk_check_value = BooleanVar()

# ------------------------------creating checkboxes--------------------------------------
sugar_checkbox = Checkbutton(root, text = 'Sugar', variable = sugar_check_value, command = coffee)
ice_checkbox = Checkbutton(root, text = 'Ice', variable = ice_check_value, command = coffee)
milk_checkbox = Checkbutton(root, text = 'Milk', variable = milk_check_value, command = coffee)
preference = Label(root)        # new label inorder to display contents

button = Button(root, text = 'place an order', command = order)
order_label = Label(root)

# ----------------------------packing contents inside root window---------------------------------
question.pack()
sugar_checkbox.pack()
ice_checkbox.pack()
milk_checkbox.pack()
preference.pack()
button.pack()
order_label.pack()

# -------------------------infinite loop so that window is visible until closed manually-------------------------------
root.mainloop()
