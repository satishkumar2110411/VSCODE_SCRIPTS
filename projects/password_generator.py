from random import choice

def strength_check(pswd_temp):
	strength = bool('A' in pswd_temp)*(pswd_temp.count('A'))+bool('a' in pswd_temp)*(pswd_temp.count('a')) + bool('0' in pswd_temp)*(pswd_temp.count('0')) + bool('@' in pswd_temp)*(pswd_temp.count('@'))
	if 0<=strength<=3:
		return 'Weak'
	elif 3<strength<=6:
		return 'Moderate'
	elif 6<strength<=10:
		return 'Strong'
	else:
		return 'Very Strong'

def main():		
	uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	lowercase = 'abcdefghijklmnopqrstuvwxyz'
	numbers = '9876543210'
	characters = "'`~!@#$%^&*()-_=+[]|;:,.<>/?\"" + '{' + '}'

	template = str(input("Enter the structure of your passsword \nEg: if you want a password like Ab23@# then type Aa00@@ \nA-uppercase letter\na-lowercase letter\n0-digit\n@-character\nEnter password structure: "))
	password = ''
	template_value = {'A':uppercase,'a':lowercase,'0':numbers,'@':characters}
	for i in template:
		password += choice(template_value[i])

	print('Your generated password is ',password)
	print(f'Estimated strength of your password structure: {strength_check(template)}')

if __name__ == '__main__':
	main()