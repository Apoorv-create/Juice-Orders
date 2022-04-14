from tkinter import *
from PIL import ImageTk, Image    
from tkinter import ttk

root = Tk()
root.title("Juice Order")
root.geometry("900x900")
root.config(bg="orange2")

#Gui
#heading
label_heading = Label(root, text = "Order The Juice Here!", bg="orange2", font=(18))
label_heading.place(relx = 0.05, rely = 0.1, anchor=W)

#Logo
#juice = ImageTk.PhotoImage(Image.open(r"P:\Python projects\Juice Orders\logo.png"))
#juice_image = Label(root, image=juice, bg = "orange2")
#juice_image.place(relx = 0.2, rely = 0.4, anchor=CENTER)

#Load the fruit images
#apple = ImageTk.PhotoImage(Image.open(r"P:\Python projects\Juice Orders\apple_img.png"))
#orange = ImageTk.PhotoImage(Image.open(r"P:\Python projects\Juice Orders\orange.png"))
#mango = ImageTk.PhotoImage(Image.open(r"P:\Python projects\Juice Orders\mango_img.png"))

#The Fruit Image thing
fruit_image = Label(root, bg="orange2")
fruit_image.place(relx = 0.75, rely = 0.8, anchor=CENTER)

#Choose The Fruit
Label_choose = Label(root, text = "Choose the Fruit Flavour!", bg = "orange2", font=(24))
Label_choose.place(relx = 0.96, rely = 0.2, anchor=E)

#The DropDown 
fruit_list=["Apple", "Orange", "Mango"]
fruit_dropdown = ttk.Combobox(root, state = "readonly", values=fruit_list, justify="right")
fruit_dropdown.place(relx = 0.96, rely = 0.25, anchor=E)

#Label Quantity
label_quantity = Label(root, text = "Quantity?", bg="orange2")
label_quantity.place(relx = 0.96, rely = 0.35, anchor=E)

#Entry
input_quantity = Entry(root)
input_quantity.place(relx = 0.95, rely = 0.4, anchor=E)

#Total Cost
label_total_cost = Label(root, bg="orange2")
label_total_cost.place(relx = 0.95, rely = 0.7, anchor=E)

#Quantity
label_show_quantity = Label(root, bg = "orange2")
label_show_quantity.place(relx = 0.95, rely = 0.8, anchor=E)

#Gui Over

class Juice():
    def __init__(self, fruit_name, quantity):
        self.fruit = fruit_name
        self.quantity = int(quantity)
        self._cost = 250
    def _calculateCost(self):
        total_cost = self.quantity * self._cost
        label_total_cost['text'] = ("You have to pay: " + str(total_cost) + "Rupees")
        if(self.fruit == "Apple"):
            calorie = self.quantity * 52
        if(self.fruit == "Mango"):
            calorie = self.quantity * 60
        if(self.fruit == "Orange"):
            calorie = self.quantity * 47
            label_show_quantity['text'] = ("x" + str(self.quantity) + "=" + str(calorie) + "calroies")
            
    def getcost(self):
        self._calculateCost()
        
def orderJuice():
    fruit = fruit_dropdown.get()
    quantity = input_quantity.get()
    obj1 = Juice(fruit, quantity)
    obj1.getcost()
        
btn = Button(root, text = "Total", bg="white", command=orderJuice)
btn.place(relx = 0.95, rely = 0.5, anchor=E)

root.mainloop()