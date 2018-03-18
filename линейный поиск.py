def line(key):
    stop = 0
    list = [1, 2, 8, 0, 4]
    for i in range(len(list)):
        if list[i] == key:
            print('yes', i)
            stop = 1
    if stop == 0:
        print('no found')


line(9)