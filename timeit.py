import time

def calculate_time(func):
	def wrapper():
		print('Total time', end = ' ' )
		func()
	return wrapper

def totalTime(): 
	print(time.time())

totalTime = calculate_time(totalTime)
totalTime()

	
