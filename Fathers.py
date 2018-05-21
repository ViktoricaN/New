fathers = {
    "Niklaus Wirth":"Pascal",
    "Rasmus Lerdorf":"Php",
    "Larry Wall":"Perl",
    "Brian Kernighan":"Awk",
    "Don Syme": "F#",
    "James Gosling":"Java",
    "Simon Cozens":"Parrot",
    "Jeremy Ashkenas": "CoffeeScript",
    "Guido van Rossum":"Python",
    "Yukihiro Matsumoto": "Ruby",
    "Bjarne Stroustrup": "C++",
    "Thomas Kurtz": "Basic"
}
dictionary = input('Введите List или Name: ')   #что необходимо вывести: список основателей или имя и язык
if dictionary == 'Name':
    Name = input("Введите имя: ")
    for name, value in fathers.items():   #возврвщвет данные из списка и их значения
        if name == Name:
            print(Name, 'создал язык', fathers[name])  #выводит имя и язык, зависящий от этого имени
else:
    if dictionary == 'List':
        Name = sorted(fathers.keys())   #сортировка списка
        for work in Name:
            print(work,'разработал', fathers[work])