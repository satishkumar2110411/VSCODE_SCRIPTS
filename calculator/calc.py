from tkinter import *
root = Tk()
root.title('Calculator')
num1 = None
instruction = None

e = Entry(root,width = 35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4)
def click():
    number = e.get()
    e.delete(0,END)
    e.insert(0,number + str(e.get()))

def clear():
    e.delete(0,END)

def addition():
    number = e.get()
    num1 = int(number)
    instruction = 'addition'
    e.delete(0,END)

def subtraction():
    number = e.get()
    num1 = int(number)
    instruction = 'subtraction'
    e.delete(0,END)

def multiplication():
    number = e.get()
    num1 = int(number)
    instruction = 'multiplication'
    e.delete(0,END)

def division():
    number = e.get()
    num1 = int(number)
    instruction = 'division'
    e.delete(0,END)

def exponentiation():
    number = e.get()
    num1 = int(number)
    instrcution = 'exponentiation'
    e.delete(0,END)

def equal():
    num2 = int(e.get())
    if instruction == 'addition':
        result = num1+num2
    elif instruction == 'subtraction':
        result = num1-num2
    elif instruction == 'multiplication':
        result = num1*num
    elif instruction == 'division':
        result = num1/num2
    elif instruction == 'exponentiation':
        result = num1**num2
    else:
        result = num2
    if result//(10**15)>=1:
        result = "Number to big"
    e.delete(0,END)
    e.insert(0,result)

button0 = Button(root,text='0',padx=40,pady=20,fg='white',bg='black',command=lambda: click(0))
button1 = Button(root,text='1',padx=40,pady=20,fg='white',bg='black',command=lambda: click(1))
button2 = Button(root,text='2',padx=40,pady=20,fg='white',bg='black',command=lambda: click(2))
button3 = Button(root,text='3',padx=40,pady=20,fg='white',bg='black',command=lambda: click(3))
button4 = Button(root,text='4',padx=40,pady=20,fg='white',bg='black',command=lambda: click(4))
button5 = Button(root,text='5',padx=40,pady=20,fg='white',bg='black',command=lambda: click(5))
button6 = Button(root,text='6',padx=40,pady=20,fg='white',bg='black',command=lambda: click(6))
button7 = Button(root,text='7',padx=40,pady=20,fg='white',bg='black',command=lambda: click(7))
button8 = Button(root,text='8',padx=40,pady=20,fg='white',bg='black',command=lambda: click(8))
button9 = Button(root,text='9',padx=40,pady=20,fg='white',bg='black',command=lambda: click(9))
button_add = Button(root,text='+',padx=40,pady=20,fg='white',bg='black',command=addition)
button_subtract = Button(root,text='-',padx=40,pady=20,fg='white',bg='black',command=subtraction)
button_multiply = Button(root,text='*',padx=40,pady=20,fg='white',bg='black',command=multiplication)
button_divide = Button(root,text='/',padx=40,pady=20,fg='white',bg='black',command=division)
button_power = Button(root,text='^',padx=40,pady=20,fg='white',bg='black',command=exponentiation)
button_clear = Button(root,text='Clear',padx=40,pady=20,fg='white',bg='black',command=clear)
button_equal = Button(root,text='=',padx=40,pady=20,fg='white',bg='black',command=equal)

button0.grid(row=5,column=1)
button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
button_add.grid(row=1,column=0)
button_subtract.grid(row=1,column=1)
button_multiply.grid(row=1,column=2)
button_division.grid(row=1,column=3)
button_exponentiation.grid(row=5,column=0)
button_clear.grid(row=2,column=3,rowspan=4)
button_equal.grid(row=5,column=2)


root.mainloop()