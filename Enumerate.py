def enumerate_(iterable, start=0):
    for i in iterable:
        yield start,i
        start+=1

ls = [1,2,3,4,5,6,7]
x=enumerate_(ls)
print(list(x))
