#      *
#     * *
#    *   *
#   *     *
#  *       *
# ***********
#  *       *
#   *     *
#    *   *
#     * *
#      *


n = 5

for row in range(0, n+1):
    if(row == n):
        for cols in range(0, 2*n+1):
            print("*", end="")
    else:
        if(row == 0):
            for cols in range(0, n-row):
                print(" ", end="")
            for cols in range(0, 1):
                print("*", end="")
        else:
            for cols in range(0, n-row):
                print(" ", end="")
            for cols in range(0, 1):
                print("*", end="")
            for cols in range(0, 2*row-1):
                print(" ", end="")
            for cols in range(0, 1):
                print("*", end="")
    print()

for row in reversed(range(0, n)):
    if(row == n):
        for cols in range(0, 2*n+1):
            print("*", end="")
    else:
        if(row == 0):
            for cols in range(0, n-row):
                print(" ", end="")
            for cols in range(0, 1):
                print("*", end="")
        else:
            for cols in range(0, n-row):
                print(" ", end="")
            for cols in range(0, 1):
                print("*", end="")
            for cols in range(0, 2*row-1):
                print(" ", end="")
            for cols in range(0, 1):
                print("*", end="")
    print()

print("----------------------------")

row = 0
while(row < n+1):
    if(row == n):
        cols = 0
        while(cols < 2*n+1):
            print("*", end="")
            cols+=1
    else:
        if(row == 0):
            cols = 0
            while(cols < n-row):
                print(" ", end="")
                cols+=1
            cols = 0
            while(cols < 1):
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
            while(cols < 2*row-1):
                print(" ", end="")
                cols+=1
            cols = 0
            while(cols < 1):
                print("*", end="")
                cols+=1
    row+=1
    print()

row = n-1
while(row > -1):
    if(row == n):
        cols = 0
        while(cols < 2*n+1):
            print("*", end="")
            cols+=1
    else:
        if(row == 0):
            cols = 0
            while(cols < n-row):
                print(" ", end="")
                cols+=1
            cols = 0
            while(cols < 1):
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
            while(cols < 2*row-1):
                print(" ", end="")
                cols+=1
            cols = 0
            while(cols < 1):
                print("*", end="")
                cols+=1
    row-=1
    print()
