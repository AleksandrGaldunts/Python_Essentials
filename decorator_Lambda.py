# # Define a decorator factory using a lambda function
# create_decorator = lambda func: (lambda decorator_func: (lambda *args, **kwargs: decorator_func(func, *args, **kwargs)))
#
# # Use the decorator factory to create a decorator
# decorator = create_decorator(lambda original_func, *args, **kwargs: (
#     lambda *func_args, **func_kwargs: original_func(*func_args, **func_kwargs) + sum(args) + sum(func_args) + kwargs.get('extra', 0)
# ))
#
# # Apply the decorator to a function using a lambda function
# @decorator
# def my_function(a, b):
#     return a + b
#
# # Test the decorated function
# result = my_function(1, 2)
# print(result)  # Output will be 1 + 2 + 1 + 2 + 0 = 6
