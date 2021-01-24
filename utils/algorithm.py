from functools import reduce


def gcm(num1, num2):
	while num1 != num2:
		if num1 > num2:
			num1 = num1 - num2
		else:
			num2 = num2 - num1
	return num2


def lcm(num1, num2):
	their_gcm = gcm(num1, num2)
	return (num1 * num2) / their_gcm


def list_sum():
	try:
		the_list = []
		tot_num = int(input('How many: '))
		for i in range(1, tot_num+1):
			cur_num = int(input(f"Number {i}:"))
			the_list.append(cur_num)
		
		return list(sorted(lambda a: a % 3 == 0, the_list))
	except Exception as exc:
		print(str(exc))
