from collections import Counter


def revenue(sizes_, purchases_):
    profit_ = 0
    for purchase in purchases_:
        if purchase[0] in sizes_:
            if sizes_[purchase[0]] == 1:
                sizes_.pop(purchase[0])
            else:
                sizes_[purchase[0]] -= 1
            profit_ += purchase[1]
    return profit_


if __name__ == '__main__':
    arrayLength = int(input())
    array = list(map(int, input().split()))
    sizes = Counter(array)
    purchasesLength = int(input())
    purchases = []
    for i in range(purchasesLength):
        new_purchase = tuple(map(int, input().split()))
        purchases.append(new_purchase)

    profit = revenue(sizes, purchases)
    print(profit)

