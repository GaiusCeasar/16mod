number = list(map(int, input('Введите последовательность чисел через пробел').split()))
user_number = int(input('Теперь введите любое число'))
number.append(user_number)
#def sort():
for i in range(len(number)):
    for j in range(len(number) - i - 1):
        if number[j] > number[j + 1]:
            number[j], number[j + 1] = number[j + 1], number[j]

#print(number)


def binary_search(number, user_number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if number[middle] == user_number:
        return middle
    elif user_number < number[middle]:
        return binary_search(number, user_number, left, middle - 1)
    else:
        return binary_search(number, user_number, middle + 1, right)


number = [i for i in range(1,100)]

print(binary_search(number, user_number, 0, 99))
print('Наставники не судите строго=)')