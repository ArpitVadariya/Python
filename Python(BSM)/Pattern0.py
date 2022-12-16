n = 7
# 1
print(1)

for i in range(1, n):
    for j in range(1, i+1):
        print("*" , end=" ")
    print()

print("----------------------------------------")
# 2
print(2)

for i in range(1, n):
    for j in range(1, i+1):
        print(i , end=" ")
    print()

print("----------------------------------------")
# 3
print(3)

for i in range(1, n):
    for j in range(1, i+1):
        print(j , end=" ")
    print()

print("----------------------------------------")
# 4
print(4)

for i in range(1, n):
    for j in range(1, i+1):
        print(n-i , end=" ")
    print()

print("----------------------------------------")
# 5
print(5)

for i in range(1, n):
    for j in range(1, i+1):
        print(n-j , end=" ")
    print()

print("----------------------------------------")
# 6
print(6)

for i in range(n-1, 0, -1):
    for j in range(i, 0, -1):
        print("*" , end=" ")
    print()

print("----------------------------------------")
# 7
print(7)

for i in range(1, n):
    for j in range(1, i+1):
        print("*" , end=" ")
    print()
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print("*" , end=" ")
    print()

print("----------------------------------------")
# 8
print(8)

for i in range(n, 1, -1):
    for j in range(i+1, 1, -1):
        print("*" , end=" ")
    print()
for i in range(0, n):
    for j in range(0, i+1):
        print("*" , end=" ")
    print()

print("----------------------------------------")
# 9
print(9)

m = n - 1
for i in range(1, n):
    for j in range(1, m):
        print(end="  ")
    m = m-1
    for j in range(1, i+1):  
        print("*", end=" ")  
    print(" ")

print("----------------------------------------")
# 10
print(10)

m = 1
for i in range(n-1, 0, -1):
    for j in range(1, m):
        print(end="  ")
    m = m+1
    for j in range(i, 0, -1):
        print("*" , end=" ")
    print()


print("----------------------------------------")

# 11
print(11)

m = n - 1
for i in range(1, n+1):
    for j in range(1, m+1):
        print(end="  ")
    m = m-1
    for j in range(1, i+1):  
        print("*", end=" ")  
    # print("m " + str(m))
    print(" ")
m = 2
for i in range(n-1, 0, -1):
    for j in range(1, m):
        print(end="  ")
    m = m+1
    for j in range(i, 0, -1):
        print("*" , end=" ")
    print()

print("----------------------------------------")

# 12
print(12)

m = 2
for i in range(n-1, 1, -1):
    for j in range(1, m):
        print(end="  ")
    m = m+1
    for j in range(i, 0, -1):
        print("*" , end=" ")
    print()
m = n - 1
for i in range(1, n):
    for j in range(1, m+1):
        print(end="  ")
    m = m-1
    for j in range(1, i+1):  
        print("*", end=" ")  
    # print("m " + str(m))
    print(" ")


print("----------------------------------------")

# 13
print(13)

m = n - 1
for i in range(1, n-1):
    for j in range(1, n-1):
        print(end="  ")
    m = m-1
    for j in range(1, i+1):  
        print("*", end=" ")  
    print(" ")

for i in range(1, n-1):
    print("*", end=" ")

m = 1
for i in range(n-1, 0, -1):
    for j in range(1, m):
        print(end="  ")
    m = m+1
    for j in range(i, 0, -1):
        print("*" , end=" ")
    print()



print("----------------------------------------")

# 14
print(14)

for i in range(1, n):
    for s in range(1, n-i):
        print("  ", end=" ")

    for j in range(1, i):
        print("* ", end=" ")

    for j in range(i, n):
        print("* ", end=" ")
    print()



print("----------------------------------------")

# 15
print(15)

for i in range(1, n):
    for s in range(1, n-i):
        print("  ", end=" ")

    for j in range(1, i):
        print("* ", end=" ")

    for j in range(1, i-1):
        print("* ", end=" ")
    print()


print("----------------------------------------")

