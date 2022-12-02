from tkinter import *
from tkinter import messagebox
import random
# from random import shuffle
import string



def password_generator():
    num = ['0','1','2','3','4','5','6','7','8','9']
    symbol = ['!','@','#','$','%','^','&','*','(',')','_']

    randomLetter = [random.choice(string.ascii_letters)]
    randomNumber = [random.choice(num) for _ in range(random.randint(0,9))]
    randomSymbols = [random.choice(symbol) for _ in range(random.randint(0,9))]



    password_list =randomLetter + randomNumber + randomSymbols
    random.shuffle(password_list)
    password = "".join(password_list)
    import pyperclip
    password_entry.insert(0, password)
    pyperclip.copy(password)



def save_user_data():
    website = website_entry.get()
    email = website_entry.get()
    password =password_entry.get()

    if len(website) ==0 or len(password) ==0:
        messagebox.showinfo(title = "Now allowed", message="Enter value more than 0")
        value_of_message_box = False

    else:
        value_of_message_box = messagebox.askokcancel(title=website, message=f'Please check the entered details\n '
                                                      f'Email: {email}\n'
                                                      f'Password: {password}')

    if value_of_message_box:
        with open('data.txt', "a") as data_file:
            data_file.write(f'{website}//{email}//{password}\n')
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)





window = Tk()
window.title('Password Manager')
window.config(padx=28, pady=20)
canvas = Canvas(height=200, width=200)
canvas.create_image((100, 100))

#Creating Labels for the window
website_label = Label(text='Enter Your Website')
website_label.grid(row=1, column=0)

email_label = Label(text='Enter Your Email')
email_label.grid(row=2, column=0)

password_label = Label(text='Enter Your Password')
password_label.grid(row=3, column=0)

#data entries for user
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)



#Buttons for the page
button_password = Button(text='Generate Password', command=password_generator)
button_password.grid(row=3, column=2)
button_add = Button(text='Add', command=save_user_data)
button_add.grid(row=4, column=1)





window.mainloop()