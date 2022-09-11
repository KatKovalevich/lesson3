# задача 1

def division (a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
print(division(int(input('Первое число: ')), int(input('Второе число: '))))

# задача 2

def personal_data(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')
personal_data (name = input('Имя:'),
              lastname = input('Фамилия:'),
              year_of_birth = input('Год рождения:'),
              city = input('Город проживания:'),
              email = input('email:'),
              phone = input('Телефон:'))

# задача 3

def my_func(a, b, c):
    print(f'Сумма двух наибольших аргументов равна: {a + b + c - min ([a, b, c])}')
my_func(int(input('a:')),
    int(input('b:')),
    int(input('c:')),)

# задача 4

def my_func(x, y):
    return x ** abs(y-1)
print(f'Возведение в степень: '
      f'{my_func(int(input("Основание степени x: ")), int(input("Показатель степени y: ")))}')

# задача 5 
def my_num():
    summ = 0
    while True:
            s = input('Введите числа: ')
            if s == '#':
                break
            for n in map(int, input('Введите числа: ').split()):
                s += n
                print(s)
    print(summ)

# задача 6-7
def int_func (*args):
    text = input("Input words ")
    print(text.title())
    return
int_func()



