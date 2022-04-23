from tkinter import *
from tkinter import CENTER, ttk, messagebox
import tkinter.messagebox
import tkinter as tk
from tkinter import Tk, Label, Button
import tkinter.messagebox
import random 
import os
import tarfile
import sys
from tkinter.messagebox import showinfo
tk = tk.Tk()
my_menu = Menu(tk)
tk.config(menu=my_menu)
def our_command2():
    root = tkinter.Tk() 
    root.resizable(0,0)
    root.title("Who made this game?")

    labelTitle = ttk.Label(root,font=("Ubuntu", 12,"bold","underline"),anchor='center', text="Who made this game?")
    label = ttk.Label(root,font=("Ubuntu", 12,"bold",),anchor='center', text="Jonathan Steadman has made this game.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tkinter.Button(root, text="Exit",font=("ubuntu",16,),bg="#0e639c",activebackground='orange', command = root.destroy)
    B1.pack()
def our_command3():
    root = tkinter.Tk() 
    root.resizable(0,0)
    root.title("What is this game about?")


    labelTitle = ttk.Label(root,font=("Ubuntu", 12,"bold","underline"),anchor='center', text="What is this game about?")
    label = ttk.Label(root,font=("Ubuntu", 12,"bold",),anchor='center', text="This is a TicTacToe clone but open source and is for Linux and FreeBSD.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tkinter.Button(root, text="Exit",font=("ubuntu",16,),bg="#0e639c",activebackground='orange', command = root.destroy)
    B1.pack()
def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
file_menu= Menu(my_menu,background="#0e639c",activebackground="orange",border="6")
my_menu.add_cascade(label="About:",font=("Ubuntu",12),background="#0e639c",activebackground="orange", menu=file_menu)
file_menu.add_command(label="Who made this game?",font=("Ubuntu",12,),activebackground="orange",background="#0e639c",command=our_command2) 
file_menu.add_command(label="What is this game about?",font=("Ubuntu",12,),activebackground="orange",background="#0e639c",command=our_command3) 
file_menu2= Menu(my_menu,background="#0e639c",activebackground="orange",border="6")
my_menu.add_cascade(label="Actions:",font=("Ubuntu",12),background="#0e639c",activebackground="orange", menu=file_menu2)
file_menu2.add_command(label="Restart This Game",font=("Ubuntu",12,),activebackground="orange",background="#0e639c",command=restart) 



tk.title("P1 VS P2 For Linux 4.0!")
tk.config(bg='#90ee90')
image = PhotoImage(file='icon.png')
tk.tk.call('wm', 'iconphoto', tk._w, image) #The icon I have made. :)
tk.resizable(0,0)
pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

bclick = True
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)



def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "P1"
        bclick = False
        playerb = p2.get() + "Player two wins!"
        pa = p1.get() + "Player one wins!"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "P2"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Sorry", "Button has allready been clicked!")

def checkForWin():
    if (button1['text'] == 'P1' and button2['text'] == 'P1' and button3['text'] == 'P1' or
        button4['text'] == 'P1' and button5['text'] == 'P1' and button6['text'] == 'P1' or
        button7['text'] =='P1'  and button8['text'] == 'P1' and button9['text'] == 'P1' or
        button1['text'] == 'P1' and button5['text'] == 'P1' and button9['text'] == 'P1' or
        button3['text'] == 'P1' and button5['text'] == 'P1' and button7['text'] == 'P1' or
        button1['text'] == 'P1' and button2['text'] == 'P1' and button3['text'] == 'P1' or
        button1['text'] == 'P1' and button4['text'] == 'P1' and button7['text'] == 'P1' or
        button2['text'] == 'P1' and button5['text'] == 'P1' and button8['text'] == 'P1' or
        button7['text'] == 'P1' and button6['text'] == 'P1' and button9['text'] == 'P1'):
        disableButton()
        tkinter.messagebox.showinfo("P1 VS P2!", pa)

    elif(flag == 8):
        tkinter.messagebox.showinfo("P1 VS P2!", "It is a Tie!")

    elif (button1['text'] == 'P2' and button2['text'] == 'P2' and button3['text'] == 'P2' or
          button4['text'] == 'P2' and button5['text'] == 'P2' and button6['text'] == 'P2' or
          button7['text'] == 'P2' and button8['text'] == 'P2' and button9['text'] == 'P2' or
          button1['text'] == 'P2' and button5['text'] == 'P2' and button9['text'] == 'P2' or
          button3['text'] == 'P2' and button5['text'] == 'P2' and button7['text'] == 'P2' or
          button1['text'] == 'P2' and button2['text'] == 'P2' and button3['text'] == 'P2' or
          button1['text'] == 'P2' and button4['text'] == 'P2' and button7['text'] == 'P2' or
          button2['text'] == 'P2' and button5['text'] == 'P2' and button8['text'] == 'P2' or
          button7['text'] == 'P2' and button6['text'] == 'P2' and button9['text'] == 'P2'):
        disableButton()
        tkinter.messagebox.showinfo("P1 V P2", playerb)


buttons = StringVar()

label = Label( tk, text="P1 VS P2!", font=('ubuntu'"underline""bold"),background="#90ee90", fg='black', height=1, width=11)
label.grid(row=1, column=1)


button1 = Button(tk, text=" ", font='Ubuntu' "bold",border="6", bg='#0e639c',activebackground='orange', fg='black', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Ubuntu' "bold",border="6", bg='#0e639c',activebackground='orange', fg='black', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Ubuntu' "bold",border="6", bg='#0e639c',activebackground='orange', fg='black', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Ubuntu' "bold",border="6", bg='#0e639c',activebackground='orange', fg='black', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Ubuntu' "bold",border="6", bg='#0e639c',activebackground='orange', fg='black', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Ubuntu' "bold",border="6", bg='#0e639c',activebackground='orange', fg='black', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Ubuntu' "bold",border="6", bg='#0e639c',activebackground='orange', fg='black', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Ubuntu' "bold",border="6", bg='#0e639c',activebackground='orange', fg='black', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Ubuntu' "bold",border="6", bg='#0e639c',activebackground='orange', fg='black', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

tk.mainloop()