def perfect(n):
    sum = 0;
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            sum += i
    return sum == n


n = int(input("Nhập n: "))
print(perfect(n))
