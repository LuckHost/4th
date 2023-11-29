from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class App():
    def __init__(self, master):
        frm = ttk.Frame(master, padding =10)
        frm.pack()
        
        self.canvas = Canvas(width = 300, height = 300, bg = 'blue')
        self.but = Button(master, text="Click me!", command=self.get_image)
        self.canvas.create_window(10, 10, anchor="nw", window=self.but)
        self.canvas.pack()
        
    def get_image(self):
        self.background_image = ImageTk.PhotoImage(file="bg.jpg")
        self.canvas.create_image(0, 0, image = self.background_image, anchor = "nw")
        

def main():
    """main function"""
    root = Tk()
    root.geometry("300x300")
    App(root)
    root.mainloop()
    #frm = ttk.Frame(root, padding=10)
    
if __name__ == "__main__":
    main()