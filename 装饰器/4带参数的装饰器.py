
def debug(func):

    def warpper(*args, **kwargs):
        print(f'[DEBUG]: run{func.__name__}()')
        return func(*args, **kwargs)

    return warpper


@debug
def say_hello():
    print("hello")


@debug
def test(a,b):
    print("a + b =",a+b)


say_hello()
test(1,2)
