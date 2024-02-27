# Функция для вычисления площади ромба
def romboid_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

# Ввод пользователем длин диагоналей
diagonal1 = float(input("Введите длину первой диагонали ромба: "))
diagonal2 = float(input("Введите длину второй диагонали ромба: "))

# Вычисление площади ромба
area = romboid_area(diagonal1, diagonal2)

# Вывод площади ромба
print("Площадь ромба:", area)