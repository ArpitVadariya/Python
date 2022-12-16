#      * * * * *
#       * * * *
#        * * *
#         * *
#          *

n = 5

for row in range(n, 0, -1):
    for cols in range(0, n-row):
        print(" ", end="")
    for cols in range(0, row):
        print("* ", end="")
    print()

print("---------------------------------------")

row = n
while(row > 0):
    cols = 0
    while(cols < n-row):
        print(" ", end="")
        cols+=1
    cols = 0
    while(cols < row):
        print("* ", end="")
        cols+=1
    row-=1
    print()