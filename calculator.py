def calculator(x,y,op):
	op_list = ['+','-','*','/','^']
	
	if op == '/':
		if y == 0:
			return 'Cannot divide by zero'
	result_list = [x+y,x-y,x*y,x/y,x**y]
	try:
		index = op_list.index(op)
	except:
		return "Invalid operator"

	return result_list[index]

def main():
	num1 = float(input('Enter the first number: '))
	num2 = float(input('Enter the second number: '))
	operation = input('Enter the operation: ')
	print(f'Result = {calculator(num1,num2,operation)}')

if __name__ == '__main__':
	main()