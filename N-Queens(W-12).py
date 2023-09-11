def n_queens(n):
    b = [[0 for _ in range(n)]for _ in range(n)]
    ss = []
    solve_until(b,0, n, ss)
    return ss
def solve_until(b,col, n , ss):
    if col == n:
        s = []
        for i in range(n):
            row = []
            for j in range(n):
                if b[i][j] == 1:
                    row.append('Q')
                else:
                    row.append('.')
            s.append(row)
        ss.append(s)
        return
    for i in range(n):
        if is_safe(b,i,col,n):
            b[i][col] =1
            solve_until(b,col+1,n,ss)
            b[i][col] = 0
def is_safe(b,row,col,n):
    for i in range(col):
        if b[row][i]==1:
            return False
    i,j = row,col
    while i>=0 and j>=0 :
        if b[i][j] == 1:
            return False
        i-=1
        j-=1
    i,j = row ,col
    while i<n and j>=0:
        if b[i][j] == 1:
            return False
        i+=1
        j-=1
    return True
n = int(input("Enter no.of queens:"))
ss = n_queens(n)
print(f"Possible ways for {n}-Queens :",len(ss))
s = ss[0]
for i in s:
    print(*i)
            
