def selection(array):
    a = array
    for i in range(len(a)):
        iMin = i
        for j in range(i+1, len(a)):
            if a[j] < a[iMin]:
                iMin = j
        tmp = a[iMin]
        a[iMin] = a[i]
        a[i] = tmp
    return a

elem = [0,-3,5,1,-34,4,2]
print(selection(elem))
