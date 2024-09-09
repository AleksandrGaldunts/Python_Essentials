# #reverse matrix
#
#
# matrix = [[3*j + x for x in range(1,4)] for j in range(3)]
# for i in range(len(matrix)):
#     print(matrix[i])
# print()
#
# matrix = [x[::-1] for x in matrix]
# print(matrix)
#
# matrix = matrix[::-1]
# print(matrix)
#
# for row in matrix:
#     print(row)



#  ankyunagci tarreri gumar


#
# matrix  = [[3*j + x for x in range(1,4)] for j in range(3)]
# gumar_glxavor = sum(matrix[i][i] for i in range(3))
# ojandak_gumar = sum(matrix[i][-1-i] for i in range(3))
# for row in matrix:
#     print(row)
# print(ojandak_gumar,gumar_glxavor)

# ojandakic ներքև տարրերի գումար


# matrix = [[3*j+x for x in range(1,4)] for j in range(3)]
# n = len(matrix)
# ANTI_dioganal_main_below = sum(matrix[i][j] for i in range(n) for j in range(n) if j > n - 1 - i)
# for row in matrix:
#     print(row)
# print(ANTI_dioganal_main_below)



# ojandak վերև տարրերի գումար


matrix = [[3*j+x for x in range(1,4)] for j in range(3)]
n = len(matrix[1])
sum_above_anti_diag = sum(matrix[i][j] for i in range(n) for j in range(n - i - 1))
print(sum_above_anti_diag)



#  գլխավորից վերև տարրերի գումար


# matrix = [[3*j+x for x in range(1,4)] for j in range(3)]
# sum_above_main_diag = sum(matrix[i][j] for i in range(len(matrix)) for j in range(i+1, len(matrix[i])))
# print(sum_above_main_diag)

# գլխավորից ներքև տարրերի գումար

"""
matrix = [[3*j+x for x in range(1,4)] for j in range(3)]
below_diagonal_sum = sum(matrix[i][j] for i in range(len(matrix)) for j in range(i) if j < i)
"""

# գլխավոր անկյունագիծ և վերև տարրերի գումար

"""
matrix = [[3*j+x for x in range(1,4)] for j in range(3)]
print(sum(matrix[i][j] for i in range(len(matrix)) for j in range(i, len(matrix[i]))))

"""

#  գլխավոր անկյունագիծ և ներքև տարրերի գումար

"""

matrix = [[3*j+x for x in range(1,4)] for j in range(3)]
print(sum(matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])) if i >= j))

"""

# օժանդակ անգյունագիծ և ներքև տարրերի գումար

"""

matrix = [[3*j+x for x in range(1,4)] for j in range(3)]
print(sum(matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])) if len(matrix)<= i + 1 + j))

"""

# օժանդակ անգյունագիծ և վերև տարրերի գումար

#
# matrix = [[3*j+x for x in range(1,4)] for j in range(3)]
# print(sum(matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])-i))) #if j <= len(matrix) - 1 - i))
#

# matrix transpose


#
# matrix = [[3*j+x for x in range(1, 4)] for j in range(3)]
# transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# for row in matrix:
#     print(row)
#
# print()
# for row in transpose:
#     print(row)


# 90 աստիճան



matrix = [[3*j+x for x in range(1, 4)] for j in range(3)]
for i in matrix:
    print(i)
print()
transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for i in transposed_matrix:
    print(i)
print()

rotated_matrix_90_clockwise = [row[::-1] for row in transposed_matrix]
for i in rotated_matrix_90_clockwise:
    print(i)



# matrix = [[3 * x + i for i in range(1, 4)] for x in range(3)]
#
# for i in range(3):
#     for j in range(3):
#         if i == j:
#             matrix[i][j] = 0
#         if j > i:
#             matrix[i][j] = 1
#         if j < i:
#             matrix[i][j] = 2
# for row in matrix:
#     print(row)

# matrix = [[3*x + i for i in range(1, 4)]for x in range(3)]
# transpose = [[matrix[i][j] for i in range(3)] for j in range(3)]
# mat = [row[::-1] for row in transpose]


# matrix = [[3 * x + i for i in range(1,4)] for x in range(3)]
# transpose = [[matrix[i][j] for i in range(3)] for j in range(3)]
# reverse = [row[::-1] for row in matrix]
# reverse = reverse[::-1]

# for  row in reverse:
#     print(row)

# print()
# for  row in transpose:
#     print(row)

# matrix = [[3 * j + i for i in range(1,4)] for j in range(3)]
# for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if j >= i:
#                 matrix[i][j] = 2

# for row in matrix:
#     print(row)

# matrix = [[3 * x + i for i in range(1,4)] for x in range(3)]
# transpose = [[matrix[i][j] for i in range(len(matrix))]for j in range(len(matrix))]
# for a in transpose:
#     print(a)


# grade = [row[::-1] for row in transpose]
# print(grade[::-1])