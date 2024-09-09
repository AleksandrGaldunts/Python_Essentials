def counter(fn):
    count = 0
    def inner(*args):
        nonlocal count;
        count +=1
        print(count)
        return fn(*args)
    return inner

def decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"arguments positional are {args}")
        print(f"arguments keyword are {kwargs}")
        res = fn(*args, **kwargs)
        print(res)
        return res
    return wrapper
@counter
@decorator
def foo(x,y,z):
    print(x+y+z)

foo(5,6,7)
#
# @counter
# def bar(x,y,z=2):
#     print(x*y*z)
#
# bar(7,8)