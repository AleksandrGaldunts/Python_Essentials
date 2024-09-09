# def div(ls, b, index):
#     return ls[index] // b
#
#
# try:
#     ls = [1, 3, 4]
#     b = 0
#     index = 55
#     res = div(ls, b, index)
# # except IndexError as e:
# #     print(e)
# # except ZeroDivisionError as e:
# #     print("you cannot divide to 0")
# except (IndexError, ZeroDivisionError) as e:
#     print(e)
#     try:
#         res = div(ls, b, index)
#     except ZeroDivisionError:
#         print("nested try_except")
#     except IndexError:
#         print("nested index error")
#
# else:
#     print("else")
# finally:
#     print("finally")
#
# print("hello")#exceptionic heto coden sharunakvuma bnakanon hunov


               #raise exception
#
# class CustomException(Exception):
#     pass
#
# def foo():
#     raise CustomException
#
# try:
#     foo()
# except CustomException:
#     print("something")

def foo():
    raise

try:
    foo()
except ZeroDivisionError as e:
    print(e)
