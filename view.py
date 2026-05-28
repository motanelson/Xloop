import tkinter as tk
from tkinter import filedialog

class myapps:
    def __init__(self,root:tk.Tk,files:str,backgrounds:str,foregrounds:str):
        self.root=root
        self.root.title(files)
        self.root.geometry("640x480")
        self.root.configure(background=backgrounds)
        self.text=tk.Text(background=backgrounds,foreground=foregrounds)
        self.text.pack(padx=10,pady=10)
        f1=open(files,"r")
        a=f1.read()
        f1.close()
        self.text.insert("1.0",a)
    


def views(files:str,backgrounds:str="black",foregrounds:str="white"):
    root=tk.Tk()
    apps=myapps(root,files,backgrounds,foregrounds)
    root.mainloop()





f1=filedialog.askopenfilename(defaultextension="*.*",title="file open")
views(files=f1)