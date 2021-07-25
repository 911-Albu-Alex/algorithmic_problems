if __name__ == "__main__":
    values = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        new_value = [name, score]
        ok = False
        for i in range(len(values)):
            if score < values[i][0]:
                values.insert(i, new_value)
                ok = True
                break
            elif score == values[i][0]:
                if name < values[i][1]:
                    values.insert(i, new_value)
                    ok = True
                    break
                else:
                    values.insert(i+1, new_value)
                    ok = True
                break

        if not ok:
            values.append(new_value)

    for i in range(1,len(values)):
        if values[i][0] > values[0][0]:
            new_value = values[i][0]
            print(values[i][0])
            i += 1
            while i < len(values) and values[i][0] == new_value:
                print(values[i][0])
                i += 1
