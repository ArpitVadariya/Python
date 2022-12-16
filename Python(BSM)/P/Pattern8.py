#     *
#    ***
#   *****
#  *******
# *********

n = 5

for row in range(0, n):
    for cols in range(1, n-row):
        print("  ", end="")
    for cols in range(1, row):
        print("* ", end="")
    for cols in range(0, row):
        print("* ", end="")
    print()


print("-------------------------------------")

row = 1
while(row < n):
    cols = 0
    while(cols < n-row):
        print("  ", end="")
        cols+=1
    cols = 1
    while(cols < row):
        print("* ", end="")
        cols+=1
    cols = 0
    while(cols < row):
        print("* ", end="")
        cols+=1
    row+=1
    print()