height = int(input("Высота пирамиды: "))
if height >= 0 and height <= 23:
    for i in range(height):
        print(' ' * (height-i-1) + '#' * (i+2))