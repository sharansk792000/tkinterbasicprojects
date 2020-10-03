from tkinter import *

root = Tk()
root.geometry('400x400')

user_dict = {
    "username" : "admin",
    "password" : "password"
}

user_label = Label(root, text="Username", padx=20, pady=10)
pwd_label = Label(root, text="Password", padx=20, pady=10)

user_label.grid(row=0, column=0)
pwd_label.grid(row=1, column=0)

user_input = Entry(root, borderwidth=2)
pwd_input = Entry(root, borderwidth=2)

user_input.grid(row=0, column=1)
pwd_input.grid(row=1, column=1)

def check():
    user = user_input.get()
    password = pwd_input.get()

    if user == user_dict["username"]:
        if password == user_dict["password"]:
            label = Label(root, text="Logged In")
            label.grid(row=3,column=0, columnspan=2)

    else:
        label = Label(root, text="invalid")
        label.grid(row=3,column=0, columnspan=2)


button = Button(root,text="Submit", padx=10, pady=10, width=15, command=check)
button.grid(row=2, column=0,columnspan=2,padx=20,sticky=W+E)


root.mainloop()