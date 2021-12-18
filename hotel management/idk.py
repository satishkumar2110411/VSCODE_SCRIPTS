import os


plans = [(1,'1 bed + sofa + integrated western toilet + bathroom + cupboard(AC) ',1000)\
            ,(2,'1 bed + sofa + integrated indian toilet + bathroom + cupboard + TV(AC)',800)\
            ,(3,'2 beds + 2 sofas + integrated western toilet + bathroom + cupboard(AC)',2000)
            ,(4,'2 beds + 2 sofas + separate western + indian toilet + bathroom + cupboard + TV(AC)',2500)
            ,(5,'king side bed + 1 bed + 2 sofas + integrated indian toilet + bathroom + cupboard + TV(AC)',3000)]
    
records = ['ROOM NUMBER','GUESTS','PLAN NUMBER','PHONE NUMBER','COST OF ROOM','DATE OF BOOKING']

Menu_list = ['Regular Tea','Masala Tea','Coffee','Cold drink','Milkshake','Yogurt','Tomato soup','Hot and sour soup','Mix vegetable soup','Corn soup'
             ,'Kadai Paneer','Palak Paneer','Chilli Paneer','Mushroom tikka','Jeera aloo','Aloo Matar','Bhindi fry'
             ,'Plain rice','Jeera rice','Veg Pulao','Plain roti','Butter naan','Plain dosa','Onion dosa','Masala dosa','Rice Idli','Veg Biriyani','Mushroom biriyani'
             ]
Cost_list = [20,25,25,25,30,30,50,50,70,60,100,110,115,135,100,105,120,90,95,110,15,20,70,85,100,100,150,155]    


#FUNCTION TO DISPLAY AVAILABLE PLANS
def Plans():
	print("Plans available: ")
	for i in plans:
		print(f'Plan number {i[0]} \n Plan details {i[1]} \n Plan price Rs. {i[2]}')

#FUNCTION TO GENERATE ALL ROOM NUMBERS AT THE BEGINNING OF THE PROGRAM
def room_initiation():
	file = open('Rooms.txt','ab+')
	content = file.read()
	if bool(content) == 1:
		file.close()
	else:
        content = [list(range(100,0,-1)),list(range(200,100,-1)),list(range(300,200,-1)),list(range(400,300,-1)),list(range(500,400,-1))]
        file.write(content)
        file.close()

#FUNCTION TO GIVE ROOM NUMBER ACCORDING TO PLAN
def Room_allotment(plan_no):
	file = open('Rooms.txt','rb+')
	temp = open('temp.txt','wb')
	content = file.read()
	room_no = content[plan_no -1].pop()
	temp.write(content)
	temp.close()
	file.close()
	os.remove('Rooms.txt')
	os.rename('temp.txt','Rooms.txt')
	return room_no


#FUNCTION TO INITIATE CUSTOMER EXPERIENCE

def Booking():
	file = open('Booking_details.txt','ab+')
	global records
	records= file.read()

	print('WELCOME TO HOTEL PROMETHEUS. PLEASE FOLLOW THE INSTRUCTIONS AND FILL IN THE REQUIRED DETAILS.')

	Plans()
	plan_no = int(input('Enter the plan number you want: '))
	if plan_no > 5 or plan_no < 1:
		print('Invalid plan number !!! Please start the procedure again!!')
	else:
		n= int(input('Enter the number of days of your stay: '))
		cost = n*plans[plan_no-1][2]*1.15

		guests_staying = []
		n = int(input('Enter the number of people staying: '))
		for i in range(n):
			guests_staying += [input('Enter name: '),]
		phone_no = int(input('Enter the phone number: '))
		date = input('Enter the date of booking(YYYY-MM-DD): ')
		room_no = Room_allotment(plan_no)

		print('The booking sequence is complete.')
		print('Plan chosen:',plans[plan_no-1][0])
		print(plans[plan_no-1][1])
		print('Total cost = ',cost)
		print('People staying: ')
		for i in guests_staying:
			print(i,'\n')
		print('Phone number: 'phone_no)
		print('Date of booking: ',date)
		print('Room number alloted: ',room_no)
		reply = input('Do you want to proceed with the above credentials{y/n}? ')
		if reply == 'y':
			records = [room_no,guests_staying,date,'Plan no '+str(plan_no),phone_no,cost]
			file.write(records)
			print('Booking successful!')
		else:
			r = input('Do you want to restart? (y/n): ')
			if r == 'y':
				Booking()
			else:
				print('Please visit later!! You are always welcome! ')
		file.close()

#FUNCTION TO DISPLAY THE MENU OF THE CAFETERIA

