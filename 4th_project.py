from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def main():
    """main function"""
    root = Tk()
    root.geometry("300x300")
    
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    
    background_image = ImageTk.PhotoImage(Image.open("bg.jpg"))
    background_label = ttk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.mainloop()
    
if __name__ == "__main__":
    main()