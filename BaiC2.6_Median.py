data = input().strip()
while len(data) == 0:
    data = input().strip()

n = int(data)
m = []
for i in range(n):
    row = [int(j) for j in input().split()]
    m.append(row)

result = []
for i in range(1, n-1):
    row = []
    for j in range(1, n-1):
        temp = [m[i-1][j-1], m[i-1][j], m[i-1][j+1], m[i][j-1], m[i][j], m[i][j+1], m[i+1][j-1], m[i+1][j], m[i+1][j+1]]
        temp.sort()
        row.append(temp[4])
    result.append(row)

for row in result:
    for i in row:
        print(i, end=' ')
    print()