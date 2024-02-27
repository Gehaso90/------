def fizz_buzz(number):
    if number < 1 or number > 100:
        print("Ошибка: Введенное число не входит в диапазон от 1 до 100")
        return
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

while True:
    try:
        number = int(input("Введите число в диапазоне от 1 до 100: "))
        fizz_buzz(number)
    except ValueError:
        print("Ошибка: Введено некорректное значение. Пожалуйста, введите число.")
    else:
        break