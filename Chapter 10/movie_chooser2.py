#Movie Chooser 2
#Demonstrates radio buttons

from tkinter import *

class Application(Frame):
    """GUI Application for favorite movie types."""
    def __init__(self, master):
        """Initialiaze the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """Create widgets for movie type choices"""
        #create desccription label
        Label(self, text = "Choose your favorite movie types"
              ).grid(row = 0, column = 0, sticky = W)

        #create instruction label
        Label(self, text = "Select all that apply"
              ).grid(row = 1, column = 0, sticky = W)

        #create variable for single, favorite type of movie
        self.favorite = StringVar()
        self.favorite.set(None)

        #create comedy radio button
        Radiobutton(self,
                    text = "Comedy",
                    variable = self.favorite,
                    command = self.update_text).grid(row = 2, colum = 0, sticky = W)

        #create Drama radio button
        Radiobutton(self,
                    text = "Drama",
                    variable = self.favorite,
                    command = self.update_text).grid(row = 3, colum = 0, sticky = W)

        #create Romance check button
        Radiobutton(self,
                    text = "Romance",
                    variable = self.favorite,
                    command = self.update_text).grid(row = 4, colum = 0, sticky = W)

        #create text field to display results
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
            """Update the text area and dispaly user's favorite movie type."""
            message = "Ypur favorite type of movie is "
            message += self.favorite.get()

            self.results_text.delete(0.0, END)
            self.results_txt.insert(0.0, message)

#main
root = Tk()
root.title("Movie Chooser 2")
app = Application(root)
root.mainloop()
