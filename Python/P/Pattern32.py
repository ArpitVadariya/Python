# 1 
# 2 4 
# 3 6 9 
# 4 8 12 16        
# 5 10 15 20 25

n = 7


for i in range(1, n):
    for j in range(1, i+1):
        print(j*i, end=" ")
    print()

print("-------------------")

row = 1
while row < n:
    cols = 1
    while cols < row+1:
        print(cols * row, end=" ")
        cols+=1
    print()
    row+=1