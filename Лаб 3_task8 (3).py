money_capital = 10000
money = 1
salary = 5000
spend = 6000
increase = 0.05
month = 0
while money > 0:
    money = money_capital - spend *(1 + increase)
    money_capital = money + salary
    month = month +1
print(month - 1)
