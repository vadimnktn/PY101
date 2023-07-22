salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
# Логика такая - считаем все затраты с учетом подорожания за 10 мес
# вычитаем ЗП за 10 мес - получаем подушку.

i = 0                   # Счетчик месяцев
zatraty = spend         # Затраты за конкретный месяц
zatraty_sum = 0         # Суммарные затраты за предыдущие и этот месяцы

#Считаем расходы в цикле
for i in range(0, 10):
    if i == 0:
        zatraty_sum += spend  			         # Первый месяц без повышения
    else:
        zatraty = zatraty * (1 + increase)       # Повышает каждый месяц затраты на increase
        zatraty_sum += zatraty                   # Суммирует их в переменную

# Суммарно подушка безопасности покрывает общую сумму
# затрат из цикла за 10 месяцев минус ЗП за эти 10 месяцев
money_capital = round(zatraty_sum - months * salary)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
