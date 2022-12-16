# *****
# *****
# *****
# *****
# *****

n = 5

for row in range(0, n):
    for cols in range(0, n):
        print("* ", end="")
    print()


print("------------------------------------")

row = 0
while(row < n):
    col = 0
    while(col < n):
        print("* ", end="")
        col+=1
    print()
    row+=1