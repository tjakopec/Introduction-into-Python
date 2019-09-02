from tkinter import Tk, Label, Button, Entry, StringVar
import ESSIS as k
#Class
class Prozor:
    #Constructor
    def __init__(self, master):
        self.master = master
        master.title("GUI window")

        # Input fiels
        self.input_field = Entry(root)
        self.input_field.pack()
        self.input_field.focus_set()

        # Button
        self.btnCalculate = Button(
            master,
            text="Prime number?",
            fg="#0000ff",
            command=self.btnCalculate_click)
        self.btnCalculate.pack()

        # Label for showing results
        self.labela_text = StringVar()
        self.labela_text.set("This is how we build GUI apps")
        self.labela = Label(master, textvariable=self.labela_text)
        self.labela.pack()

    # EVENT function, I use all kinds of naming conventions. Details how to use propper naming for python https://www.python.org/dev/peps/pep-0008/
    def btnCalculate_click(self):
        try:
            self.labela_text.set(
                "number" +
                ( " is " if e.primeNumber(int(self.input_field.get())) else " not ") +
                " prime number"
                )
        except ValueError:
            self.labela_text.set("Insert integer that is grater that 0")
        
#new instance of Thinker
root = Tk()
prozor = Prozor(root)
root.mainloop()
