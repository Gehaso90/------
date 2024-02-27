# Задание 2
# Пользователь вводит с клавиатуры два числа (начачисла в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start > end:
    print("Начало диапазона не может быть больше конца.")
    exit()

print("\n1. Все числа диапазона:")
for num in range(start, end + 1):
    print(num)

print("\n2. Все числа диапазона в убывающем порядке:")
for num in range(end, start - 1, -1):
    print(num)

print("\n3. Все числа, кратные 7:")
for num in range(start, end + 1):
    if num % 7 == 0:
        print(num)

print("\n4. Количество чисел, кратных 5:")
count = 0
for num in range(start, end + 1):
    if num % 5 == 0:
        count += 1
print(count)