print("This program will convert and print the number of days into seconds by taking user input of days")
try:
    days = float(input("Enter the number of days: "))
    seconds = days*24*60*60 #Conversion factor
    print(days,"days when converted into seconds equals",seconds,"seconds.")
except Exception as e: # for any error cases
    print(e,"Please enter a valid number of days.")