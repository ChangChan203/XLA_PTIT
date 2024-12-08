data = input().strip()
while len(data) == 0:
    data = input().strip()

n = int(data)
m = []
for i in range(n):
    row = [float(j) for j in input().split()]
    m.append(row)

for i in range(n):
    for j in range(n):
        oldpix = float(m[i][j])
        newpix = float(255) if oldpix > 127 else float(0)
        error = oldpix - newpix
        m[i][j] = newpix

        if j + 1 < n:
            m[i][j + 1] += error * 7 / 16

        if i + 1 < n:
            if j - 1 >= 0:
                m[i + 1][j - 1] += error * 3 / 16

            if j + 1 < n:
                m[i + 1][j + 1] += error / 16

            m[i + 1][j] += error * 5 / 16

for row in m:
    for i in row:
        print(int(i), end=' ')
    print()