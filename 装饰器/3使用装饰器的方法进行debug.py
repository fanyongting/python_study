


def debug(func):
    def wrapper():
        print(f'[DEBUG]: run{func.__name__}()')
        return func()

    return wrapper


def say_hello():
    print("hello")


hello = debug(say_hello)
hello()




