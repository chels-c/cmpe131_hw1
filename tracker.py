def func_counter(func):
        counter = 0
        def wrapper():
                counter += 1
                func()
        return wrapper()
