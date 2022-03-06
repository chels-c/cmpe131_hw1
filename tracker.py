def func_counter(func(x)):
        counter = 0
        def wrapper(x):
                counter += 1
                func(x)
        return wrapper(x)
