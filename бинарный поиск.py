def binar(list, found, begin, end):
    if begin > end:
        return "0"
    else:
        center = (begin + end) // 2
        if found == list[center]:
            return center
        elif found < list[center]:
            return binar(list, found, begin, center - 1)
        else:
            return binar(list, found, center + 1, end)

list = [1, 8, 0, -7, 3, 12, 11]
begin = 0
end = len(list)
found = 12

new = binar(list, found, begin, end)

if new == "0":
    print("not found")
else:
    print(new)