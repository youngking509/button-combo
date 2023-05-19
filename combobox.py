#import tinker from library
import tkinter as tk

from tkinter import ttk

#create a function
def on_select(event):

    #create an item that obtains value of the selected item
    selected_item = event.widget.get()
    print("Selected item:", selected_item)


#
root = tk.Tk()
root.title("King is funny")

#create an array called item
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
#create the combo box object, put the object in root window and populate value
combo_box = ttk.Combobox(root, values=items)

#the bind function will tie the selected item to the on_selected function
combo_box.bind("<<ComboboxSelected>>", on_select)
#Pack the object to the screen with the geometry manager
combo_box.pack()

#mainloop keeps the root parent window visible
root.mainloop()
