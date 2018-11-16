import local

tax = 0
year_income = 0

print(local.INCOME_INPUT)
for month in range(12):  # Ввод зарплаты за год помесячно
    month_income = int(input())
    year_income += month_income
print(year_income)

category = int(input(local.CATEGORY_INPUT))  # Ввод вашей категеории

if category == 1:  # Подсчет для 1 категории
    if year_income <= 9075:
        tax = year_income*0.1
    elif year_income <= 36900:
        tax = 9075*0.1 + (year_income - 9075)*0.15
    elif year_income <= 89350:
        tax = 5081.1 + (year_income - 36901)*0.25
    elif year_income <= 186350:
        tax = 19766.82 + (year_income - 89351)*0.28
    elif year_income <= 405100:
        tax = 46926.54 + (year_income - 186351)*0.33
    elif year_income <= 406750:
        tax = 119113.71 + (year_income - 405101)*0.35
    else:
        tax = 119690.86 + (year_income - 406751)*0.396

if category == 2:  # Подсчет для 2 категории
    if year_income < 18150:
        tax = year_income*0.1
    elif year_income <= 73800:
        tax = 1815 + (year_income - 18151)*0.15
    elif year_income <= 148850:
        tax = 10162.35 + (year_income - 73801)*0.25
    elif year_income <= 226850:
        tax = 28924.6 + (year_income - 148851)*0.28
    elif year_income <= 405100:
        tax = 50764.32 + (year_income - 226851)*0.33
    elif year_income <= 457600:
        tax = 109586.49+(year_income - 405101)*0.35
    else:
        tax = 127961.14 + (year_income - 457601)*0.396
if category == 3:  # Подсчет для 3 категории
    if year_income <= 12950:
        tax = year_income*0.1
    elif year_income <= 49400:
        tax = 1295 + (year_income-12950)*0.15
    elif 127550 >= year_income:
        tax = 6762.35 + (year_income - 49401)*0.25
    elif year_income <= 206600:
        tax = 26299.6 + (year_income - 127551)*0.28
    elif year_income <= 405100:
        tax = 48433.32 + (year_income - 206601)*0.33
    elif year_income <= 432200:
        tax = 113937.99 + (year_income - 405101)*0.35
    else:
        tax = 123422.64 + (year_income - 432201)*0.396
print(round(tax))  # Вывод  налога
end = int(input())
