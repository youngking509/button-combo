#import tkinter from library
import tkinter as tk


#create a function called button clicked then print it
def button_click():
    print("button clicked!")


#created a root window
root = tk.Tk()
root.title("button example")


#create an object for the button
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

#this is the root
root.mainloop()


