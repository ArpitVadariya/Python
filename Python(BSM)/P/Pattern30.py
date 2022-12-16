#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5


n = 6

for row in range(1, n):
    number = row
    for cols in range(0, n-row):
        print("  ", end="")
    for cols in range(0, row-1):
        print(number, end=" ")
        number-=1
    for cols in range(row-1, 2*row-1):
        print(number, end=" ")
        number+=1
    print()

print("--------------------------------")


row = 1
while(row < n):
    number = row
    cols = 0
    while(cols < n-row):
        print("  ", end="")
        cols+=1
    cols = 0
    while(cols < row-1):
        print(number, end=" ")
        number-=1
        cols+=1
    cols = row-1
    while(cols < 2*row-1):
        print(number, end=" ")
        number+=1
        cols+=1
    print()
    row+=1