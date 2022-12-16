# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11 12 13 14 15

n = 5

number = 1
for row in range(0, n+1):
    for cols in range(0, row):
        print(number, end=" ")
        number+=1
    print()

print("-------------------------------")

row = 0
number = 1
while(row < n+1):
    cols = 0
    while(cols < row):
        print(number, end=" ")
        number+=1
        cols+=1
    print()
    row+=1