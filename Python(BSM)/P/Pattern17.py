#      1
#     212
#    32123
#   4321234
#    32123
#     212
#      1


n = 6

for row in range(0, int(n/2+1)):
    number = row
    for cols in range(0, n-row):
        print(" ", end="")
    for cols in range(0, row):
        print(number, end="")
        number-=1
    number = 2
    for cols in range(1, row):
        print(number, end="")
        number+=1
    print()

for row in range(int(n/2+1), -1, -1):
    number = row
    for cols in range(0, n-row):
        print(" ", end="")
    for cols in range(0, row):
        print(number, end="")
        number-=1
    number = 2
    for cols in range(1, row):
        print(number, end="")
        number+=1
    print()


print("-------------------------------")


row = 0
while(row < int(n/2+1)):
    number = row
    cols = 0
    while(cols < n-row):
        print(" ", end="")
        cols+=1
    cols = 0
    while(cols < row):
        print(number, end="")
        number-=1
        cols+=1
    number = 2
    cols = 1
    while(cols < row):
        print(number, end="")
        number+=1
        cols+=1
    row+=1
    print()

while(row > 0):
    number = row
    cols = 0
    while(cols < n-row):
        print(" ", end="")
        cols+=1
    cols = 0
    while(cols < row):
        print(number, end="")
        number-=1
        cols+=1
    number = 2
    cols = 1
    while(cols < row):
        print(number, end="")
        number+=1
        cols+=1
    row-=1
    print()

