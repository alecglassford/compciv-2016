from utils.geocoding import geocode

B_X = "\033[1m"
B_Z = "\033[0m"

the_command = input('What do you want to do? ')

if the_command == 'hello':
	usertext = input('What is your name? ')
	print('Hello', '{}{}{}'.format(B_X, usertext, B_Z))

elif the_command =='geocode':
	userlocation = input('What is your location? ')
	print('Ok...geocoding:', userlocation)
	georesult = geocode(userlocation)
	print(georesult)

elif the_command == 'help':
    print(geocode.__name__)
    print(geocode.__doc__)

else:
	print('Sorry, I don\'t know how to respond to', the_command)
