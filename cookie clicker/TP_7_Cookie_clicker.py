from tkinter import *

window= Tk()
cookies = 0
upgrade_price = 10
click=1

def add_cookies():
    global cookies
    global click
    cookies += click
    nb_cookies.delete(0, END)
    nb_cookies.insert(0, cookies)
    print(cookies)
    shop.entryconfigure(1, label="Upgrade for " + str(upgrade_price) + " Cookies")



def upgrade():
    global upgrade_price
    global click
    global cookies
    if cookies >= upgrade_price:
        cookies -= upgrade_price
        nb_cookies.delete(0, END)
        nb_cookies.insert(0, cookies)
        click *= 2
        upgrade_price = upgrade_price*2+50
        print(upgrade_price)




window.title("Cookie Cliker")

# Taille et taille minimum de la fenetre
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background="#69E7BB")
window.iconbitmap("Cookie.ico")


label_title = Label(window, text="Click to get more cookies !!!", font=("Halvetica",30), bg="#69E7BB")
label_title.place(relx=0.5, rely=0, anchor=CENTER)
label_title.pack(pady=80)

nb_cookies = Entry(window, font=("Halvetica", 20), bg="white")
nb_cookies.pack( pady=20)

width = 300
height = 300
image =  PhotoImage(file="Cookie.png")

cookie = Button(window ,text=(cookies), image=image, bg="#69E7BB", command=add_cookies, bd=0, highlightthickness=0)
cookie.pack(pady=40)

menu = Menu(window)

shop = Menu(menu, tearoff=0)
shop.add_command(label="Upgrade for " + str(upgrade_price) + " Cookies", command=upgrade)
menu.add_cascade(label="shop", menu=shop)

window.config(menu=menu)

window.mainloop()
