def plusMinus(arr):
    positive_numbers = 0.00
    negative_numbers = 0.00
    zero_numbers = 0.00

    for number in arr:
        if number < 0:
            negative_numbers += 1.00
        elif number > 0:
            positive_numbers += 1.00
        else:
            zero_numbers += 1.00

    print('{0:.6f}'.format(positive_numbers/len(arr)))
    print('{0:.6f}'.format(negative_numbers / len(arr)))
    print('{0:.6f}'.format(zero_numbers / len(arr)))


if __name__ == "__main__":

    arr = [1, 1, 0, -1, -1]
    plusMinus(arr)
