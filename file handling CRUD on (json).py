'''
creating a more advanced json file program
'''

import json
import os

def add_data():
    user_details = []
    while True:
        name = input('Enter your name (type "quit" to exit) : ')
        if name == 'quit':
            break

        email = input('Enter your mail id : ')
        contact = input('Enter your phone number : ')

        details = {'name' : name, 'email' : email, 'contact' : contact}

        user_details.append(details)

    if os.path.exists('user_database.json'):            # Checking if the file already exists
        with open('user_database.json', 'r') as file:
            existing_data = json.load(file)
        user_details.extend(existing_data)      # Prevents over-writing existing data

    with open('user_database.json', 'w') as file:
        json.dump(user_details, file)       # dumps all the data present in user_details[] into the specified json file.
    print("User data added successfully")

'''
Possible error is that if you have an existing file named 'user_database.json' with no data in it, json.load() throws an error.
You can solve it if you want.
'''


def read_data():

    if not os.path.exists('user_database.json'):
        print('No data found')

    with open('user_database.json', 'r') as file:
        data_to_dict = json.load(file)
        for user in data_to_dict:
            name = user['name']
            email = user['email']
            contact = user['contact']

            contents = f"name: {name}   email: {email}   contact: {contact}"
            print(contents)
        print("Here are all the userdata")


def update_data(name):      # name parameter takes argument. Remember this..
    user_found = False      # Setting flag

    if not os.path.exists('user_database.json'):
        print("No file found to look for data")


    with open('user_database.json', 'r') as file:
        user_data = json.load(file)

        for user in user_data:
            if name.lower() == user['name'].lower():   # Converting both to lowercase to prevent case mismatch error while user gives input

                updated_email = input(f"Enter new email for {name} : ")
                updated_contact = input(f"Enter new contact for {name} : ")

                user['email'] = updated_email
                user['contact'] = updated_contact

                user_found = True       # Changing flag value

        if user_found == False:
                print("User not found")

    with open('user_database.json', 'w') as file:
        json.dump(user_data, file)
    print("User data updated successfully")



def delete_data(name):      # name parameter takes argument. Remember this..
    user_found = False      # Setting flag

    if not os.path.exists('user_database.json'):
        print("No file found to look for data")


    with open('user_database.json', 'r') as file:
        user_data = json.load(file)

        for user in user_data:
            if name.lower() == user['name'].lower():   # Converting both to lowercase to prevent case mismatch error while user gives input
                user_data.remove(user)
                user_found = True       # Changing flag value

        if user_found == False:
                print("User not found")

    with open('user_database.json', 'w') as file:
        json.dump(user_data, file)
    print("User data deleted successfully")


print("Hello user, I am capable of performing CRUD on your data.\n Please -- \n Enter '1' to read data\n Enter '2' to add data\n Enter '3' to update data\n Enter '4' to delete data")
user_choice = input("Please enter your choice : ")
if user_choice == '1':
    read_data()
elif user_choice == '2':
    add_data()
elif user_choice == '3':
    name = input("Enter the name of the user you would like to edit the data for : ")
    update_data(name)
elif user_choice == '4':
    name = input("Enter the name of the user you would like to delete the data : ")
    delete_data(name)
else:
    print("I guess you donot want to perform any of the operations. However, this is all I am capable of as for now.")