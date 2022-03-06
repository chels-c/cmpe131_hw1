def func_counter(func):
	counter += 1
	def wrapper():
		func()
	return wrapper
	


