# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1


n = 5

for row in range(0, n+1):
    if(row%2 == 0):
        for cols in range(0, row):
            if(cols%2 == 0):
                print("0 ", end="")
            else:
                print("1 ", end="")
    else:
        for cols in range(0, row):
            if(cols%2 == 0):
                print("1 ", end="")
            else:
                print("0 ", end="")
    print()

print("-----------------------------------")


row = 0
while(row < n+1):
    if(row%2 == 0):
        cols = 0
        while(cols < row):
            if(cols%2 == 0):
                print("0 ", end="")
            else:
                print("1 ", end="")
            cols+=1
    else:
        cols = 0
        while(cols < row):
            if(cols%2 == 0):
                print("1 ", end="")
            else:
                print("0 ", end="")
            cols+=1
    print()
    row+=1