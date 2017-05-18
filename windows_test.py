from tkinter import *


root=Tk()
root.title('测试应用软件')
li=['C','python','php','html']
movie=['css','jquery','bootstrap']

listtb=Listbox(root)
listtb2=Listbox(root)

for item in li:
    listtb.insert(0,item)

for item in movie:
    listtb2.insert(0,item)

listtb.pack()
listtb2.pack()
root.mainloop()