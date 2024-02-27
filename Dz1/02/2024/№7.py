def power_function():
    number = int(input("Введите число: "))
    if number < 0:
        print("Ошибка: степень не может быть отрицательной.")
        return
    power = int(input("Введите степень (от 0 до 7): "))
    if power < 0 or power > 7:
        print("Ошибка: степень должна быть от 0 до 7 включительно.")
        return
    result = 1
    for _ in range(power):
        result *= number
    print(f"{number}^{power} = {result}")

while True:
    print("\n1. Рассчитать степень числа")
    print("2. Выход")
    choice = int(input("Введите номер действия: "))
    if choice == 1:
        power_function()
    elif choice == 2:
        break
    else:
        print("Ошибка: некорректный номер действия.")