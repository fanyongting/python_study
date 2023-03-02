class logging:
    def __init__(self, level):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]:run {func}()".format(level=self.level, func = func.__name__))
            return func(*args, **kwargs)
        return wrapper


@logging(level='info')
def say(message):
    print(f'say: {message}')


say("hello")