# 16
print(16)

m = 1
for i in range(n-1, 0, -1):
    for j in range(1, m):
        print("  ", end=" ")
    m = m+1
    for j in range(i, 0, -1):
        print("* " , end=" ")
    

    for j in range(1, i):
        print("* ", end=" ")
    print()


print("----------------------------------------")

# 17
print(17)

for i in range(1, n):
    for s in range(1, n-i+1):
        print("  ", end=" ")

    for j in range(1, i):
        print("* ", end=" ")

    for j in range(1, i-1):
        print("* ", end=" ")
    print()

m = 1
for i in range(n-1, 0, -1):
    for j in range(1, m):
        print("  ", end=" ")
    m = m+1
    for j in range(i, 0, -1):
        print("* " , end=" ")
    

    for j in range(1, i):
        print("* ", end=" ")
    print()


print("----------------------------------------")

# 18
print(18)

for i in range(1, n):
    for s in range(1, n-i+1):
        print("  ", end=" ")

    for j in range(1, i):
        print("*", end=" ")

    for j in range(1, i-1):
        print("*", end=" ")
    print()

m = 1
for i in range(n-1, 0, -1):
    for j in range(1, m):
        print("  ", end=" ")
    m = m+1
    for j in range(i, 0, -1):
        print("*" , end=" ")
    

    for j in range(1, i):
        print("*", end=" ")
    print()


print("----------------------------------------")

# 19
print(19)

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

# 20
print(20)

for i in range(1, n):
    for j in range(1, i+1):
        print(j*i, end=" ")
    print()


print("----------------------------------------")

# 21
print(21)

for i in range(1, n):
    if(i < (n/2)):
        for j in range(1,i+1):
            print(j*i, end=" ")
    else:
        for j in range(1, n-i+1):
            print(j*(n-i), end=" ")
    print()



print("----------------------------------------")

# 22
print(22)

for i in range(0, n+1):
    if(i == n):
        for j in range(0, n-i-1):
            print(" ", end="")
        for j in range(0, 1):
            print("* ", end="")
        for j in range(0, n):
            print("* ", end="")
        for j in range(0, 1):
            print("*", end="")
    else:
        if(i == 0):
            for j in range(0, n-i+1):
                print(" ", end="")
            for j in range(0, 1):
                print("* ", end="")
        else:
            for j in range(0, n-i):
                print(" ", end="")
            for j in range(0, 1):
                print("*", end="")
            for j in range(0, 2*i+1):
                print(" ", end="")
            for j in range(0, 1):
                print("*", end="")
    print()



print("----------------------------------------")

# 23
print(23)

for i in range(n, -1, -1):
    if(i == n):
        for j in range(0, n-i-1):
            print(" ", end="")
        for j in range(0, 1):
            print("* ", end="")
        for j in range(0, n):
            print("* ", end="")
        for j in range(0, 1):
            print("*", end="")
    else:
        if(i == 0):
            for j in range(0, n-i+1):
                print(" ", end="")
            for j in range(0, 1):
                print("* ", end="")
        else:
            for j in range(0, n-i):
                print(" ", end="")
            for j in range(0, 1):
                print("*", end="")
            for j in range(0, 2*i+1):
                print(" ", end="")
            for j in range(0, 1):
                print("*", end="")
    print()


print("----------------------------------------")

# 24
print(24)

for i in range(0, n+1):
    if(i == n):
        for j in range(0, n-i-1):
            print(" ", end="")
        for j in range(0, 1):
            print("* ", end="")
        for j in range(0, n):
            print("* ", end="")
        for j in range(0, 1):
            print("*", end="")
    else:
        if(i == 0):
            for j in range(0, n-i+1):
                print(" ", end="")
            for j in range(0, 1):
                print("* ", end="")
        else:
            for j in range(0, n-i):
                print(" ", end="")
            for j in range(0, 1):
                print("*", end="")
            for j in range(0, 2*i+1):
                print(" ", end="")
            for j in range(0, 1):
                print("*", end="")
    print()

