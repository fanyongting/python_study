def log(level):
    def wrapper(func):
        def inwrapper(*args, **kwargs):
            print(f'[DEBUG][{level}]:{func.__name__}')
            return func(*args, **kwargs)

        return inwrapper

    return wrapper


@log(level='info')
def say_hello(message):
    print(f'say {message}')


say_hello("hi 装饰器")
