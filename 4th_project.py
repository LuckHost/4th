""" 4я работа по ввпд СФУ вариант 6
Выполнил Ходыкин Александр КИ23-17/2б"""

from tkinter import *
from tkinter import ttk
from PIL import *

class App():
    def __init__(self, master):
        """ creating buttons and canvas """
        frm = ttk.Frame(master, padding =10)
        frm.pack()
        
        self.canvas = Canvas(width = 300, height = 300, bg = 'blue')

        self.but = Button(master, text="Сброс", command=self.get_image)
        self.but2 = Button(master, text="Изменить цвет", command=self.change_color)
        self.chkbox_var = BooleanVar()
        self.chkbox = Checkbutton(master, text="Темнее", variable=self.chkbox_var, offvalue=False, onvalue=True)
        
        self.canvas.create_window(10, 10, anchor="nw", window=self.but)
        self.canvas.create_window(200, 10, anchor="nw", window=self.but2)
        self.canvas.create_window(224, 60, anchor="nw", window=self.chkbox)
        
        self.canvas.pack()
        
    def get_image(self):
        """ creating and adding an image
        """
        self.background_image = PhotoImage(file="bg.png")
        self.image_id = self.canvas.create_image(0, 0, image = self.background_image, anchor = "nw")

    def change_color(self):
        """ color changing """
        self.image = PhotoImage(width=300, height=300)
        for x in range(300):
            for y in range(300):
                rgb = list(self.background_image.get(x, y))
                for i in range(len(rgb)):
                    if self.chkbox_var.get() == True: 
                        rgb[i] = rgb[i] // 2
                    else:
                        rgb[i] = int(rgb[i] * 1.5)
                        if rgb[i] > 254:
                            rgb[i] = 255
                
                self.image.put("#%02x%02x%02x" % tuple(rgb), (x, y))        
        self.background_image = self.image
        self.canvas.itemconfig(self.image_id, image = self.background_image)

def main():
    """main function"""
    root = Tk()
    root.geometry("300x300")
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()