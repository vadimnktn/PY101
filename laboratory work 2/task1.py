money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

month = 1
while money_capital + month * salary - spend * month >= 0:
    if month == 1:
        pass
    else:
        spend = spend * (1 + increase)
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
