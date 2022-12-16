# *
# **
# ***
# ****
# *****

n = 5

for row in range(0, n+1):
    for cols in range(0, row):
        print("* ", end="")
    print()

print("----------------------------------------")


row = 0
while(row < n+1):
    cols=0
    while(cols<row):
        print("* ", end="")
        cols+=1
    print()
    row+=1