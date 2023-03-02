def debug(func):
    def wrap():
        print(f'[DEBUG]: run{func.__name__}()')
        return func()

    return wrap


@debug
def say_hello():
    print("hello")


say_hello()
