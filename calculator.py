from tkinter import *

def click(event):
   global scvalue
   text = event.widget.cget("text")
   print(text)
   if text == "=":
       if scvalue.get().isdigit():
           value = int(scvalue.get())
       else:
           try:
               value = eval(screen.get())
           except Exception as e:
               print(e)
               value = "Error"

       scvalue.set(value)
       screen.update()

   elif text =="C":
       scvalue.set("")
       screen.update()

   else:
       scvalue.set(scvalue.get() + text)
       screen.update()

root = Tk()
root.geometry("360x610")
root.title("Calculator By Rashmi")
root.wm_iconbitmap("")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue, font = "lucida 27 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root,bg="grey")
b = Button(f,text="9",padx = 20,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)

b = Button(f,text="8",padx = 20,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)

b = Button(f,text="7",padx = 20,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="6",padx = 20,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)

b = Button(f,text="5",padx = 20,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)

b = Button(f,text="4",padx = 20,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="3",padx = 20,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)

b = Button(f,text="2",padx = 20,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)

b = Button(f,text="1",padx = 20,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="0",padx = 20,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)

b = Button(f,text="-",padx = 21,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 15,pady = 5)
b.bind("<Button-1>",click)

b = Button(f,text="+",padx = 19,pady = 9,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="*",padx = 20,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)

b = Button(f,text="%",padx = 18,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)

b = Button(f,text="C",padx = 18,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text=".",padx = 23,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)

b = Button(f,text="/",padx = 23,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)

b = Button(f,text="=",padx = 22,pady = 10,font="lucida 22 bold")
b.pack(side=LEFT,padx = 12,pady = 5)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()