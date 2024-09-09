def zipp(*iterables,strict=0):
    size = min(len(i) for i in iterables)
    for i in range(size):
        yield tuple(iterable[i] for iterable in iterables)

x = zipp([1,2,3,4],[1,2,3])
print(list(x))
