salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
money =0
summ = spend
for i in range(2, months + 1):
    spend = spend * 1.03
    summ = summ + spend
print( int(summ - salary * months) )

