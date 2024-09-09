def filter_(function,iterable):
    "I implement filter"
    if function is None:
        for i in iterable:
            if bool(i):# aysinqn vori cast y true tpelu vory che che
                yield i
    else:
        for i in iterable:
            if function(i):# ete mer function y kanchac i ov true a ktpi
                yield i
x = filter_(lambda x: x%2,[1,2,3,4,5])
print(list(x))