def get_user_choice():
    print("Выберите единицу измерения:")
    print("1. Мили")
    print("2. Дюймы")
    print("3. Ярды")
    choice = int(input("Введите номер единицы измерения: "))
    while choice not in [1, 2, 3]:
        print("Некорректный ввод. Введите номер единицы измерения: ")
        choice = int(input("Введите номер единицы измерения: "))
    return choice

def get_meters():
    meters = float(input("Введите количество метров: "))
    return meters

def convert_meters_to_miles(meters):
    return meters * 0.000621371

def convert_meters_to_inches(meters):
    return meters * 39.37007874

def convert_meters_to_yards(meters):
    return meters * 1.0936133

def main():
    choice = get_user_choice()
    meters = get_meters()

    if choice == 1:
        print("Метры в мили: ", convert_meters_to_miles(meters))
    elif choice == 2:
        print("Метры в дюймы: ", convert_meters_to_inches(meters))
    elif choice == 3:
        print("Метры в ярды: ", convert_meters_to_yards(meters))

if __name__ == "__main__":
    main()