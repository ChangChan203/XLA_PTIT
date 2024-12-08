def dilated_image(f, filter, n, matrix):
    re = [[i for i in row] for row in matrix]
    fs = f // 2

    for i in range(n):
        for j in range(n):

            check = True

            for k in range(-fs, fs + 1):
                for l in range(-fs, fs + 1):
                    if 0 <= i + k < n and 0 <= j + l < n:
                        if (filter[k + fs][l + fs] == 1
                                and matrix[i + k][j + l] == filter[k + fs][l + fs]):
                            re[i][j] = 1
                            check = False
                    else:
                        re[i][j] = 0
                        check = True
                    if not check:
                        break
                if not check:
                    break
    return re


data = input().strip()
while len(data) == 0:
    data = input().strip()

f = int(data)
filter = []
for i in range(f):
    row = [int(j) for j in input().split()]
    filter.append(row)

n, m = [int(i) for i in input().split()]
matrix = []
for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

result = dilated_image(f, filter, n, matrix)

for row in result:
    for i in row:
        print(i, end=' ')
    print()