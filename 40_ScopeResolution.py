# 40. Scope Resolution

# In order (LEBG) : Local -> Enclosed -> Global -> Build-in

from math import e

gloval_var = 10  # Global variable


def func1():
    x = 1  # Local variable of func1()

    def inner_func():

        print(f"inner_func: x = {x}")  # using enclosing variable x from func1()

    inner_func()


def func2():
    print(f"func2: gloval_var = {gloval_var}")  # using global variable


def func_e():
    print(e)  # using build-in varible


func1()
func2()
func_e()
