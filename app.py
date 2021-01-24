from utils.helpers import helpers

print("Hi $USER, Welcome to AKIMANA Math Play ground")
message = """
Choose among the choices below to calculate:\n
1. Growth salary\n
2. Net salary
Enter your choice: """
try:
	choice = input(message)
	selected = 'net' if choice == '1' else 'growth'
	if int(choice) < 3:
		amount_entered = int(input(f'Enter your {selected} salary: '))
		if choice == '1':
			amount_wanted = helpers.get_growth(net=amount_entered)
		elif choice == '2':
			amount_wanted = helpers.get_net(growth=amount_entered)

		warning_message_1 = f'From this amount: {amount_entered}, there might be some extra charges'
		warning_message_2 = 'Please refer to the Employer quotation.'
		print(f'The calculated {selected} money is {amount_wanted}')
		print(warning_message_1)
		print(warning_message_2)
	else:
		print('This is a Math playground')
		print('=======================')
		choice_message = """
		1.Multiplication table.
		2.Dividends.
		3.Square table.
		Enter your choice:
		"""
		math_choice = int(input(choice_message))

		if math_choice == 1:
			table_number = int(input('Enter multiplier number: '))
			helpers.multiplication_table(table_number)
		elif math_choice == 2:
			number = int(input('Type a number you want to find its dividers: '))
			dividers = helpers.n_dividers(number)
			print(f'Di vi de nts {dividers}')
		else:
			last_square_number = int(input('Enter last square number: '))
			helpers.multiply_square(last_square_number)
except Exception as exc:
	print(f"Oops something is wrong: {str(exc)}")
