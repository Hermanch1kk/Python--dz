def product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
#-------------------------------

def find_minimum(numbers):
    if not numbers:
        raise ValueError("Список не повинен бути порожнім")
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value
numbers = [5, 3, 8, 1, 9, 2]
minimum = find_minimum(numbers)
print(f"Мінімум y списку {numbers} є {minimum}")
#--------------------------------------------------------------


def is_prime(num):
    """ Перевіряє, чи є число `num` простим. """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt_num = int(num**0.5) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False
    return True
def count_primes(numbers):
    """ Підраховує кількість простих чисел у списку `numbers`. """
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count
#--------------------------------------------------------------------

def remove_elements(numbers, element_to_remove):
    """ Видаляє зі списку `numbers` всі входження числа `element_to_remove` i повертає кількість видалених елементів. """
    count_removed = 0
    i = 0
    while i < len(numbers):
        if numbers[i] == element_to_remove:
            numbers.pop(i)
            count_removed += 1
        else:
            i += 1
    return count_removed
#----------------------------------------------------------------------------------------------------------------------------

def merge_lists(list1, list2):
    """ Об'єднує два списки `list1` і `list2` і повертає новий список з усіма їх елементами. """
    merged_list = list1 + list2
    return merged_list
#---------------------------------------------------------------------------------------------------


def calculate_powers(numbers, power):
    """ Обчислює ступінь `power` для кожного елемента у списку `numbers`. """
    powered_numbers = [num ** power for num in numbers]
    return powered_numbers
#------------------------------------------------------------------------------