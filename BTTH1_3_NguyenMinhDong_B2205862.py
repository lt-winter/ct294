def Floyd(n):
    current = 1
    row = 1
    for i in range (1, n):
        for j in range (1, i):
            print(current, end=" ")
            current += 1
        if (current > n): break;
        print("\n")

Floyd(15)