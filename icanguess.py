import time

print("Welcome to")

time.sleep(1)

print("I CAN GUESS")

time.sleep(1)

print("\nPRESS ENTER")

user = input()

print("\nThink on a number from 1 to 5.\n \nPress enter when you are ready.")

user = input()

print("\nIs your number 1, 2 or 3?")

user = input("[Y] Yes       [N] No\n")

if user == "n" or user == "N":
	
	print("\nIs your number 2, 3 or 4?")
	
	user = input("[Y] Yes       [N] No\n")
	
	if user == "y" or user == "Y":
		print("Your number is 4.")
	
	elif user == "n" or user == "N":
		print("Your number is 5.")
		
elif user == "y" or user == "Y":
	
	print("\nIs your number 2, 3 or 4?")
	
	user = input("[Y] Yes       [N] No\n")
	
	if user == "n" or user == "N":
		
		print("Your number is 1.")
		
	elif user == "y" or user == "Y":
		
		print("\nIs your number 3, 4 or 5?")
		
		user = input("[Y] Yes       [N] No\n")
		
		if user == "y" or user == "Y":
			print("Your number is 3.")
		
		elif user == "n" or user == "N":
			print("Your number is 2.")
			
print("\nMade by JCionx \nVersion 1.0")