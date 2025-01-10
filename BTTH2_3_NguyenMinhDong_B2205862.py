def createDict(n):
    dict = {}
    for i in range (1, n + 1):
        dict.update({i: i * i})
    return dict


n = int(input("Nhap so nguyen n: "))
dict = createDict(n)
print(dict)
