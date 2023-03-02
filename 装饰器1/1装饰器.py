

def log(level):
    def wrapper(func):
        def inwrapper(*args, **kwargs):
            print(f"[DEBUG] [{level}]: run {func.__name__}")
            return func(*args, **kwargs)
        return inwrapper
    return wrapper



def say(message):
    print(f"说了：{message}")