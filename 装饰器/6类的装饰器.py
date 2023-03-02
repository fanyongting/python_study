class test:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[DEBUG] [level]: enter the function {func}".format(func = self.func.__name__))
        return self.func(*args, **kwargs)


@test
def say_hello():
    print("hello")


say_hello()

