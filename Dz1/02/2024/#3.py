# Пользователь вводит с клавиатурыдва числа. Нужно 
# посчитать отдельно сумму четных, нечетных и чисел, 
# кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start > end:
    print("Начало диапазона не может быть больше конца.")
    exit()

sum_even = 0
sum_odd = 0
sum_multiples_of_9 = 0
count_multiples_of_9 = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
    if num % 9 == 0:
        sum_multiples_of_9 += num
        count_multiples_of_9 += 1

print("\nСумма четных чисел:", sum_even)
print("Среднее арифметическое четных чисел:", sum_even / (end - start + 1) if count_multiples_of_9 > 0 else 0)
print("\nСумма нечетных чисел:", sum_odd)
print("Среднее арифметическое нечетных чисел:", sum_odd / (end - start + 1) if count_multiples_of_9 > 0 else 0)
print("\nСумма чисел, кратных 9:", sum_multiples_of_9)
print("Среднее арифметическое чисел, кратных 9:", sum_multiples_of_9 / count_multiples_of_9 if count_multiples_of_9 > 0 else 0)