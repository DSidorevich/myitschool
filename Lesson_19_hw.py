def debug(func):
    def wrapper(*args):
        print(f'Function name: {func.__name__}. Name of arguments: {args}')
        print(f'The result of decorated function:')
        func(*args)
        print('The program is finished.')
    return wrapper


@debug
def my_function(a, b, c):
    print((a + b) * c)


my_function(5, 7, 4)


