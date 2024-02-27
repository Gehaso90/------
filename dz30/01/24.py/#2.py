def get_user_choice():
    print("Выберите действие:")
    print("1. Найти максимум из трёх чисел")
    print("2. Найти минимум из трёх чисел")
    print("3. Найти среднеарифметическое трёх чисел")
    choice = int(input("Введите номер действия: "))
    while choice not in [1, 2, 3]:
        print("Некорректный ввод. Введите номер действия: ")
        choice = int(input("Введите номер действия: "))
    return choice

def get_numbers():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    return a, b, c

def calculate_max(a, b, c):
    return max(a, b, c)

def calculate_min(a, b, c):
    return min(a, b, c)

def calculate_average(a, b, c):
    return (a + b + c) / 3

def main():
    choice = get_user_choice()
    a, b, c = get_numbers()

    if choice == 1:
        print("Максимум из трёх чисел: ", calculate_max(a, b, c))
    elif choice == 2:
        print("Минимум из трёх чисел: ", calculate_min(a, b, c))
    elif choice == 3:
        print("Среднеарифметическое трёх чисел: ", calculate_average(a, b, c))

if __name__ == "__main__":
    main()