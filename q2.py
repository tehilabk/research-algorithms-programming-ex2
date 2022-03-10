previous_input = {} #global var with last input

def lastcall(func: callable):
    def inner(*args):
        global previous_input
        if previous_input == args: #if input the same
            return f"I already told you that the answer is {func(*args)}"
        else:  #else if changed
            previous_input = args
            return func(*args)

    return inner


@lastcall
def f1(x: int):
    return x ** 2


@lastcall
def f2(x: int):
    return x+2

@lastcall
def sort(x):
    return sorted(x)