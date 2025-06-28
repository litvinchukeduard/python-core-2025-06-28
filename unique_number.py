'''
Є список з деякими числами. Усі числа рівні, крім одного. Спробуйте знайти його!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

Гарантовано, що список містить щонайменше 3 числа.

Тести містять дуже великі масиви, тому подумайте про продуктивність.

Це перший ката в серії:

Знайти унікальне число (цей ката)
Знайти унікальний рядок
Знайти унікальний
'''

# [ 1, 1, 1, 2, 1, 1 ]
# [ -, -]
# [  , -, -]
# [  ,  , -, -]

def find_uniq(numbers_list: list[int]) -> int:
    # for i in range(6 - 1)
    for i in range(len(numbers_list) - 1):
        first_number = numbers_list[i]
        second_number = numbers_list[i + 1]
        if first_number != second_number:
            return second_number
        

print(find_uniq([ 2, 1, 1, 1, 1, 1 ])) # Fails on this option
