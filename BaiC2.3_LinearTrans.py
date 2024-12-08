def linear_transform(matrix, a, b):
    linear_matrix = [[(a * i + b) if (a * i + b) < 256 else 255 for i in row] for row in matrix]
    return linear_matrix


def main():
    data = input().split()
    while len(data) == 0:
        data = input().split()

    a = float(data[0])
    b = float(data[1])
    n = int(input())

    matrix = []
    for i in range(n):
        row = [int(j) for j in input().split()]
        matrix.append(row)

    result = linear_transform(matrix, a, b)

    for row in result:
        for i in row:
            print(int(i), end=' ')
        print()


if __name__ == '__main__':
    main()