from tkinter import *

def click(event):
    global scvalue
    text= event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("550x550")
root.title("Calculator for codeclause by Raghav Sharma")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="Arial 25 bold")
screen.pack(fill=X, ipadx=8,pady=10, padx=10)

f= Frame(root,bg="Blue")

b= Button(f, text="9", padx=30, pady=15 , font= "lucida 25 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b= Button(f, text="8", padx=30, pady=15 , font= "lucida 25 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b= Button(f, text="7", padx=30, pady=15 , font= "lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=5)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg="Black")

b= Button(f, text="6", padx=30, pady=15 , font= "lucida 25 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b= Button(f, text="5", padx=30, pady=15 , font= "lucida 25 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b= Button(f, text="4", padx=30, pady=15 , font= "lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=5)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg="Black")

b= Button(f, text="3", padx=30, pady=15 , font= "lucida 25 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b= Button(f, text="2", padx=30, pady=15 , font= "lucida 25 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b= Button(f, text="1", padx=30, pady=15 , font= "lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=5)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg="Black")

b= Button(f, text="0", padx=30, pady=25 , font= "lucida 25 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b= Button(f, text="/", padx=33, pady=20 , font= "lucida 25 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b= Button(f, text="*", padx=33, pady=20 , font= "lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=5)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg="Black")

b= Button(f, text="-", padx=28, pady=26 , font= "lucida 25 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b= Button(f, text="+", padx=30, pady=26 , font= "lucida 25 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b= Button(f, text="%", padx=30, pady=26 , font= "lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=5)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg="Black")

b= Button(f, text="=", padx=30, pady=15 , font= "lucida 25 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b= Button(f, text="C", padx=30, pady=15 , font= "lucida 25 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)
f.pack()


root.mainloop()