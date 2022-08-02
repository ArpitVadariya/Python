# 4 4 4 4 4 4 4  
# 4 3 3 3 3 3 4   
# 4 3 2 2 2 3 4   
# 4 3 2 1 2 3 4   
# 4 3 2 2 2 3 4   
# 4 3 3 3 3 3 4   
# 4 4 4 4 4 4 4  



n = 4
N = n
n = 2*n-1

for row in range(0, n+1):
    for cols in range(0, n+1):
        number = N - min(min(row, cols), min(n-row, n-cols)+1)
        print(number, end=" ")
    print()


print("------------------------")

n = 4
N = n
n = 2*n-1

row = 0
while(row < n+1):
    cols = 0
    while(cols < n+1):
        number = N - min(min(row, cols), min(n-row, n-cols)+1)
        print(number, end=" ")
        cols+=1
    print()
    row+=1