ABC_Rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ABC_Eng = "abcdefghijklmnopqrstuvwxyz"
message = input("Введите сообщение: ")
number = int(input("Введите число сдвига: "))
new_word = " "
for letter in message:
    if (letter != ' '):  #пока не встретится перенос строки
        new_word += " ".join(chr(ord(letter) + number))   #сборка строки со сдвигом вправо на введенное число

print(new_word)