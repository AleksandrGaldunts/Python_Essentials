# import inspect
# def custom_wraps(function):
#     def inner(inner):
#         inner.__name__=function.__name__
#         inner.__doc__ = function.__doc__
#         inner.__annotations__ = function.__annotations__
#         inner.__signature__ = inspect.signature(function)
#         return function
#     return inner
# def counter(function):
#     count = 0
#     #from functools import wraps
#     @custom_wraps(function)
#     def inner(*args,**kwargs):
#         nonlocal count
#         count+=1
#         print(count)
#         res = function(*args,**kwargs)
#         return res
#     # inner.__name__=function.__name__
#     # inner.__doc__ = function.__doc__
#     # inner.__annotations__ = function.__annotations__
#     # inner.__signature__ = inspect.signature(function)
#     return inner
#
#
# @counter
# def foo(x:int,y:int)->int:
#     '''docstring'''
#     return x+y
#
# foo(5,7)
# foo(5,7)
# foo(5,7)
# foo(5,7)
# print(foo(5,7))
# help(foo)


####### implement wraps ##########
# import inspect
# def custom_wraps(function):
#     def inner(wrapper):
#         wrapper.__name__=function.__name__
#         wrapper.__doc__ = function.__doc__
#         wrapper.__annotations__ = function.__annotations__
#         wrapper.__signature__ = inspect.signature(function)
#         return wrapper
#     return inner

# def counter(func):
#     count = 0
#     @custom_wraps(func)
#     def wrapper(*args,**kwargs):
#         nonlocal count
#         count+=1
#         print(f"Args is {args}")
#         print(f"kwargs is {kwargs}")
#         print(f"Our function calls {count} times")
#         res = func(*args,**kwargs)
#         return res
#     return wrapper
#
# def timer(func):
#     @custom_wraps(func)
#     def wrapper(*args,**kwargs):
#         import time
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         sub_time = end - start
#         print(f"our function takes {sub_time} to execute")
#         return result
#     return wrapper

# def memo(func):
#     cache = {}
#     @custom_wraps(func)
#     def wrapper(*args,**kwargs):
#         if args in cache.keys():
#             print("qeshic")
#             return cache[args]
#         else:
#             result = func(*args,**kwargs)
#             cache[args]=result
#             return result
#     return wrapper

#@memo
#@timer
#@counter
# def foo(x:int,y:int)->int:
#     '''This is annotations'''
#     # import time
#     # time.sleep(2)
#     print("some code will be seen here")
#     return x**y
#
# print(foo(5,3))
# print(foo(5,3))
# print(foo(5,3))
# print(foo(5,3))
# print(help(foo))




















