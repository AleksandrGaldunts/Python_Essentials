# 2 akani meji 1 eri  qanak
# def count1(num):
#     count = 0
#     while(num):
#         count += num & 1
#         num >>= 1
#     return count
#
# print(count1(5))

# def count0(num):
#     count = 0
#     while num:
#         if (num & 1) == 0:
#             count +=1
#         num >>= 1
#     return count
# print(count0(5))


# def power2(num):
#     if num & (num - 1) == 0:
#         print("2֊ի աստիճանա")
#     else:
#         print("2-ի աստիճան չի")


# def power4(num):
#     if (num & (num - 1) == 0) and (num - 1) % 3 == 0:
#         print("4֊ի աստիճանա")
#     else:
#         print("4-ի աստիճան չի")

# ''' 2-րդ եղանակ

# def astjan4(num):
#     if num <= 0:
#         return False

#     if num & (num - 1) == 0 and num & 0x55555555:
#         return True
#     return False

# '''


# def gumarum(a, b):

#     while b != 0:
#         carry = a & b
#         a = a ^ b
#         b = carry << 1
#     return a


# def sub (a,b):
#     flag = 0
#     if a < b:
#         a ^= b
#         b ^= a
#         a ^= b
#         flag += 1
#     while b:
#         carry = (~a) & b
#         a = a ^ b
#         b = carry << 1
#     return  -a if flag == 1 else a


# str-i uniq-ությունա ստուգում

# st = "hello"
# flag = 0
# for i in st:
#     pos = ord(i)
#     if flag & (1 << pos) > 0:
#         print("false")
#         break
#     flag = flag | (1 << pos)
# else:
#     print("done")


# def foo(num, size_num):
#     tmp = (num << size_num) & num
#     tmp1 = num & 1
#     if tmp1 == tmp:
#         return True
#     return False

# import sys
# num = int(input())
# size = sys.getsizeof(num)
# print(size)
# print(foo(num, size))


# def foo(num, i, j):
#     tmp_i = num & (1 << i)
#     tmp_j = num & (1 << j)
#     if tmp_i != tmp_j:
#         num ^= (1 << i)
#         num ^= (1 << j)
#     return num
# print(foo(10, 0, 1))


# def foo(num):
#     i = 31
#     j = 0
#     while j < i:
#         tmp_i = bool(num & (1 << i))
#         tmp_j = bool(num & (1 << j))
#         if tmp_i != tmp_j:
#             num ^= (1 << i)
#             num ^= (1 << j)
#         i -=1
#         j +=1
#     return num
# print(foo(43261596))


# def tiv(num):
#     if num ==0:
#         return 'Binary code:  0b0'
#     ls = []
#     while num:
#         ls.append(str(num % 2))
#         num //=2
#     return 'Binary code:  0b' + ''.join(ls[::-1])
# num = int(input())
# print(tiv(num))




