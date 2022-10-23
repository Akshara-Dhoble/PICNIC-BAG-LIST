from tkinter import *
import random

root = Tk()
root.title("PICNIC BAG LIST")
root.geometry("400x400")

label_list = Label(root)
label_item = Label(root)

list_items = ["Water Battle" , "Tiffin" , "ID Card" , "Chocolates" , "Chips" , "Tickets" , "Hanky"]
label_list["text"] = "listed Item : " + str(list_items)


def randomlist():
    
    random_list = random.sample(range(0,7) , 1)
    random_item["text"] = "Put Item No. : " + str(random_list) + "In Bag" 
    
    label_list.place(relx=0.5 , rely=0.4 , anchor = CENTER)
    
    btn = Button(root , text = "Which item to put in bag ? " , command=big_item , bg = "cream" , fg = "black")
    
    btn.place(relx=0.5 , rely=0.5 , anchor = CENTER)
    
    label_item.place(relx=0.5 , rely= 0.6 , anchor=CENTER)
    
root.mainloop()