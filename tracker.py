def func_counter(func):
        def wrapper():
                counter += 1
                func()
        counter = 0
        return wrapper
