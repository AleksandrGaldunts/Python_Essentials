def filtr(func, ls):
    if func == None:
        for i in ls:
            if bool(i):
                yield i
    else:
        for i in ls:
            yield (func(i))

#x = list(filtr(lambda x : x * 2  , [1,2,3]))
x = list(filtr(None, [2, 0, 5, 4, 0, 4]))
print(x)
