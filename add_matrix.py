X = [[1,2,3],
    [4 ,5,6],
    [7 ,6,9]]
Y = [[9,8,9],
    [6,5,4],
    [3,2,1]]
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)
