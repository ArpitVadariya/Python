# ****
# *  *
# *  *
# *  *
# ****


n = 5

for row in range(0, n):
    if(row == 0 or row == n-1):
        for cols in range(0, n):
            print("*", end="")
    else:
        for cols in range(0, n):
            if(cols == 0 or cols == n-1):
                print("*", end="")
            else:
                print(" ", end="")
    print()

print("---------------------------------")

row = 0
while(row < n):
    if(row == 0 or row == n-1):
        cols = 0
        while(cols < n):
            print("*", end="")
            cols+=1
    else:
        cols = 0
        while(cols < n):
            if(cols == 0 or cols == n-1):
                print("*", end="")
            else:
                print(" ", end="")
            cols+=1
    print()
    row+=1