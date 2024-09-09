ls = [1, 2, 3, 4]
ls2 = [5, 6, 7]
def mapp(function,*iterables):
    res = []
    min_len = len(iterables[0])
    for i in iterables[1:]:
        if min_len > len(i):
            min_len = len(i)
    for i in range(min_len):
        args = []
        tp=(iterator[i] for iterator in iterables)
        res.append(function(*tp))
    return res
res = mapp(lambda x,y: x+y,ls,ls2)
print(res)