Zarplata = int(input("Введите зарплату: "))
Platez_po_kreditu = int(input("Введите сумму месячного платежа по кредиту: "))
Zadolzhennost_za_Kommunalnye_uslugi = int(input("Введите задолженность за коммунальные услуги: "))


Ostavshaya_summa = Zarplata - Platez_po_kreditu - Zadolzhennost_za_Kommunalnye_uslugi

print("Сумма, которая останется у пользователя после всех выплат: ", Ostavshaya_summa)