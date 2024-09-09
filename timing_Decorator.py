import time


def timed(origin):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = origin(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"function name is {origin.__name__}")
        print(f"function duration is {end:.6f}s")
        return result

    return wrapper



def fac_rec(n):
    return 1 if n == 0 else n * fac_rec(n - 1)

@timed
def fac_iter(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

@timed
def recursion(n):
    return fac_rec(n)

fac_iter(500)
recursion(500)
