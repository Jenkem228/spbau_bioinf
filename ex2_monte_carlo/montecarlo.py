import multiprocessing as mp
from random import random
import time
from math import sin, pi


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


if __name__ == "__main__":
    with mp.Pool(processes=mp.cpu_count()) as pool:
        print("Считаем интеграл от функции sin(x^2) на отрезке [0, pi]")
        print("")
        N = 100000
        M = 100
        t0 = time.time()
        print("Время простого счета:")
        int_val = Calculus(N * M)
        print("Значение", int_val)
        t1 = time.time() - t0
        print("время", t1)
        t0 = time.time()
        int_val = sum(pool.map(Calculus, [N]*M)) / M
        print("Счет с мультипроцессингом", int_val)
        t2 = time.time() - t0
        print("время", t2)
        print("Распараллеливание даёт ускорение в", t2/t1, "раз")
        print("количество потоков", mp.cpu_count())


