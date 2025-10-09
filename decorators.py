# Made by Prof. Daryll Ko (not mine)

from time import sleep


def show_call_stack(fun):
    def superfun(*args):
        call = f"{fun.__name__}({', '.join(map(str, args))})"

        print(f"START\t{call}")
        sleep(0.5)

        res = fun(*args)

        print(f"END\t{call}")
        sleep(0.5)

        return res

    return superfun


def show_calls(fun):
    def superfun(*args):
        call = f"{fun.__name__}({', '.join(map(str, args))})"

        print(call)
        sleep(0.5)

        return fun(*args)

    return superfun