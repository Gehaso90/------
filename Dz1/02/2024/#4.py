# Пользователь вводит с клавиатуры длину линии и 
# символ для заполнения линии. Нужно отобразить на 
# экране вертикальную линию из введенного символа, 
# указанной длины. 
# Например, если было введено 5 и символ %, тогда 
# вывод на экран будет такой:
# %
# %
# %
# %
# %


n = int(input("Введите длину линии: "))
symbol = input("Введите символ для заполнения линии: ")


for i in range(n):
    print(symbol, end="")