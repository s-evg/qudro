"""Quadro v 0.2 / Author © s-evg"""

INFO = '''   \nДля решения квадратного уравнения вида:
a*x**2 + b*x + c = 0 введи последовательно
значения a, b, c, каждый раз нажимая Enter:\n'''

HELP = '''   \nВведено не верное значение, введите "y"
чтобы решить ещё одно уравнение,
или "n" чтобы выйти: '''

ERROR = ''' \nЭто не квадратное уравнение.
Коэффициент а не может быть равен нулю.
Введите верные значения.\n'''

EXIT = '''  \nСпасибо, что выбрали наше приложение.
До новых встреч!(❁´◡`❁)'''

UPS = '''   \nУпссс... (⊙_⊙;) Похоже Вы ошиблись
и ввели не числовые значения коэффициентов.
Попробуйте ещё раз, и будьте внимательны!\n'''

run = True
while run:
    print(INFO)

    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    c = float(input("Введите значение c: "))

    

    if a == 0:
        print(ERROR)
        run = True

    else:
        D = b ** 2 - 4 * a * c  # вычисляем дискриминант
        print("\nДискриминант D равен: ", D)

        if D > 0:
            X1 = (-b - D ** 0.5) / (2 * a)
            X2 = (-b + D ** 0.5) / (2 * a)
            print("X1 =", X1, "X2 =", X2)

        elif D == 0:
            print("X =", str(-b / 2 * a))

        else:
            print('Дискриминант D меньше 0, корней нет.¯\\_(ツ)_/¯')

        question = input('\nРешить ещё одно уравнение? y/n: ').lower()
        y_n = True

        while y_n:
            if question == 'y':
                run = True
                y_n = False

            elif question == 'n':
                print(EXIT)
                run = False
                y_n = False

            else:
                question = input(HELP).lower()
                y_n = True
                run = False