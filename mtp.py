def ManhattanTourist(n,m,down,right):
    LM = {(0,0):0}
    LP = {(0,0):'-'}
    #n is the number of columns and m is the number of rows
    #Setting up first row and fist column
    for i in range(1,n+1):
        LM[(i,0)] = LM[(i-1,0)] + down[i-1][0]
        LP[(i,0)] = 'U'
    for j in range(1,m+1):
        LM[(0,j)] = LM[(0,j-1)] + right[0][j-1]
        LP[(0,j)] = 'L'
    
    #Finding longest path
    for i in range(1,n+1):
        for j in range(1,m+1):
            LM[(i,j)] = max(LM[(i-1,j)]+down[i-1][j], LM[(i,j-1)] + right[i][j-1])
            if LM[(i,j)] == LM[(i-1,j)]+down[i-1][j]:
                LP[(i,j)] = 'U'
            else:
                LP[(i,j)] = 'L'
    test = True
    l = ""
    i = n
    j = m
    while test:
        if LP[(i,j)] == 'U':
            l = "Down "+l
            i-=1
        else:
            l = "Right "+l
            j-=1
        if i==0 and j==0:
            test = False
    print("The longest path is:",l)
    return LM[(n,m)] 

print("Enter the number of rows:",end="")
rows = int(input())
print("Enter the number of columns:",end="")
columns = int(input())

print("Enter the weights of the downward facing arrows in order of left to right:",end="")
downi = input().split()
print("Enter the weights of the rightward facing arrows in order of left to right:",end="")
righti = input().split()
down = []
count = 0
for i in range(rows-1):
    tmp = []
    for j in range(columns):
        curr = int(downi[count])
        tmp.append(curr)
        count += 1
    down.append(tmp)
right = []
count = 0
for i in range(columns):
    tmp = []
    for j in range(rows-1):
        curr = int(righti[count])
        tmp.append(curr)
        count+=1
    right.append(tmp)

print("The weight of the longest path is:",ManhattanTourist(columns-1,rows-1,down,right))
