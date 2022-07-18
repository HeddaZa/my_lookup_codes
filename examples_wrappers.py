def print_return_type(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        print('{}() returned type {}'.format(func.__name__, type(result)))
        return result
    return wrapper


@print_return_type
def foo(value):
    return value
print(foo(42))

def timer(func):
    """A decorator that prints how long a function took to run."""  
    def wrapper(*args, **kwargs):
        t_start = time.time()
    
        result = func(*args, **kwargs)
    
        t_total = time.time() - t_start
        print('{} took {}s'.format(func.__name__, t_total))
    
        return result
    return wrapper
@timer
def sleep_n_seconds(n=10):
    """Pause processing for n seconds.
  
    Args:
        n (int): The number of seconds to pause for.
    """
    time.sleep(n)
print(sleep_n_seconds.__doc__)

from functools import wraps

def add_hello(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)
    return wrapper
@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)
print_sum(10,20)

def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
@run_n_times(3)
def print_sum(a, b):
    print(a + b)
@run_n_times(5)
def print_hello():
    print('Hello!')
    
print_sum(3,5)
print_hello()