money = int(input("Сдача: "))
if money > 0 and money <= 999:
    for i in range(money):
        s1 = money // 50
        s11 = money - 50 * s1
        s2 = s11 // 10
        s22 = s11 - 10*s2
        s3 = s22 // 5
        s33 = s22 - 5*s3
        s4 = s33 // 1
print(s1,s2,s3,s4)