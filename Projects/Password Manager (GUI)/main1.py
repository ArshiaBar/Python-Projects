from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def add():
    if len(website_entry.get()) or len(pass_entry.get()) !=0:
        ok=messagebox.askokcancel("be aware",f"your info:\n{website_entry.get()}\n{email_entry.get()}\n{pass_entry.get()}\n"
                                          f" Wanna continue?")
        if ok:
            data={website_entry.get():{"email":email_entry.get(),"password":pass_entry.get()}}
            #with open("inventory.txt","a") as f:
                #f.write(f"{website_entry.get()} | {email_entry.get()} | {pass_entry.get()}\n")
            try:
                with open("inventory.json","r") as f:
                    diction = json.load(f)
                    diction.update(data)
                    with open("inventory.json", "w") as fi:
                        json.dump(diction, fi, indent=4)
            except (FileNotFoundError,json.JSONDecodeError):#from json import JSONDecodeError/except json.JSONDecodeError
                with open("inventory.json","w") as f:
                    json.dump(data,f,indent=4)

            messagebox.showinfo("Hey","you did it!")
            website_entry.delete(0,END)
            pass_entry.delete(0,END)
    else:
        messagebox.showinfo("Hey","Don't leave stuff empty")

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    lets=[random.choice(letters) for _ in range(random.randint(5,6))]
    nums=[random.choice(numbers) for _ in range(random.randint(3,4))]
    syms=[random.choice(symbols) for _ in range(random.randint(1,2))]

    pas=lets+nums+syms

    random.shuffle(pas)

    #final_pass=''
    #for _ in pas:
        #final_pass+=_

    final_pass=''.join(pas)

    pyperclip.copy(final_pass)

    pass_entry.delete(0,END)
    pass_entry.insert(0,final_pass)

def search():
    searchable=website_entry.get()
    try:
        with open("inventory.json") as f:
            diction=json.load(f)
            if searchable in diction:
                messagebox.showinfo("nice",f"This is your email and password:\n"
                                           f"{diction[searchable]['email']}\n"
                                           f"{diction[searchable]['password']}")
            else:
                messagebox.showinfo("error", "The website is not in the database")
    except FileNotFoundError:
        messagebox.showinfo("error","The appropriate database is not existent")
    except json.JSONDecodeError:
        messagebox.showinfo("error","The database is empty")

    website_entry.delete(0,END)

window=Tk()
window.title("Password manager")
window.config(padx=20,pady=20)

canvas=Canvas(width=200,height=189)
image=PhotoImage(file="logo.png")
canvas.create_image(100,94.5,image=image)
canvas.grid(column=1)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)
pass_label=Label(text="Password:")
pass_label.grid(column=0,row=3)

website_entry=Entry(width=39)
website_entry.focus()
website_entry.grid(column=1,row=1)
email_entry=Entry(width=57)
email_entry.insert(0,"arshia@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2)
pass_entry=Entry(width=39)
pass_entry.grid(column=1,row=3)

pass_button=Button(text='Generate password',highlightthickness=0,command=generate)
pass_button.grid(column=2,row=3)
add_button=Button(text="Add to inventory",command=add)
add_button.grid(column=1)
search_button=Button(text="Search",width=14,highlightthickness=0,command=search)
search_button.grid(row=1,column=2)



window.mainloop()