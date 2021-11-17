# To design a function that arrange three numbers in ascending order

def arrange(x,y,z):
	if x<=y and x<=z:
		if y<= z:
			x,y,z=x,y,z
		else:
			x,y,z=x,z,y

	elif y<=x and y<=z:
		if x<=z:
			x,y,z = y,x,z
		else:
			x,y,z = y,z,x
	else:
		if x<=y:
			x,y,z = z,x,y
		else:
			x,y,z = z,y,x

	print('The ascending order is: ',x,y,z)

a = int(input('Enter number: '))
b = int(input('Enter number: '))
c = int(input('Enter number: '))
arrange(a,b,c)

# To create a recursive function to find the sum of numbers in the list

def sum_of_list(list_):
	return(list_.pop()+sum_of_list(list_))

list_=[]
n = int(input('Enter the number of numbers you want to enter in the list: '))
for i in range(n):
	x = int(input('Enter number: '))
	list_.append(x)

sum_of_list(list_)

#To create a function that checks whether a given string is a palindrome or not

def palindrome_check(string):
	if len(string)<1:
		return(1)
	else:
		if string[0]==string[-1]:
			palindrome_check[1:-1]
		else:
			return(0)

string = input('Enter the string that needs to be checked for palindrome: ')
x = palindrome_check(string)
if x == 1:
	print(string,'is a palindrome')
else:
	print(string,'is not a palindrome')

#To create a function that swaps the odd indexed integers with the even indexed integers in a list

def swap(list_):
	for i in range(x//2):
			list_[i],list_[i+1]=list_[i+1],list_[i]
	
list_ = []
n = int(input('Enter the number of elements you want to enter: '))
for i in range(n):
	x = int(input('Enter number: '))
	list_.append(x)
swap(list_)

#To create a function that bubble sorts a list in ascending order

def bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(n-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]

array = []
n = int(input('Enter the number of elements you want to enter: '))
for i in range(n):
	x = int(input('Enter number: '))
	array.append(x)
print('Original list entered: ',array)
bubble_sort(array)
print('The ascending order of the list is: ',array)

#To create functions Pop(),Push() and Display() to remove,add and display numbers in a list

def Pop(array):
	array.pop()

def Push(array):
	n = int(input('Enter the element to be pushed into the stack: '))
	array.append(n)

def Display(array):
	for i in array:
		print(i,end =' ')
	print()

array =[]
n = int(input('Enter the number of elements you want to enter: '))
for i in range(n):
	x = int(input('Enter number: '))
	array.append(x)
Display(array)
Pop(array)
Display(array)
Push(array)
Display(array)

#To create a function that stores words in a text file and another function that counts the number of times a certain words appeared

def store_words():
	file = open('content.txt','w')
	n = int(input('Enter the number of words you want to enter: '))
	for i in range(n):
		x = input('Enter the word: ')
		file.write(x+'\n')
	file.close()

def count_words():
	file = open('content.txt','r')
	content = file.read()
	a,an,the=0,0,0
	count = 0
	for i in content:
		if i.lower() in ['a','an','the']:
			count+=1
	print('Number of times a,an,the occurs is: ',count)
	file.close()

store_words()
count_words()

#To write a python program with a binary file vehicle.dat with the structure [reg.no,type,make,price]. Write a function register in python
#to create the binary file with n vehicles. A function display to read the contents of the file and display details of those vehicles whose
#price is greater than or equal to 90000

import pickle

def register_vehicle():
	file = open('vehicle.dat','ab')
	reg_no = input('Enter the registration number of the vehicle: ')
	type_ = input('Enter the vehicle type: ')
	make = input('Enter the make of the vehicle: ')
	price = int(input('Enter the price of the vehicle: '))
	record = [reg_no,type_make,price]
	pickle.dump(record,file)
	file.close()

def display():
	file = open('vehicle.dat','rb')
	try:
		while True:
			record = pickle.load(file)
			if record[3]>=90000:
				print(record)

	except EOFError:
		pass

n = int(input('How many vehicles do you want to register: '))
for i in range(n):
	register_vehicle()

display()

#To create a function that uses CSV files to store marks of students and update marks of certain students

import pickle,occurs

def create_record():
	file = open('marks.dat','wb')
	name = input('Enter name: ')
    roll_no = int(input('Enter roll number of student: '))
    marks = int(input('Enter marks of student: '))
    record = [roll_no,name,marks]
    pickle.dump(record,file)
    file.close()

def update_marks():
	file = open('marks.dat','rb')
	temp = open('temp.dat','wb')
	roll_no = int(input('Enter the roll number of the student whose marks needs to be changed: '))
	for i in range(strength):
		record = pickle.load(file)
		if record[0]==roll_no:
			record[2]=marks
		pickle.dump(record,temp)
	file.close()
	temp.close()
	os.remove('marks.dat')
	os.rename('temp.dat','marks.dat')
	print('Updation of marks successful')

strength = int(input('Enter strength of class: '))
for i in range(strength):
	create_record()
n = int(input('Enter the number of students whose marks needs to be updated: '))
for i in range(n):
	update_marks()

#SQL CONNECTION
import mysql.connector as sql
connect = sql.connect(host = 'localhost',user='root',passwd = 'Sa@231203',database='computer')
if connect.is_connected():
	print('Successdully connected')
else:
	print('Connection failed')
cursor = connect.cursor()

print('PART 1')
cursor.execute('select * from mobile')
try:
	row = cursor.fetchone()
	while row is not None:
		print(row)
		row = cursor.fetchone()
except EOFError:
	pass

print('PART 2')
cursor.execute('select * from mobile')
content = cursor.fetchall()
print(content)

print('PART 3')
cursor.execute('delete from mobile where M_Price>40000')
cursor.execute('select * from mobile')
content = cursor.fetchall()
print(content)

print('PART 4')
cursor.execute('update mobile set M_Price = 17999 where M_Id = 1002')
cursor.execute('select * from mobile')
print(cursor.fetchall())

print('PART 5')
cursor.execute('select M_Name,M_Make,M_Price from mobile')
print(cursor.fetchall())

connect.close()

#END OF ALL THE PROGRAMS