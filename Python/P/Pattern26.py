# 1 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3
# 4 4 4
# 5 5
# 6



n = 7

for row in range(1, n):
    for cols in range(0, n-row):
        print(row, end=" ")
    print()


print("---------------------------------")


row = 1
while(row < n):
    cols = 0
    while(cols < n-row):
        print(row, end=" ")
        cols+=1
    print()
    row+=1