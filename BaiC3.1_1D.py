
data = input().strip().split()
while len(data) == 0:
    data = input().strip().split()

m = int(data[0])
n = int(data[1])
matrix = []
for i in range(m):
    row = [int(j) for j in input().split()]
    matrix.append(row)

for i in range(m):
    e = 0
    for j in range(n):
        u = matrix[i][j] - e
        b = 0 if u < 127 else 255
        e = b - u
        matrix[i][j] = b

for row in matrix:
    for i in row:
        print(i, end=' ')
    print()
