#features in this project we have 1. income add and 2.rent expense 3.food expense 4.study expense 5.total  calculate
income = float(input("ENTER YOUR INCOME  "))
max_income = 200000

if income < 1000 or income > max_income:
    print("invalid value")
    raise SystemExit

print(income)

rent_expense = float(input("ENTER YOUR RENT EXPENSE  : "))
if rent_expense < 1000 or rent_expense > 12000:
    print("invalid value")
    raise SystemExit
print(rent_expense)
food_expense = float(input("ENTER YOUR FOOD EXPENSE  : "))    

if food_expense < 1000 or food_expense > 12000:
    print("invalid value")
    raise SystemExit
print(food_expense)

study_expense= float(input("ENTER YOUR STUDY EXPENSE  : "))  

if study_expense < 0 or study_expense > 10000:
    print("invalid value")
    raise SystemExit
print(study_expense) 
total_expense =income-rent_expense-food_expense-study_expense
print(total_expense)
remain_balance = total_expense
transport_expense = float(input("enter transport expense : "))
if transport_expense < 0 or transport_expense > 5000:
    print("invalid value")
    raise SystemExit
print(transport_expense)

mobile_expense = float(input("enter mobile/internet expense : "))
if mobile_expense < 0 or mobile_expense > 1500:
    print("invalid value")
    raise SystemExit
print(mobile_expense)

personal_expense = float(input("enter personal expense : "))
if personal_expense < 0 or personal_expense > 8000:
    print("invalid value")
    raise SystemExit
print(personal_expense)

savings = float(input("enter savings : "))
if savings < 0 or savings > 20000:
    print("invalid value")
    raise SystemExit
print(savings)
emergency = remain_balance-transport_expense-mobile_expense-personal_expense-savings


remain_money=emergency
print(remain_money)

