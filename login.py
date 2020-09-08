import json

#functions

def SignUp(username, password):
	with open('data.json','r')as f:
		data = json.load(f)
	
	if username in data:
		print('Username has been taken! \n')
		username = input('Username: ')
	else:
		data[str(username)] = password
		with open('data.json', 'w')as f:
			json.dump(data, f, indent=4)
			
def login(username, password):
	with open('data.json', 'r')as f:
		data = json.load(f)
	
	try:
		if username in data:
			if password == data[str(username)]:
				print('Login successful!')
			else:
				print('Password incorrect')
		elif username not in data:
			print('username not found')
	except:
		print('username not found')


#main
choice = str(input('1. Sign Up \n2.Login \n'))

if choice == "1":
	username = str(input('Username: '))
	password = str(input('Password: '))
	SignUp(username, password)
elif choice == "2":
	username = str(input('Username: '))
	password = str(input('Password: '))
	login(username, password)
else:
	print('Invalid choice!')
