
# # def outer(function):
# #     di = {}
# #     def inner(*args, **kwargs):
# #         num = args[0]
# #         if num in di:
# #             return di[num]
# #         else:
# #             res = function(num)
# #             di[num] = res
# #             print(di)
# #             return res
# #     return inner


# # @outer
# # def faktorial(num):
# #     if num <= 1:
# #         return num
# #     return num * faktorial(num-1)
# # print(faktorial(5))
# # print(faktorial(4))
# # print(faktorial(2))




# def decor(func):
#     def wrapper(*args,**kwargs):
#         import time
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time() - start
#         print(end)
#         return res
#     return wrapper

# # @decor
# def fact(num):
#     if num < 0:
#         return -1
#     if num <= 1:
#         return num
#     return num * fact(num-1)



# # @decor
# def fibo(num):
#     if num <= 1:
#         return num
#     return fibo(num - 1) + fibo(num - 2)

# @decor
# def recur(n):
#     return fact(n)
# @decor
# def fib(n):
#     return fibo(n)

# recur(10)
# fib(10)











# # # def decor(func):
# # #     di = {}
# # #     di[0] = 1
# # #     def wrapper(num):
# # #         if num in di:
# # #             return di[num]
# # #         res = func(num)
# # #         di[num] = res
# # #         print(di)
# # #         return res
# # #     return wrapper

# # # @decor
# # # def fact(num):
# # #     if num < 0:
# # #         return -1
# # #     if num <= 1:
# # #         return num
# # #     return num * fact(num-1)

# # # @decor
# # # def fibo(num):
# # #     if num <= 1:
# # #         return num
# # #     return fibo(num - 1) + fibo(num - 2)



# def foo(n):
#     def foo1(m):
#         return m * n
#     return foo1
#
# res = foo(5)
# print(res(4))