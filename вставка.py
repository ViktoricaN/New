def insertion(array):
    a = array
    for i in range(len(a)):
        b = a[i]
        j = i
        while (a[j - 1] > b) and (j > 0):
            a[j] = a[j - 1]
            j = j - 1
        a[j] = b
        """print(a)"""
    return a


elem = [-74, 1, -2, 7, 52, 3, 4, 6, 3, 2]
print(insertion(elem))

