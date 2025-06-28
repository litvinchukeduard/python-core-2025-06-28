'''
Дано список цілих чисел. Знайдіть те, яке зустрічається непарну кількість разів.

Завжди буде лише одне ціле число, яке зустрічається непарну кількість разів.
Приклади

[7] має повернути 7, оскільки воно зустрічається 1 раз (що непарно).

[0] має повернути 0, оскільки воно зустрічається 1 раз (що непарно).

[1,1,2] має повернути 2, оскільки воно зустрічається 1 раз (що непарно).

[0,1,0,1,0] має повернути 0, оскільки воно зустрічається 3 рази (що непарно).

[1,2,2,3,3,3,4,3,3,3,2,2,1] має повернути 4, оскільки воно зустрічається 1 раз (що непарно).
'''

def find_it(list_of_numbers: list[int]) -> int:
    # Потрібно порахувати скільки разів зустрічаються числа
    statistics_dict = {}
    for number in list_of_numbers:
        if number in statistics_dict:
            statistics_dict[number] += 1
        else:
            statistics_dict[number] = 1

    for number, statistic in statistics_dict.items():
        if statistic % 2 != 0:
            return number

# 1: 5
# 2: 3
# 6: 1

{1: 5, 2: 3, 6: 1}


list_of_numbers = [0,1,0,1,0]

statistics_dict = {}

# statistics_dict[0] += 1
# 0
# {0: 3} 
# + 1
# {0: 4}
# 1

for number in list_of_numbers:
    if number in statistics_dict:
        statistics_dict[number] += 1
    else:
        statistics_dict[number] = 1

print(statistics_dict)

for number, statistic in statistics_dict.items():
    if statistic % 2 != 0:
        print(number)       

# print(4 % 2)