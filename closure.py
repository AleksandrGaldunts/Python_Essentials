def esim():
    a = 0
    def hashvich():
        nonlocal a
        a += 1
        return a
    return hashvich



count = esim()


print(count())
print(count())