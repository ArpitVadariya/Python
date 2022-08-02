#           *****
#          *   *
#         *   *
#        *   *
#       *****


n = 5

for row in range(0, n):
    if(row == 0 or row == n-1):
        for cols in range(0, n-row):
            print(" ", end="")
        for cols in range(0, n):
            print("*", end="")
    else:
        for cols in range(0, n-row):
            print(" ", end="")
        for cols in range(0, 1):
            print("*", end="")
        for cols in range(0, n-2):
            print(" ", end="")
        for cols in range(0, 1):
            print("*", end="")
    print()

print("-----------------------------------")

row = 0
while(row < n):
    if(row == 0 or row == n-1):
        cols = 0
        while(cols < n-row):
            print(" ", end="")
            cols+=1
        cols = 0
        while(cols < n):
            print("*", end="")
            cols+=1
    else:
        cols = 0
        while(cols < n-row):
            print(" ", end="")
            cols+=1
        cols = 0
        while(cols < 1):
            print("*", end="")
            cols+=1
        cols = 0
        while(cols < n-2):
            print(" ", end="")
            cols+=1
        cols = 0
        while(cols < 1):
            print("*", end="")
            cols+=1
    print()
    row+=1