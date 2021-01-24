from utils import algorithm

welcome_msg = """
Welcome to data structure
"""
print(welcome_msg)
is_go = True
while is_go:
	try:
		intro_msg = """
		1. Array manipulation
		2. Data manipulation
		"""
		choice = int(input(intro_msg))
		if choice == 1:
			print("Manipulation of array")
			print(algorithm.list_sum())
		elif choice == 2:
			print("Data manipulation")
			fi = int(input('Enter num 1: '))
			se = int(input('Enter num2: '))
			print(f"GCM of {fi} and {se} is {algorithm.gcm(fi, se)}")
			print(f"LCM of {fi} and {se} is {algorithm.lcm(fi, se)}")
		elif choice == 0:
			is_go = False
		else:
			print('Invalid option')
	except Exception as exc:
		print(f"Something went wrong:{str(exc)}")
		is_go = False
