class Helper:
	def __init__(self):
		self.first_initial = 6000
		self.second_initial = 16000
		self.first_net = 30000
		self.second_net = 100000
		self.n_times = 10

	def get_net(self, growth):
		if growth <= self.first_net:
			net = growth
		elif self.first_net < growth <= self.second_net:
			net = (0.8 * growth) + self.first_initial
		else:
			net = (0.7 * growth) + self.second_initial
		return net

	def get_growth(self, net):
		if net <= self.first_net:
			growth = net
		elif self.first_net < net <= 86000:
			growth = (net - self.first_initial) / 0.8
		else:
			growth = (net - self.second_initial) / 0.7
		return round(growth, 0)

	@staticmethod
	def multiply_square(n):
		print(f'Multiplier square from 1 to {n}')
		for i in range(1, n):
			print(f'{i} x {i} = {pow(i, 2)}\n')

	def multiplication_table(self, n):
		for i in range(1, n+1):
			self.n_multiply(i)
			
	def n_multiply(self, number):
		print(f'Multiply by {number}')
		print('________________')
		for j in range(1, self.n_times+1):
			print(f'{number} x {j} = {number*j}')
		print('================')
		
	@staticmethod
	def n_dividers(number):
		# print(f'All dividend of {number}')
		dividers = []
		for i in range(2, number-1):
			if number % i == 0:
				dividers.append(i)
				# print(f'{number} : {i} = {number/i}')
		# print(f'Dividers: {dividers}')
		return dividers
		
		
helpers = Helper()
