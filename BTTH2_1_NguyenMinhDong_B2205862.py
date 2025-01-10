def avg(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)

content = input("Nhập danh sách số, nhập $ để kết thúc: ")
list = []
while content != '$':
    content = int(content)
    list.append(content)
    content = input()

print("Trung bình của danh sách: ", avg(list))
