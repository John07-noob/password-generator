# Author	: John07-noob
# Date		: Sep/7/2020 (Up/Nov8/2020)
import random

class User:
	def __init__(self, passwd_range):
		self.passwd_range = passwd_range

	def alpha(self):
		alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		return "".join(random.choice(alpha) for i in range(self.passwd_range))

	def num(self):
		num = "0123456789"
		return "".join(random.choice(num) for i in range(self.passwd_range))

	def superpass(self):
		superpass = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%()[]~'"
		return "".join(random.choice(superpass) for i in range(self.passwd_range))

def num_input(user_input):
	while True:
		try:
			user_input = int(input(user_input))
		except ValueError:
			print("Just Number!")
			continue
		else:
			return user_input

if __name__=='__main__':
	print("Welcome to Password Generator")
	print("1.Just Alphabet")
	print("2.Just Number")
	print("3.Alphabet, Number & Character")
	while True:
		chooice = input("Insert Here: ")
		if chooice == "1":
			passwd_range = num_input("How long you want: ")
			user = User(passwd_range)
			result = user.alpha()
			print(f"The Result: {result}")
			break
		elif chooice == "2":
			passwd_range = num_input("How long you want: ")
			user = User(passwd_range)
			result = user.num()
			print(f"The Result: {result}")
			break
		elif chooice == "3":
			passwd_range = num_input("How long you want: ")
			user = User(passwd_range)
			result = user.superpass()
			print(f"The Result: {result}")
			break
		else:
			print("Invalid Command!")
