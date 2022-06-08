from random import random
import time
from math import sin, pi
from numba import njit

def func(x):
    return sin(x*x)

def randomfloat(a, b):
    return random() * (b-a) + a

def MonteCarloInt(a, b, f ,n):
    s = 0
    for i in range(n):
        s += f(randomfloat(a, b))
    return s * ((b - a) / n)

def Calculus(n):
    return MonteCarloInt(0, pi, func, n)

@njit()
def func_jit(x):
    return sin(x*x)

@njit()
def randomfloat_jit(a, b):
    return random() * (b-a) + a

@njit()
def MonteCarloInt_jit(a, b, f ,n):
    s = 0
    for i in range(n):
        s += f(randomfloat_jit(a, b))
    return s * ((b - a) / n)

@njit()
def Calculus_jit(n):
    return MonteCarloInt_jit(0, pi, func_jit, n)


if __name__ == "__main__":
        print("Считаем интеграл от функции sin(x^2) на отрезке [0, pi]")
        print("")
        N = 100000000
        t0 = time.time()
        print("Время простого счета:")
        int_val = Calculus(N)
        print("Значение", int_val)
        t1 = time.time() - t0
        print("время", t1)
        t0 = time.time()
        int_val = Calculus_jit(N)
        print("Счет с Numboй", int_val)
        t2 = time.time() - t0
        print("время", t2)
        print("Numba даёт ускорение в", t1/t2, "раз")


