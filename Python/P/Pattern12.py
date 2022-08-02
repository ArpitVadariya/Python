#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

from math import ceil


n = 5

if(n%2 != 0):
    for row in range(0, n):
        if(row < n/2):
            for cols in range(0, row+1):
                print(" ", end="")
            for cols in range(0, (int(ceil(n/2)))-row):
                print("* ", end="")
        else:
            for cols in range(0, n-row+1):
                print(" ", end="")
            for cols in range(1, row-(int(n/2))+1):
                print("* ", end="")
        
        print()
else:
    for row in range(0, n):
        if(row < n/2):
            for cols in range(0, row+1):
                print(" ", end="")
            for cols in range(0, (int(ceil(n/2)))-row):
                print("* ", end="")
        else:
            for cols in range(1, n-row+1):
                print(" ", end="")
            for cols in range(0, row-(int(n/2))+1):
                print("* ", end="")
        
        print()

print("-----------------------------------------")


row = 0

if(n%2 != 0):
    while(row < n):
        if(row < n/2):
            cols = 0
            while(cols<row):
                print(" ", end="")
                cols+=1
            cols = 0
            while(cols < (int(ceil(n/2)))-row):
                print("* ", end="")
                cols+=1
        else:
            cols = 0
            while(cols < n-row):
                print(" ", end="")
                cols+=1
            cols = 1
            while(cols < row-(int(n/2))+1):
                print("* ", end="")
                cols+=1
        print()
        row+=1
else:
    while(row < n):
        if(row < n/2):
            cols = 0
            while(cols<row):
                print(" ", end="")
                cols+=1
            cols = 0
            while(cols < (int(n/2))-row):
                print("* ", end="")
                cols+=1
        else:
            cols = 1
            while(cols < n-row):
                print(" ", end="")
                cols+=1
            cols = 0
            while(cols < row-(int(ceil(n/2)))+1):
                print("* ", end="")
                cols+=1
        print()
        row+=1

