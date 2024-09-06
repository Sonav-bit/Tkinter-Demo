from tkinter import *
root=Tk()
root.geometry('400x400')
root.title('Tk')
root.config(bg='yellow')


l1=Label(root,text='Enter Username', fg='red',bg='orange')
l1.pack()
e1=Entry(root)
e1.pack()
l2=Label(root,text='Enter a password', fg='red',bg='orange')
l2.pack()

e2=Entry(root)
e2.pack()
def c1():
    user=e1.get()
    passw=e2.get()
    
    if user=='root' and passw=='root':
        l4=Label(root,text='Login Successful')
        l4.pack()
    else:
        l5=Label(root,text='Login failed')
        l5.pack()
b1=Button(root,text='Submit',command=c1)
b1.pack()

root.mainloop()
