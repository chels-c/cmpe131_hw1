counter = 0
def func_counter(func):
        def wrapper(*args):
                counter += 1
                func(*args)
        return wrapper()
