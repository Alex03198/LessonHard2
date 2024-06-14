for number in range(3, 21):
    code = []
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                code.append(str(i) + str(j))
    print(number, end=' - ')
    for n in code:
        print(n,  end="")
    print()