#25: Inverted Pyramid of Numbers
# 1 1 1 1 1 
#  2 2 2 2 
#   3 3 3 
#    4 4 
#     5
rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    print(' ' * (i - 1), end='')
    print(f"{i} " * (rows - i + 1))

#26: Half Pyramid Pattern of Numbers
#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5
rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    print(' ' * (rows - i) * 2, end='')
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

#27: Inverted Half Pyramid Number Pattern
# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1
rows = int(input("Enter rows: "))
for i in range(rows, 0, -1):
    for j in range(i):
        print(j, end=' ')
    print()

#28: Unique Pyramid Pattern of Digits
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1
rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    for j in range(i - 1, 0, -1):
        print(j, end=' ')
    print()

#29: Pyramid of Horizontal Tables
# 0  
# 0 1  
# 0 2 4  
# 0 3 6 9  
# 0 4 8 12 16  
# 0 5 10 15 20 25  
# 0 6 12 18 24 30 36
rows = int(input("Enter rows: "))
for i in range(rows):
    for j in range(i + 1):
        print(i * j, end=' ')
    print()

#30: Equilateral Triangle with Stars (Asterisk Symbol)
#         *   
#        * *   
#       * * *   
#      * * * *   
#     * * * * *   
#    * * * * * *   
#   * * * * * * *
rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    print(' ' * (rows - i), end='')
    print('* ' * i)