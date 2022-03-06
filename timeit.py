import time

def calculate_time(func):
        def wrapper():
                func()
                print('Total time ', time.time())
        return wrapper

	
