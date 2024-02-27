# # Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум, 
# # введенных чисел. Когда пользователь вводит число 7 
# программа прекращает свою работу и выводит на экран 
# надпись «Good bye!»



def main():
    numbers = []
    while True:
        number = float(input("Введите число (или 7 для остановки): "))
        if number == 7:
            break
        numbers.append(number)
        print("Текущая сумма:", sum(numbers))
        print("Текущий максимум:", max(numbers))
        print("Текущий минимум:", min(numbers))
    print("Good bye!")

if __name__ == "__main__":
    main()