for i in range(n-1, -1, -1):
    if(i == n):
        for j in range(0, n-i-1):
            print(" ", end="")
        for j in range(0, 1):
            print("* ", end="")
        for j in range(0, n):
            print("* ", end="")
        for j in range(0, 1):
            print("*", end="")
    else:
        if(i == 0):
            for j in range(0, n-i+1):
                print(" ", end="")
            for j in range(0, 1):
                print("* ", end="")
        else:
            for j in range(0, n-i):
                print(" ", end="")
            for j in range(0, 1):
                print("*", end="")
            for j in range(0, 2*i+1):
                print(" ", end="")
            for j in range(0, 1):
                print("*", end="")
    print()



print("----------------------------------------")

# 25
print(25)

for i in range(0, n):
    if(i == 0):
        for j in range(0, n-i+1):
            print(" ", end="")
        for j in range(0, 1):
            print("* ", end="")
    else:
        for j in range(0, n-i):
            print(" ", end="")
        for j in range(0, 1):
            print("*", end="")
        for j in range(0, 2*i+1):
            print(" ", end="")
        for j in range(0, 1):
            print("*", end="")
    print()

for i in range(n, -1, -1):
    if(i == 0):
        for j in range(0, n-i+1):
            print(" ", end="")
        for j in range(0, 1):
            print("* ", end="")
    else:
        for j in range(0, n-i):
            print(" ", end="")
        for j in range(0, 1):
            print("*", end="")
        for j in range(0, 2*i+1):
            print(" ", end="")
        for j in range(0, 1):
            print("*", end="")
    print()


print("----------------------------------------")

# 26
print(26)

for i in range(0, n+1):
    if(i == 0 or i==n):
        for j in range(0, n+1):
            print("* ", end="")
    else:
        for j in range(0, 1):
            print("* ", end="")
        for j in range(1, n):
            print("  ", end="")
        for j in range(0, 1):
            print("* ", end="")
    print()


print("----------------------------------------")

# 27
print(27)

for i in range(n, -1, -1):
    if(i == n):
        for j in range(0, n-i-1):
            print(" ", end="")
        for j in range(0, 1):
            print("* ", end="")
        for j in range(0, n):
            print("* ", end="")
        for j in range(0, 1):
            print("*", end="")
    else:
        if(i == 0):
            for j in range(0, n-i+1):
                print(" ", end="")
            for j in range(0, 1):
                print("* ", end="")
        else:
            for j in range(0, n-i):
                print(" ", end="")
            for j in range(0, 1):
                print("*", end="")
            for j in range(0, 2*i+1):
                print(" ", end="")
            for j in range(0, 1):
                print("*", end="")
    print()

for i in range(1, n+1):
    if(i == n):
        for j in range(0, n-i-1):
            print(" ", end="")
        for j in range(0, 1):
            print("* ", end="")
        for j in range(0, n):
            print("* ", end="")
        for j in range(0, 1):
            print("*", end="")
    else:
        if(i == 0):
            for j in range(0, n-i+1):
                print(" ", end="")
            for j in range(0, 1):
                print("* ", end="")
        else:
            for j in range(0, n-i):
                print(" ", end="")
            for j in range(0, 1):
                print("*", end="")
            for j in range(0, 2*i+1):
                print(" ", end="")
            for j in range(0, 1):
                print("*", end="")
    print()


print("----------------------------------------")

# 28
print(28)


m = 1
for i in range(n-1, 0, -1):
    for j in range(1, m):
        print("  ", end=" ")
    m = m+1
    for j in range(i, 0, -1):
        print("* " , end=" ")
    

    for j in range(1, i):
        print("* ", end=" ")
    print()
for i in range(3, n+1):
    for s in range(1, n-i+1):
        print("  ", end=" ")

    for j in range(1, i):
        print("* ", end=" ")

    for j in range(1, i-1):
        print("* ", end=" ")
    print()


print("----------------------------------------")

# 29
print(29)


