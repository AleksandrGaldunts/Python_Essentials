def parz(x):
    if x == 0 or x == 1:
        print("Alen jan lav eli ")
    else:
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                return print("prime chi")
        else:
            return print("prime a")



x = int(input())
parz(x)
