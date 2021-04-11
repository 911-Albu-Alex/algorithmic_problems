def diagonalDifference(arr):
    first_diagonal = 0
    second_diagonal = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                first_diagonal += arr[i][j]
            if i + j == len(arr) - 1:
                second_diagonal += arr[i][j]

    if first_diagonal > second_diagonal:
        return first_diagonal - second_diagonal
    else:
        return second_diagonal - first_diagonal


if __name__ == "__main__":

    arr = [[11, 2, 4]]
    arr.append([4, 5, 6])
    arr.append([10, 8, -12])

    result = diagonalDifference(arr)
    print(result)
