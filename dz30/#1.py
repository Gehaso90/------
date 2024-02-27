a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

choice = input("Выберите действие (сумма/произведение): ")

if choice == "сумма":
    sum = a + b + c
    print("Сумма:", sum)
elif choice == "произведение":
    product = a * b * c
    print("Произведение:", product)
else:
    print("Некорректный выбор")