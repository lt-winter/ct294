def myFn(n):
    for i in range(1, n + 1):
        print(f"{i}:{i * i}", end=" ")


myNum = int(input("Nhập 1 số nguyên: "))
myFn(myNum)