def Menu_display():
            print("-------------------------------------------------------------------------") 
            print("                           Hotel PROMETHEUS") 
            print("-------------------------------------------------------------------------") 
            print("                            Menu Card") 
            print("-------------------------------------------------------------------------")  
            print("\n BEVARAGES AND SOUPS                  SIDE DISHES") 
            print("----------------------------------      ---------------------------------") 
            print(" 1  Regular Tea............. 20.00      11 Kadai Paneer............100.00") 
            print(" 2  Masala Tea.............. 25.00      12 Palak Paneer............110.00") 
            print(" 3  Coffee.................. 25.00      13 Chilli Paneer...........115.00") 
            print(" 4  Cold Drink.............. 25.00      14 Mushroom Tikka..........135.00") 
            print(" 5  Milkshake............... 30.00      15 Jeera aloo..............100.00") 
            print(" 6  Yogurt.................. 30.00      16 Aloo Matar..............105.00") 
            print(" 7  Tomato soup............. 50.00      17 Bhindi fry..............120.00") 
            print(" 8  Hot and sour soup....... 50.00      ") 
            print(" 9  Mix vegetable soup...... 70.00") 
            print(" 10 Corn soup............... 60.00      ")  
            print()
            print(" MAIN COURSE                                  ") 
            print("----------------------------------      23 Plain dosa.............. 70.00") 
            print(" 18 Plain rice.............. 90.00      24 Onion dosa.............. 85.00") 
            print(" 19 Jeera rice.............. 95.00      25 Masala dosa............ 100.00") 
            print(" 20 Veg Pulao.............. 110.00      26 Rice Idli.............. 100.00") 
            print(" 21 Plain roti.............. 15.00      27 Veg biriyani........... 150.00") 
            print(" 22 Butter naan............. 20.00      28 Mushroom biriyani...... 155.00")
            print(" ------------------------------------------------------------------------")
            
            
#FUNCTION TO INTITIATE ROOM SERVICES

def Room_service():
	print('Welcome to room service menu. Room service stays open in the following timings: \n 6AM to 9AM \n 5PM to 6PM \n 8PM to 9PM')
	print('You can order anything from the general hotel menu.')
	Menu_display()
	n = int(input("How many dishes do you want to order? : "))
	total_cost = 0
	food = []
	for i in range(n):
		request = int(input('Enter the food item\'s number: '))
		number = int(input('Enter the number of plates/items : '))
		cost = number*Cost_list[request-1]*1.05
		total_cost += cost
		food.append([Menu_list[request-1],number,cost],)
	else:
		print('Final bill (tax inclusive): ')
		for i in food:
			for j in i:
				print(j,end = '\t')
			print()
		print('Total cost(5% GST inclusive) = ',total_cost)
		reply = input('Do you want to confirm? (y/n) : ')
		if reply == 'y':
			print('Please pay the bill via google pay with the QR code')
		else:
			reply = input('Do you wish to order again? (y/n) :')
			if reply == 'y':
				Room_service()
			else:
				print('Thank you! Keep visiting!')


#FUNCTION TO INITIATE CHECK OUT SEQUENCE

def check_out():
	file = open('Booking_details.txt','rb')
	file2 = open('Rooms.txt','rb')
	temp = open('temp.txt','wb')
	temp2 = open('temp2.txt','wb')
	room_no = int(input('Enter room number: '))
	phone_no = int(input('Enter the phone number used for registration: '))
	content = file.readlines()
	Plans()
	plan = int(input('Enter the plan number you chose: '))
	for i in content:
		if i[0]==room_no:
			pass
		else:
			temp.write(i)
	content = file2.read()
	content[plan-1] += [room_no,]
	content[plan-1].sort()
	temp2.write(content)
	file.close()
	file2.close()
	temp.close()
	temp2.close()
	os.remove('file.txt')
	os.remove('file2.txt')
	os.rename('temp.txt','file.txt')
	os.rename('temp2.txt','file2.txt')
	print('Check out successful')


#FUNCTION TO INITIATE CAB SERVICE SEQUENCE

def Cab_service():
    print('Welcome to the cab service centre.')
    destination = input('Enter the address of the destination: ')
    date = input('Enter the date on which it is required (YYYY-MM-DD): ')
    time = input('Enter the time during which it is required(HH:MM): ')
    print(destination,date,time)
    reply = input('Do you want to proceed or make changes or cancel(yes/change/cancel): ')
    if reply == 'yes':
        print('Booking sucessful.')
    elif reply == 'change':
        Cab_service()
    else:        
        print('Cab cancelled.')
    print('Cost of travel can be obtained by contacting the reception.')

#FUNCTION TO GENERATE FEEDBACK SYSTEM
    
def Feedback():
    file = open('feedback.txt','ab')
    print('You have entered the feedback session.')
    feedback = input('Enter the feedback you would wish to give. It can be related to anything: ')
    file.write(feedback)
    file.close()

def main():
	Room_initiation()
	print('---------HOTEL PROMETHEUS---------')
	print('Please select the action you would like to perform: ')
	print('1. Booking\n2. Room service\n3. Cab service\n4.Check out\n5. Feedback')
	ans = int(input('--> '))
	if ans == 1:
    	Booking()
	elif ans == 2:
    	Room_service()
	elif ans ==3:
    	Cab_service()
	elif ans == 4:
    	Check_out()
	elif ans == 5:
    	Feedback()
	else:
    	print('Please enter a valid number corresponding to the action.')