# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


n = 10

# if(n%2 == 0):
#     n-=1

for row in range(0, n+1):
    if(row < (n/2)):
        for cols in range(0, row):
            print("* ", end="")
        print()
    else:
        for cols in range(n, row, -1):
            print("* ", end="")
        print()


print("-----------------------------------------")

row = 0
while(row < n):
    cols = 0
    if(row < (n/2)):
        while(cols < row):
            print("* ", end="")
            cols+=1
        cols=0
    else:
        while(cols < n-row):
            print("* ", end="")
            cols+=1
    print()
    row+=1
        