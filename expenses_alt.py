'''
Написати додаток, який допоможе нам керувати бюджетом

Бюджет на тиджень не більше 1000

Пн - 100
Вт - 200
Ср - 100
Чт - 100
Пт - 50

Поки що написати додаток який це все зберігає
'''

WEEK_DAYS = ('Понеділок', 'Вівторок', 'Середа')

print("Вітаю у додатку для бюджету")
budget = int(input("Введіть максимальний бюджет на тиждень: "))
print('Ваш бюджет')
print(budget)

expenses_dict = {}

# for i in range(3):
#     # expenses_list.append(int(input("Введіть витрати в " + WEEK_DAYS[i] + ": ")))
#     ...

for day in WEEK_DAYS:
    expenses_dict[day] = int(input("Введіть витрати в " + day + ": "))

print(expenses_dict)

total_expenses = sum(expenses_dict.values())
print('Загальні витрати: ' + str(total_expenses))
print(f'Загальні витрати: {total_expenses}')

print(f'Результат: {budget - total_expenses}')
