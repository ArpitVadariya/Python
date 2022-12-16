#      *
#     * *
#    *   *
#   *     *
#  *       *
#   *     *
#    *   *
#     * *
#      *


n = 10

for row in range(0, int(n/2+1)):
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
for row in range(int(n/2-1), -1, -1):
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


print("---------------------------------------")


row = 0

while(row < int(n/2+1)):
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

while(row > -1):
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
