def histogram_image(m, n, l, matrix):
    ma = []
    for row in matrix:
        for i in row:
            ma.append(i)
    p = []
    for i in range(l):
        p.append((ma.count(i) / (m * n)))
    s = []
    for i in range(l):
        t = 0
        for j in range(i + 1):
            t += p[j]
        s.append(round((l - 1) * t))

    histogram_matrix = [[s[i] for i in row] for row in matrix]
    return histogram_matrix

data = input().split()
m = int(data[0])
n = int(data[1])
l = int(input())

matrix = []
for i in range(m):
    row = [int(j) for j in input().split()]
    matrix.append(row)

result = histogram_image(m, n, l, matrix)

for row in result:
    for i in row:
        print(i, end=' ')
    print()
