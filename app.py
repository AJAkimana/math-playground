from utils.helpers import helpers

print("Hi $USER, Welcome to RWANDA salary calculator")
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
		choice_message = '1. Multiplication table.\n2.Square table\n Enter your choice: '
		math_choice = int(input(choice_message))

		if math_choice == 1:
			table_number = int(input('Enter multiplier number: '))
			helpers.multiplication_table(table_number)
		else:
			last_square_number = int(input('Enter last square number: '))
			helpers.multiply_square(last_square_number)
except Exception as exc:
	print(f"Oops something is wrong: {str(exc)}")
