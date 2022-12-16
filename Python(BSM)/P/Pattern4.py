# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = 5

for row in range(0, n+1):
    for cols in range(0, row):
        print(cols+1, end=" ")
    print()


print("----------------------------------")


row = 0
while(row < n+1):
    cols=0
    while(cols<row):
        print(cols+1, end=" ")
        cols+=1
    print()
    row+=1