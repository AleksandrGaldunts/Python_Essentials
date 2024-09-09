
def create_counter(start=0):

    di = {'value': start}

    def inc(step=1):
        try:
            di['value'] += step
        except TypeError as e:
            print(e)
    def dec(step=1):
        try:
            di['value'] -= step
        except TypeError as e:
            print(e)

    def get_counter_value():
        return di['value']

    return inc, dec, get_counter_value


inc, dec, get_counter_value = create_counter()

inc('52')
print(get_counter_value())

dec(7)
print(get_counter_value())

inc(10)
print(get_counter_value())

dec(2)
print(get_counter_value())

inc(4)
print(get_counter_value())