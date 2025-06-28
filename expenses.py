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

# print input
print("Вітаю у додатку для бюджету")
budget = int(input("Введіть максимальний бюджет на тиждень: "))
print('Ваш бюджет')
print(budget)

# set, list, tuple, dict

# {1, 1, 2} -> {2, 1}
# [1, 1, 2] -> [1, 1, 2] - список підходить
# (1, 1, 2) - не дуже зручно
# {'Пн': 100, 'Вт': 100} - теж підходить, але потрібно трохи більше тексту

expenses_list = []
# expenses_list.append(int(input("Введіть витрати в Понеділок: ")))
# expenses_list.append(int(input("Введіть витрати у Вівторок: ")))

for i in range(3):
    expenses_list.append(int(input("Введіть витрати в " + WEEK_DAYS[i] + ": ")))

print(expenses_list)

total_expenses = sum(expenses_list)

print('Загальні витрати: ' + str(total_expenses))
print(f'Загальні витрати: {total_expenses}')

print(f'Результат: {budget - total_expenses}')

# sum({1, 2, 3})

# monday_expenses = int(input("Введіть витрати в Понеділок: "))
# tuesday_expenses = int(input("Введіть витрати у Вівторок: "))
