#REQUIRED MODULES

import pickle,os

#GLOBAL VARIABLES

plans = [(1,'1 bed + sofa + integrated western toilet + bathroom + cupboard(AC) ',1000)\
            ,(2,'1 bed + sofa + integrated indian toilet + bathroom + cupboard + TV(AC)',800)\
            ,(3,'2 beds + 2 sofas + integrated western toilet + bathroom + cupboard(AC)',2000)
            ,(4,'2 beds + 2 sofas + separate western + indian toilet + bathroom + cupboard + TV(AC)',2500)
            ,(5,'king side bed + 1 bed + 2 sofas + integrated indian toilet + bathroom + cupboard + TV(AC)',3000)]
    
record = ['ROOM NUMBER','GUESTS','PLAN NUMBER','PHONE NUMBER','COST OF ROOM','DATE OF BOOKING']

Menu_list = ['Regular Tea','Masala Tea','Coffee','Cold drink','Milkshake','Yogurt','Tomato soup','Hot and sour soup','Mix vegetable soup','Corn soup'
             ,'Kadai Paneer','Palak Paneer','Chilli Paneer','Mushroom tikka','Jeera aloo','Aloo Matar','Bhindi fry'
             ,'Plain rice','Jeera rice','Veg Pulao','Plain roti','Butter naan','Plain dosa','Onion dosa','Masala dosa','Rice Idli','Veg Biriyani','Mushroom biriyani'
             ]
Cost_list = [20,25,25,25,30,30,50,50,70,60,100,110,115,135,100,105,120,90,95,110,15,20,70,85,100,100,150,155]    

#FUNCTION DEFINITIONS


#FUNCTION STORING ALL PLAN STRUCTURES

def Plans():
    print('PLANS AVAILABLE:-')
    for i in plans:
        print('Plan number: ',i[0],'\nPlan Details: ',i[1],'\nPlan price per day',i[2])


#FUNCTION TO GENERATE THE ROOM NUMBER OF THE GUEST
def Room_initiation():
    file = open('Room.dat','ab+')
    content = pickle.load(file)
    if bool(content)==1:
        file.close()
    else:
        try:
            content = [list(range(100,0,-1)),list(range(200,100,-1)),list(range(300,200,-1)),list(range(400,300,-1)),list(range(500,400,-1))]
            pickle.dump(content,file)
            file.close()
        except EOFError:
            pass
        
        
def Rooms():
    file = open('Room.dat','rb+')
    temp = open('temp2.dat','wb+')
    content = pickle.load(file)
    plan_no = int(input('Enter the plan number chosen: '))
    no = content[plan_no-1]
    x = no.pop()
    pickle.dump(content,temp)
    temp.close()
    file.close()
    os.remove('Room.dat')
    os.rename('temp2.dat','Room.dat')
    return(x)
    

#FUNCTION TO INITIATE THE BOOKING SEQUENCE

def Booking():
    file = open('Booking details.dat','ab+')
    global record
    pickle.dump(record,file)
    
    
    #WELCOME
    print('WELCOME TO HOTEL PROMETHEUS. PLEASE FOLLOW THE INSTRUCTIONS AND FILL IN THE REQUIRED DETAILS.')
    
    #PLAN DECISION
    Plans()
    plan_no = int(input('Enter the plan number you want: '))
    if plan_no > 5 or plan_no<1:
        print('Invalid plan number!!! Please start the procedure again.')
    else:
        n = int(input('Enter the number of days of your stay (If half day enter 1, if 1 and a half day enter 2 and so on): '))
        cost = n*plans[plan_no-1][2]
    
        #GUEST DETAILS
        people_name= []
        n = int(input('Enter the number of people staying: '))
        for i in range(n):
           name = input('Enter guest name: ')
           people_name.append(name)
        phone_no = int(input('Enter phone number: '))
        date = input('Enter the date of booking in the form YYYY-MM-DD: ')
        room_no=Rooms()
    
        #CONFIRMATION
        print('The booking sequence is complete.')
        print('PLAN CHOSEN: ',plans[plan_no-1][1])
        print('People staying: ')
        for i in people_name:
            print(i)
        print('PHONE NUMBER ENTERED: ',phone_no)
        print('TOTAL COST= Rs',cost)
        print('Room number: ',room_no)
        reply = input('Do you want to proceed? (yes/no): ')
        if reply == 'yes':
            record = [room_no,people_name,date,'Plan no '+str(plan_no),phone_no,cost]
            pickle.dump(record,file)
            print('Booking successful.')
        else:
            r = input('Do you want to restart? (yes/no) ')
            if r == 'yes':
                Booking()
            else:
                print('Please visit later!! You are always welcome!!')
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
            
            
 #FUNCTION TO INITIATE ROOM SERVICES

 
           
def Room_service():
    print('Welcome to room service menu. Room service stays open in the following timings:\n 6AM to 9AM \n 5PM to 6PM \n 8PM to 9PM')
    print('You can order anything from the general hotel menu. ')
    Menu_display()
    n = int(input('How many dishes do you want to order? : '))
    total_cost = 0
    food = []
    for i in  range(n):
        request = int(input("Enter the food item's number : "))
        number = int(input('Number of plates/items: '))
        cost= (number)*(Cost_list[request-1])
        total_cost+=cost
        food.append([Menu_list[request-1],number,cost],)
    else:
        print('Final bill: ')
        for i in food:
            for j in i:
                print(j,end='\t')
            print()
        print('GST = 5%')
        print('GST =',total_cost*0.05)
        print('Total cost =',total_cost*1.05)
        reply = input('Would you like to confirm your order? (yes/no): ')
        if reply == 'yes':
            print('Please pay the bill to the room service attendant. Thank you. Keep ordering.')
        else:
            reply = input('Would you like to order again? (yes/no): ')
            if reply == 'yes':
                Room_service()
            else:
                print('Thank you. Keep visiting.')


#FUNCTION TO INITIATE CHECK OUT SEQUENCE

def Check_out():
    file = open('Booking details.dat','rb')
    file2 = open('Room.dat','rb')
    temp = open('temp.dat','ab+')
    temp2 = open('temp2.dat','wb')
    people_name= []
    n = int(input('Enter the number of people staying: '))
    for i in range(n):
           name = input('Enter guest name: ')
           people_name.append(name)
    phone_no = int(input('Enter phone number: '))
    date = input('Enter the date of booking in the form YYYY-MM-DD: ')
    Room_no = int(input('Enter your room number: '))
    content = pickle.load(file)
    for i in content:
        if i[0]== Room_no:
            pass
        else:
            pickle.dump(i,temp)
    content = pickle.load(file2)
    if 0<Room_no<101:
        content[0]+=[Room_no]
    if 100<Room_no<201:
        content[1]+=[Room_no]
    if 200<Room_no<301:
        content[2]+=[Room_no]
    if 300<Room_no<401:
        content[3]+=[Room_no]
    if 400<Room_no<501:
        content[4]+=[Room_no]
    
    pickle.dump(content,temp2)
    file2.close()
    temp2.close()
    os.remove('Room.dat')
    os.rename('temp2.dat','Room.dat')
        
    file.close()
    temp.close()
    os.remove('Booking details.dat')
    os.rename('temp.dat','Booking details.dat')
    print('Check out successful. Keep visiting.')


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
    file = open('feedback.dat','ab')
    print('You have entered the feedback session.')
    feedback = input('Enter the feedback you would wish to give. It can be related to anything: ')
    pickle.dump(feedback,file)
    file.close()
    
#MAIN PROGRAM
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

