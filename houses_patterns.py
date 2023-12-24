import math

def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Уравнение имеет бесконечное количество решений"
        else:
            return "Уравнение не имеет решений"
    else:
        return -b / a

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return "Уравнение не имеет действительных корней"

print("Выберите тип уравнения:")
print("1. Линейное уравнение (вида ax + b = 0)")
print("2. Квадратное уравнение (вида ax^2 + bx + c = 0)")

choice = input("Введите номер типа уравнения (1/2): ")

if choice == '1':
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    solution = solve_linear_equation(a, b)
    print("Решение уравнения:", solution)
elif choice == '2':
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    c = float(input("Введите значение c: "))
    solution = solve_quadratic_equation(a, b, c)
    print("Решение уравнения:", solution)
else:
    print("Неправильный ввод")