#Lazy Buttons 2
#Demonstrates using a class with tkinter

from tkinter import *

class Application(Frame):
    """A GUI applicatiin with three buttons."""

    def __init__(self, master):
        """Inistialize the Frame."""
        super(Application, self).__intit__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create three buttons that do nothing."""
        #create first button
        self.bttn1 = Button(self,text = "I do nothing!")
        self.bttn1.grid()

        #create a second button in the frame
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Me too!")

        #create a third button in the frame
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3.["text"] = "Same here!"

#main
root = Tk()
root.tile("Lazy Buttons 2")
root.geometry("200x85")

app = Application(root)

root.mainloop()
