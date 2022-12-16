#       * * * * 
#     * * * * 
#   * * * * 
# * * * * 




n = 5


for i in range(1, n):
    for s in range(1, n-i):
        print(" ", end=" ")

    for j in range(1, i):
        print("*", end=" ")

    for j in range(i, n):
        print("*", end=" ")
    print()

print("------------------------")


i = 1

while(i < n):
    s = 1
    while(s < n-i):
        print("  ", end="")
        s+=1
    j = 1
    while(j < i):
        print("* ", end="")
        j+=1
    j = i
    while(j < n):
        print("* ", end="")
        j+=1
    print()
    i+=1