print('This program will give the simple interest for given inputs.')
def S_I(principle,interest,time):
    simple_interest = (principle*interest*time)/100
    return(simple_interest)

if __name__ == "__main__":
    principle = float(input('Enter principle value: '))
    interest = float(input("Enter rate of interest percentage: "))
    time = float(input('Enter the number of years: '))

    print('The simple interest for is: Rs',S_I(principle,interest,time))
