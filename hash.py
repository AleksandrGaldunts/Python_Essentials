def hesh(int_str):
    gumar = 0
    g = 0
    if int_str == " ":
        return 0
    else:

        for i in int_str:
            gumar += ord(i)
            g += 1
    return gumar // g


x = input()
print(hesh(x))
