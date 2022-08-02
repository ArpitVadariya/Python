# *****
# ****
# ***
# **
# *

n = 5

for row in range(n, 0, -1):
    for cols in range(0, row):
        print("* ", end="")
    print()

print("--------------------------")


row = n
while(row > 0):
    cols = row
    while(cols > 0):
        print("* ", end="")
        cols-=1
    print()
    row-=1