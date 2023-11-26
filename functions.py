class Cat:
    def __init__(self, name) -> None:
        self.name = name
    # method
    def meow(self):
        print(f'{self.name} meows!')

# function
def foo():
    print('bar')

# anonymous function
add = lambda x, y: x + y

# recursive function
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)