def boundary_ex(f, n, fil, matrix):
    re = [[i for i in row] for row in matrix]
    fs = f // 2

    for i in range(n):
        for j in range(n):
            check = True

            for k in range(-fs, fs + 1):
                for l in range(-fs, fs + 1):
                    if 0 <= i + k < n and 0 <= j + l < n:
                        if fil[k + fs][l + fs] != 0 and matrix[i + k][j + l] != fil[k + fs][l + fs]:
                            re[i][j] = 0
                            check = False
                    else:
                        re[i][j] = 0
                        check = False
                    if not check:
                        break
                if not check:
                    break
    result = [[0 for i in row] for row in matrix]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == re[i][j]:
                result[i][j] = 0
            else:
                result[i][j] = 1
    return result


data = input().strip()
while len(data) == 0:
    data = input().strip()

f = int(data)
fil = []
for i in range(f):
    row = [int(j) for j in input().split()]
    fil.append(row)

n = int(input())
matrix = []
for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

result_matrix = boundary_ex(f, n, fil, matrix)

for row in result_matrix:
    for i in row:
        print(i, end=' ')
    print()