
def log_operation(func):

    def wrapper(*args, **kwargs):
        print("Starting operation:", func.__name__)

        result = func(*args, **kwargs)

        print("Operation completed:", func.__name__)

        return result

    return wrapper

