def thresholding_image(threshold, matrix):
    thresholding_matrix = [[255 if point > threshold else 0 for point in row] for row in matrix]
    return thresholding_matrix


def main():

    threshold = int(input())
    n = int(input())
    matrix = []
    for i in range(n):
        row = [int(j) for j in input().split()]
        matrix.append(row)

    result = thresholding_image(threshold, matrix)

    for row in result:
        for point in row:
            print(point, end=' ')
        print()


if __name__ == '__main__':
    main()