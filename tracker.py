def func_counter(func):
        counter = 0
        def wrapper(*args):
                counter += 1
                func(*args)
        return wrapper()
