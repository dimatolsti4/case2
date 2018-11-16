
import local

tax = 0
year_income = 0
print(local.INCOME_INPUT) 

for month in range(12):             #ввод зарплаты за год помесячно
    month_income = int(input())
    year_income += month_income
print(year_income)

category = int(input(local.CATEGORY_INPUT)) #ввод вашей категеории для подсчета налогов
if category == 1: //подсчет для 1 категории
    if year_income <= 9075:
        tax = year_income*0.1
    elif year_income <= 36900:
        tax = 9075*0.1 + (year_income - 9075)*0.15
    elif year_income <= 89350:
        tax = 9075*0.1 + 27824*0.15 + (year_income - 36901)*0.25
    elif year_income <= 186350:
        tax = 9075*0.1 + 27824*0.15 + 52449*0.28 + (year_income - 89351)*0.28
    elif year_income <= 405100:
        tax = 9075*0.1 + 27824*0.15 + 52449*0.25 + 96999*0.28 + (year_income - 186351)*0.33
    elif year_income <= 406750:
        tax = 9075*0.1 + 27824*0.15 + 52449*0.25 + 96999*0.28 + 218749*0.33 + (year_income - 405101)*0.35
    else:
        tax = 9075*0.1 + 27824*0.15 + 52449*0.25 + 96999*0.28 + 218749*0.33 + 1649*0.35 + (year_income - 406751)*0.396

if category == 2:  #подсчет для 2 категории
    if year_income < 18150:
        tax = year_income*0.1       
    elif year_income <= 73800:
        tax = 1815*10.1 + (year_income - 18151)*0.15       
    elif year_income <= 148850:
        tax = 18151*0.1 + 55649*0.15 + (year_income - 73801)*0.25     
    elif year_income <= 226850:
        tax = 18151*0.1 + 55649*0.15 + 75049*0.25 + (year_income - 148851)*0.28    
    elif year_income <= 405100:
        tax = 18151*0.1 + 55649*0.15 + 75049*0.25 + 77999*0.28 + (year_income - 226851)*0.33   
    elif year_income <= 457600:
        tax = 18151*0.1 + 55649*0.15 + 75049*0.25 + 77999*0.28 + 178249*0.33 + (year_income - 405101)*0.35   
    else:
        tax = 18151*0.1 + 55649*0.15 + 75049*0.25 + 77999*0.28 + 178249*0.33 + 52499*0.35 + (year_income - 457601)*0.396
       
if category == 3: #подсчет для 3 категории
    if year_income <=12950:
        tax = year_income*0.1        
    elif year_income <= 49400:
        tax = 12950*0.1 + (year_income-12950)*0.15      
    elif 127550 >= year_income:
        tax = 12950*0.1 + 36449*0.15 + (year_income - 49401)*0.25       
    elif year_income <= 206600:
        tax = 12950*0.1 + 36449*0.15 + 78149*0.25 + (year_income - 127551)*0.28
    elif year_income <= 405100:
        tax = 12950*0.1 + 36449*0.15 + 78149*0.25 + 79049*0.28 + (year_income - 206601)*0.33      
    elif year_income <= 432200:
        tax = 12950*0.1 + 36449*0.15 + 78149*0.25 + 79049*0.28 + 198499*0.33 + (year_income - 405101)*0.35
    else:
        tax = 12950*0.1 + 36449*0.15 + 78149*0.25 + 79049*0.28 + 198499*0.33 + 27099*0.35 + (year_income - 432201)*0.396
print(round(tax)) #вывод  налога
end = int(input())
