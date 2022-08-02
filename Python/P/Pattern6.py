#       *
#      **
#     ***
#    ****
#   *****


n = 5

for row in range(1, n+1):
    for space in range(0, n-row):
        print("  ", end="")
    for cols in range(0, row):
        print("* ", end="")
    print()

print("----------------------------------")


row = 1
while(row < n+1):
    cols = 0
    # col = 0
    while(cols < n-row):
        print("  ", end="")
        cols+=1
    cols = 0
    while(cols < row):
        print("* ", end="")
        cols+=1
    print()
    row+=1