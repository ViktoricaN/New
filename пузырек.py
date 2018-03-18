elem = [1,5,-8,0,2,42,-9]

def bubble(myelem):
    last_i = len(myelem) - 1
    for a in range(0, last_i):
        for x in range(0, last_i):
            if myelem[x] > myelem[x+1]:
                b = myelem[x]
                myelem[x] = myelem[x+1]
                myelem[x+1] = b
    return myelem

print(elem)
new_elem = bubble(elem)
print(new_elem)
