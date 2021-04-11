def runner_up(arr):
    maximum_value = max(arr)
    runner_up_score = -101
    for index in range(len(arr)):
        if maximum_value > arr[index] > runner_up_score:
            runner_up_score = arr[index]

    return runner_up_score


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(runner_up(arr))