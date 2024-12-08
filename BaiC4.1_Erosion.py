def image_erosion(f, n, fil_matrix, matrix):
    result = [[i for i in row] for row in matrix]
    fs = f // 2

    for i in range(n):
        for j in range(n):
            check = True

            for k in range(-fs, fs + 1):
                for l in range(-fs, fs + 1):
                    if 0 <= i + k < n and 0 <= j + l < n:
                        if (fil_matrix[k + fs][l + fs] != 0
                                and matrix[i + k][j + l] != fil_matrix[k + fs][l + fs]):
                            result[i][j] = 0
                            check = False
                    else:
                        result[i][j] = 0
                        check = False
                    if not check:
                        break
                if not check:
                    break
    return result


data = input().strip()
while len(data) == 0:
    data = input().strip()

f = int(data)
fil_matrix = []
for i in range(f):
    row = [int(j) for j in input().split()]
    fil_matrix.append(row)

n, m = [int(j) for j in input().split()]
matrix = []
for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

result_matrix = image_erosion(f, n, fil_matrix, matrix)

for row in result_matrix:
    for i in row:
        print(i, end=' ')
    print()