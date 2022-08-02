# *        *
# **      **
# * *    * *
# *  *  *  *
# *   **   *
# *   **   *
# *  *  *  *
# * *    * *
# **      **
# *        *


n = 10


for row in range(0, int(n/2)):
    for cols in range(0, 1):
        print("*", end="")
    for cols in range(0, row-1):
        print(" ", end="")
    for cols in range(0, 1):
        if(row > 0):
            print("*", end="")
    for cols in range(0, n-2*row-2):
        print(" ", end="")
    for cols in range(0, 1):
        print("*", end="")
    for cols in range(0, row-1):
        print(" ", end="")
    for cols in range(0, 1):
        if(row > 0):
            print("*", end="")
    print()
for row in reversed(range(0, int(n/2))):
    for cols in range(0, 1):
        print("*", end="")
    for cols in range(0, row-1):
        print(" ", end="")
    for cols in range(0, 1):
        if(row > 0):
            print("*", end="")
    for cols in range(0, n-2*row-2):
        print(" ", end="")
    for cols in range(0, 1):
        print("*", end="")
    for cols in range(0, row-1):
        print(" ", end="")
    for cols in range(0, 1):
        if(row > 0):
            print("*", end="")
    print()


print("-----------------------------")


row = 0

while(row < int(n/2)):
    cols = 0
    while(cols < 1):
        print("*", end="")
        cols+=1
    cols = 0
    while(cols < row-1):
        print(" ", end="")
        cols+=1
    cols = 0
    while(cols < 1):
        if(row > 0):
            print("*", end="")
        cols+=1
    cols = 0
    while(cols < n-2*row-2):
        print(" ", end="")
        cols+=1
    cols = 0
    while(cols < 1):
        print("*", end="")
        cols+=1
    cols = 0
    while(cols < row-1):
        print(" ", end="")
        cols+=1
    cols = 0
    while(cols < 1):
        if(row > 0):
            print("*", end="")
        cols+=1
    print()
    row+=1

row-=1

while(row > -1):
    cols = 0
    while(cols < 1):
        print("*", end="")
        cols+=1
    cols = 0
    while(cols < row-1):
        print(" ", end="")
        cols+=1
    cols = 0
    while(cols < 1):
        if(row > 0):
            print("*", end="")
        cols+=1
    cols = 0
    while(cols < n-2*row-2):
        print(" ", end="")
        cols+=1
    cols = 0
    while(cols < 1):
        print("*", end="")
        cols+=1
    cols = 0
    while(cols < row-1):
        print(" ", end="")
        cols+=1
    cols = 0
    while(cols < 1):
        if(row > 0):
            print("*", end="")
        cols+=1
    print()
    row-=1