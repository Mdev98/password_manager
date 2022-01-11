from json.decoder import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = 5 
nr_symbols = 5
nr_numbers = 5

def passGen():

    password_list = []

    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_entry.delete(0,END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    username_mail = email_username_entry.get()
    password = password_entry.get()

    user_data = {
        website:{
            "email": username_mail,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="OOPS",message="Please don't leave any fields empty")
    else:
        alert = messagebox.askokcancel(title=website,message=f"These are the details entered :\n\nEmail: {username_mail}\n\npassword:{password}\n\nAre you ok with these ?")

        if alert:
            try:
                with open("data.json",mode="r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open("data.json",mode="w") as f:
                    json.dump(user_data,f,indent=4)
            else:
                data.update(user_data)
                with open("data.json",mode="w") as f:
                    #saving data
                    json.dump(data,f,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json",mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("BOX_INFO","No Data file found")
    else:
        for key in data:
            if website_entry.get() == key:
                messagebox.showinfo("Box_info", f"WEBSITE : {key}\nPASSWORD : {data[key]['password']}")
            else:
                messagebox.showinfo("BOX_INFO","No details for the website exists")
                break
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg="#fff")
window.geometry("1200x720")
window.minsize(400,300)

frame = Frame(window,bg="#fff")

canvas = Canvas(frame, width=200, height= 200,bg="#fff",highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website_label = Label(frame,text="Website:",bg="#fff")
website_label.grid(row=1,column=0,pady=5)
website_entry = Entry(frame,width=35)
website_entry.grid(row=1,column=1,pady=5)

email_username_label = Label(frame,text="Email/Username:",bg="#fff")
email_username_label.grid(row=2,column=0,pady=5)
email_username_entry = Entry(frame,width=45)
email_username_entry.insert(0, "mamour.diop22@gmail.com")
email_username_entry.grid(row=2,column=1,columnspan=2,pady=5)

password_label = Label(frame,text="Password",bg="#fff")
password_label.grid(row=3,column=0,pady=5)
password_entry = Entry(frame,width=35)
password_entry.grid(row=3,column=1,pady=5)

generate_btn = Button(frame,text="generate",bg="#fff",command=passGen)
generate_btn.grid(row=3,column=2)

add_btn = Button(frame,text="Add",command=save_info,width=30,bg="#fff")
add_btn.grid(row=4,column=1)

search_btn = Button(frame,text="Search",command = find_password,bg="#fff")
search_btn.grid(row=1,column = 2)

frame.pack(expand=YES)
window.mainloop()