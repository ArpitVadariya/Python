#        *      *
#      *   *  *   *
#    *      *      *


n = 3

for row in range(0, n):
    for cols in range(0, n-row):
        print("  ", end="")
    for cols in range(0, 1):
        print("* ", end="")
    for cols in range(0, 2*row-1):
        print("  ", end="")
    for cols in range(0, 1):
        if(row > 0):
            print("* ", end="")
    for cols in range(0, 2*(n-row-1)):
        print("  ", end="")
    for cols in range(0, 1):
        print("* ", end="")
    for cols in range(0, 2*row-1):
        print("  ", end="")
    for cols in range(0, 1):
        if(row > 0):
            print("* ", end="")
    print()

print("--------------------------------")

row = 0
while(row < n):
    cols = 0
    while(cols < n-row):
        print("  ", end="")
        cols+=1
    cols = 0
    while(cols < 1):
        print("* ", end="")
        cols+=1
    cols = 0
    while(cols < 2*row-1):
        print("  ", end="")
        cols+=1
    cols = 0
    while(cols < 1):
        if(row > 0):
            print("*  ", end="")
        cols+=1
    cols = 0
    while(cols < 2*(n-row-1)):
        print("  ", end="")
        cols+=1
    cols = 0
    while(cols < 1):
        print("* ", end="")
        cols+=1
    cols = 0
    while(cols < 2*row-1):
        print("  ", end="")
        cols+=1
    cols = 0
    while(cols < 1):
        if(row > 0):
            print("* ", end="")
        cols+=1
    print()
    row+=1