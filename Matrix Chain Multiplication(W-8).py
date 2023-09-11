def mcm(dims, names):
    n = len(dims)-1
    dp = [[0]*n for _ in range(n)]
    k_table = [[0]*n for _ in range(n)]
    k1_table = [[0]*n for _ in range(n)]
    for length in range(2,n+1):
        for i in range(n-length+1):
            j = i+length-1
            dp[i][j] = float('inf')
            for k in range(i,j):
                cost = dp[i][k]+dp[k+1][j]+dims[i]*dims[k+1]*dims[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    k_table[i][j] = k
                    k1_table[i][j] = k+1
    def combination(i,j):
        if i==j:
            return names[i]
        else:
            k = k_table[i][j]
            l = combination(i,k)
            r = combination(k+1,j)
            return f'({l}x{r})'
    mini = dp[0][n-1]
    combo = combination(0,n-1)
    print("Cost Table:")
    for i in dp:
        print(i)
    print("K- Table")
    for i in k1_table:
        print(i)
    return mini, combo
n = int(input("Enter no.of matrices:"))
dim = []
names = []
for i in range(n):
    m = input(f"Enter row and column dimensions of matrix {i+1}:")
    row,col = map(int,m.split('x'))
    nam = input(f"Enter name of the matrix {i+1}:")
    if i==0:
        dim.append(row)
    dim.append(col)
    names.append(nam)
mini,combo = mcm(dim,names)
print("Cost:",mini)
print("Combo:",combo)
