def invert_image_matrix(n, matrix):
    inverted_matrix = [[255 - pixel for pixel in i] for i in matrix]
    return inverted_matrix


def main():

    data = input().split()
    n = int(data[0])


    matrix = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index: index + n]))
        matrix.append(row)
        index += n

    result = invert_image_matrix(n, matrix)
    for i in result:
        print(' '.join(map(str, i)))


if __name__ == "__main__":
    main()
