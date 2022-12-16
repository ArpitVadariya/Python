#    * 
#   * * * 
#  * * * * * 
# * * * * * * * 
#  * * * * * 
#   * * * 
#    * 


n = 5



for i in range(1, n):
    for s in range(1, n-i+1):
        print(" ", end="")

    for j in range(1, i):
        print("* ", end="")

    for j in range(1, i-1):
        print("* ", end="")
    print()

m = 1
for i in range(n-1, 0, -1):
    for j in range(1, m):
        print(" ", end="")
    m = m+1
    for j in range(i, 0, -1):
        print("* " , end="")
    

    for j in range(1, i):
        print("* ", end="")
    print()

print("----------------------------------------")


i = 1
while(i < n):
    s = 1
    while(s < n-i+1):
        print(" ", end="")
        s+=1
    j = 1
    while(j < i):
        print("* ", end="")
        j+=1
    j = 1
    while(j < i-1):
        print("* ", end="")
        j+=1

    print()
    i+=1


i = n
while(i > 1):
    s = 1
    while(s < n-i+1):
        print(" ", end="")
        s+=1
    j = 1
    while(j < i):
        print("* ", end="")
        j+=1
    j = 1
    while(j < i-1):
        print("* ", end="")
        j+=1

    print()
    i-=1