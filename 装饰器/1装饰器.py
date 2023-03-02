import inspect


def debug():
    call_name = inspect.stack()[1][3]
    print("[DEBUG]:enter {}()".format(call_name))


def say_hello():
    debug()
    print("hello")


def say_goodbye():
    debug()
    print("goodbye")

if __name__ == '__main__':
    say_hello()
    say_goodbye()
