##############################################################
#          # Created by ManavPatni                           #
#          # Contact me on GitHub or Medium                  #
#          # Visit my website                                #
#          # https://fireframe.godaddysites.com/             #
##############################################################

#importing 
import tkinter as tk
from tkinter import filedialog
from tkinter.font import Font
from typing import Text
from tkinter import * 
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


#adding function to the menu bar
#file menu starting
#function for new file
def newFile():
    global File
    root.title("*Untitled - Notepad")
    root.iconbitmap('logo.ico')#you can use your logo here
    file = None
    TextArea.delete(1.0 , END)
#function for open file
def openFile():
    global File
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Doucments","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
#function for save file
def saveFile():
    global file
    if File == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Doucments","*.txt")])
    else:
        f = open(File, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        root.title(os.path.basename(File) + " - Notepad")

    if file == "": 
        file = None
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + " - Notepad")

    
#function for exit
def quitApp():
    root.destroy()
#file menu ending

#edit menu staring
#cut function
def cut():
    TextArea.event_generate(("<<Cut>>"))
#function copy
def copy():
    TextArea.event_generate(("<<Copy>>"))
#function paste
def paste():
    TextArea.event_generate(("<<Paste>>"))
#edit menu ending

#help menu
#about
def about():
    showinfo("About Notepad",''' 
       FireFrame
       Version 2021HQ 1.0.0 
       © FIREFRAME - ALL RIGHTS RESERVED.
       
       This software is useful for saving notes and written 
       information this software is free for all.
       
       This product is Licenced to FireFrame.''')
#help
def helpme():
    showinfo("Help",'''
        For Any help or error conctact us via email
        or visit out website.

        Email:- help.fireframe@gmail.com
                                     or
        Visit website:- https://fireframe.godaddysites.com/
          ''')
#help menu ending
#starting of the firepad
root = tk.Tk()


#window deigning
root.title("*Untitled - Notepad")
root.geometry("744x588")

#textarea
TextArea = Text(root, font="lucida 13")
File = None
TextArea.pack(expand=True, fill=BOTH)

#menu deigning
Menubar = tk.Menu(root)

#file menu 
Filemenu = tk.Menu(Menubar, tearoff=0)
#opning a new file 
Filemenu.add_command(label="New", command=newFile)
#to open a existing file 
Filemenu.add_command(label="Open", command=openFile)
#to save a current file
Filemenu.add_command(label="Save", command=saveFile)
Filemenu.add_separator()
#exit firepad
Filemenu.add_command(label="Exit", command=quitApp)
#adding file menu to the menu bar
Menubar.add_cascade(label="File", menu=Filemenu)
#ending of file menu

#edit menu
Editmenu = tk.Menu(Menubar, tearoff=0)

#adding cut, copy, paste operaction
Editmenu.add_command(label="Cut", command=cut)
Editmenu.add_command(label="Copy", command=copy)
Editmenu.add_command(label="Paste", command=paste)
#adding edit menu to menubar
Menubar.add_cascade(label="Edit", menu=Editmenu)
#ending of edit menu

#adding Anout and help in menu bar
Helpmenu = tk.Menu(Menubar, tearoff=0)

#about
Helpmenu.add_command(label="About", command=about)
Helpmenu.add_separator()
#help
Helpmenu.add_command(label="Help", command=helpme)
#adding help menu to menu bar
Menubar.add_cascade(label="Help", menu=Helpmenu)
#ending of help and abourt menu
#ending of menu bar
root.config(menu=Menubar)

#scrollbar
Scrollbar = Scrollbar(TextArea)
Scrollbar.pack(side=RIGHT, fill = Y)
Scrollbar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scrollbar.set)

#ending to firepad
root.mainloop()

#################################################################################################################################################################################
#                                                                                   THE END                                                                                     #
#################################################################################################################################################################################
