from tkinter import *
root = Tk()
root.title('Calculator')

e = Entry(root,width = 35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4)
def click(number):
    current = str(e.get())
    e.delete(0,END)
    e.insert(0,current + str(number))

def clear():
    e.delete(0,END)

def addition():
    number = e.get()
    global num1,instruction
    num1 = float(number)
    instruction = 'addition'
    e.delete(0,END)

def subtraction():
    number = e.get()
    global num1,instruction
    num1 = float(number)
    instruction = 'subtraction'
    e.delete(0,END)

def multiplication():
    number = e.get()
    global num1,instruction
    num1 = float(number)
    instruction = 'multiplication'
    e.delete(0,END)

def division():
    number = e.get()
    global num1,instruction
    num1 = float(number)
    instruction = 'division'
    e.delete(0,END)

def exponentiation():
    global num1,instruction
    number = e.get()
    num1 = float(number)
    instruction = 'exponentiation'
    e.delete(0,END)

def equal():
	num2 = e.get()
	List = ['addition','subtraction','multiplication','division','exponentiation']
	instr_id = List.index(instruction)
	if instr_id == 0:
		result = num1 + float(num2)
	elif instr_id == 1:
		result = num1 - float(num2)
	elif instr_id == 2:
		result = num1*float(num2)
	elif instr_id == 3:
		result = num1/float(num2)
	elif instr_id == 4:
		result = num1**float(num2)
	else:
		result = num2
	if result//(10**15)>=1:
		result = 'Number too big'
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
button_add = Button(root,text='+',padx=39,pady=20,fg='white',bg='black',command=addition)
button_subtract = Button(root,text='-',padx=40,pady=20,fg='white',bg='black',command=subtraction)
button_multiply = Button(root,text='*',padx=40,pady=20,fg='white',bg='black',command=multiplication)
button_division = Button(root,text='/',padx=42,pady=20,fg='white',bg='black',command=division)
button_power = Button(root,text='^',padx=39,pady=20,fg='white',bg='black',command=exponentiation)
button_clear = Button(root,text='C',padx=41,pady=116,fg='white',bg='black',command=clear)
button_equal = Button(root,text='=',padx=39,pady=20,fg='white',bg='black',command=equal)

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
button_power.grid(row=5,column=0)
button_clear.grid(row=2,column=3,rowspan=4)
button_equal.grid(row=5,column=2)


root.mainloop()