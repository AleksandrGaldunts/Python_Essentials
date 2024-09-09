# def academy_zip(*iterables, strict=False):
#   '''
#     The zip function yields n-length tuples, where n is the number of iterables passed
#     as positional arguments to zip(). The i-th element in every tuple comes from the i-th
#     iterable  argument to zip(). This continues until the shortest argument is exhausted.
#     zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.
#   '''
#   iterators = [iter(iterable) for iterable in iterables]
#   while True:
#     try:
#       current_tuple = tuple(next(iterator) for iterator in iterators)
#       yield current_tuple
#     except StopIteration:
#       return


# def academy_map(func, *iterables):
#   '''
#     Make an iterator that computes the function using arguments from
#     each of the iterables. Stops when the shortest iterable is exhausted.
#     map(func, *iterables) --> map object
#   '''
#   iterators = [iter(iterable) for iterable in iterables]
#   while True:
#     try:
#       current_tuple = [next(iterator) for iterator in iterators]
#       yield func(*current_tuple)
#     except StopIteration:
#       return

# ls = academy_map(lambda x, y: x + y, [1, 2, 3], [1, 2])


# def academy_enumerate(iterable, start = 0):
#   '''
#     The enumerate object yields pairs containing a count (from start, which defaults to zero)
#     and a value yielded by the iterable argument.
#     enumerate(iterable, start=0)
#   '''
#   for item in iterable:
#     yield start, item
#     start += 1


# def academy_filter(func, iterable):
#   '''
#     Return an iterator yielding those items of iterable for which function(item)
#     is true. If function is None, return the items that are true.
#     filter(function or None, iterable) --> filter object
#   '''
#   if func is None:
#     filtered_items = [it for it in iterable if bool(it)]
#   else:
#     filtered_items = [it for it in iterable if func(it)]
#   for item in filtered_items:
#     yield item


# def academy_reduce(func, iterable, initial = None):
#   '''
#     Apply a function of two arguments cumulatively to the items of a sequence
#     or iterable, from left to right, so as to reduce the iterable to a single
#     value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#     ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
#     of the iterable in the calculation, and serves as a default when the
#     iterable is empty.
#   '''
#   iterator = iter(iterable)
#   if initial is None:
#     try:
#       initial = next(iterator)
#     except TypeError:
#       raise 'reduce() of empty iterable with no initial value'

#   result = initial
#   for item in iterator:
#     result = func(result, item)

#   return result


# def your_map(func, *iterables):
#     it = [iter(i) for i in iterables]
#     while True:
#         try:
#             ls = [next(iterator) for iterator in it]
#             yield func(*ls)
#         except StopIteration:
#             return


# def your_map(func, *iterables):
#     it = [iter(i) for i in iterables]
#     while True:
#         try:
#             ls = [next(iterator) for iterator in it]
#             yield func(*ls)
#         except StopIteration:
#             return

# ls = your_map(lambda x, y, z: z + x + y, [1, 2, 3, 7], [2,3,4,5], [7,5,3,3])
# print(list(ls))


# def my_map(func, *iterables):
#     size = min(len(x) for x in iterables)
#     for i in range(size):
#         yield(func(*(x[i] for x in iterables)))

# def your_map(func, *iterables):
#     it = [iter(i) for i in iterables]
#     while True:
#         try:
#             ls = [next(i) for i in it]
#             yield func(*ls)
#         except StopIteration:
#             return
# ls = my_map(lambda x, y, z: z + x + y, [1, 2, 3, 7], [2,3,4,5], [7,5,3,3])
# print(list(ls))

