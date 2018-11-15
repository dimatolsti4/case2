"""Case-study #0 My first code
Developers:
Timofeev A (60%), Ignatov G(40%), Rodionov D(20%) 

""" 


import local

tax= 0
year_income = 0

print('Введите свой доход за месяц\n')

for month in range(12):
    month_income = int(input())
    year_income+=month_income

print(year_income)

category = int(input(local.slovo))

if category==1:
    if year_income<9075:
        tax=year_income0.1
        print(tax)

    if (year_income>9075) and (year_income<36900):
        tax = 90750.1+(year_income-9075)0.15
        print(tax)

    if (year_income>36901) and (year_income<89350):
        tax = 90750.1+278240.15+(year_income-36901)0.25
        print(tax)

    if (year_income>89351) and (year_income<186350):
        tax = 90750.1+278240.15+524490.28+(year_income-89351)0.28
        print(tax)

    if (year_income>186351) and (year_income<405100):
        tax = 90750.1+278240.15+524490.25+969990.28+(year_income-186351)0.33
        print(tax)

    if (year_income>405101) and (year_income<406750):
        tax = 90750.1+278240.15+524490.25+969990.28+2187490.33+(year_income-405101)0.35
        print(tax)

    if (year_income>406751):
        tax = 90750.1+278240.15+524490.25+969990.28+2187490.33+16490.35+(year_income-406751)0.396
        print(tax)
if category == 2:
    if year_income < 18150:
        tax = year_income0.1
        print(tax)
    if (year_income > 18151) and (year_income < 73800):
        tax = 181510.1 + (year_income - 18151)0.15
        print(tax)
    if (year_income > 73801) and (year_income < 148850):
        tax = 181510.1 + 556490.15 + (year_income - 73801)0.25
        print(tax)
    if (year_income > 148851) and (year_income < 226850):
        tax = 181510.1 + 556490.15 + 750490.25 + (year_income - 148851)0.28
        print(tax)
    if (year_income > 226851) and (year_income < 405100):
        tax = 181510.1 + 556490.15 + 750490.25 + 779990.28 + (year_income - 226851)0.33
        print(tax)
    if (year_income > 405101) and (year_income < 457600):
        tax = 181510.1 + 556490.15 + 750490.25 + 779990.28 + 1782490.33 + (year_income - 405101)0.35
        print(tax)
    if (year_income > 457601):
        tax = 181510.1 + 556490.15 + 750490.25 + 779990.28 + 1782490.33 + (year_income - 457601)*0.396
        print(tax)
if category==3:
    if year_income<12950:
        tax=year_income0.1
        print(tax)

    if (year_income>12950) and (year_income<49400):
        tax = 129500.1+(year_income-12950)0.15
        print(tax)

    if (year_income>49401) and (year_income<127550):
        tax = 129500.1+364490.15+(year_income-49401)0.25
        print(tax)

    if (year_income>127551) and (year_income<206600):
        tax = 129500.1+364490.15+781490.25+(year_income-127551)0.28
        print(tax)

    if (year_income>206601) and (year_income<405100):
        tax = 129500.1+364490.15+781490.25+790490.28+(year_income-206601)0.33
        print(tax)

    if (year_income>405101) and (year_income<432200):
        tax = 129500.1+364490.15+781490.25+790490.28+1984990.33+(year_income-405101)0.35
        print(tax)

    if (year_income>432201):
        tax = 129500.1+364490.15+781490.25+790490.28+1984990.33+270990.35+(year_income-432201)0.396
        print(tax)
