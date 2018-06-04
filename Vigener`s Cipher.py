ABC_Rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
message = input("Введите сообщение: ")
line = message.lower()  #преобразование строки
key = input("Введите ключ: ")
key *= len(message) // len(key) + 1  #новый ключ
new_word = ''.join([chr((ord(j) + ord(key[i])) % 33 + ord('а')) for i, j in enumerate(line)])  # шифруем
print(new_word)