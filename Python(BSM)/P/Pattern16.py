#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1


n = 5

for row in range(0, n):
    for cols in range(0, n-row-1):
        print("  ", end="")
    for cols in range(0, row):
        number = str(11**row)
        print(number[cols], end="   ")
    for cols in range(0, 1):
        print("1", end="")
    print()


print("---------------------------------------")

row = 0

while(row < n):
    cols = 0
    while(cols < n-row-1):
        print("  ", end="")
        cols+=1
    
    cols = 0
    while(cols < row):
        number = str(11**row)
        print(number[cols], end="   ")
        cols+=1

    cols = 0
    while(cols < 1):
        print("1", end="")
        cols+=1

    row+=1
    print()