array=list(map(int, input('Список чисел через пробел').split()))
element=int(input('Введите число'))
def proverka():
    while type:
        try:
            array

            if len(array)==0:
                raise ValueError
        except ValueError:
            print("Неверный формат данных")
        else:
            break
proverka()
def sort():

    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array
sort()
sp = []
for idx, val in enumerate(array):
    sp.append(idx)
left = sp[0]
right = sp[-1]
def binary_search(array, element, left, right):
    while left < right:
        middle = (left + right) // 2
        if array[middle] < element:
            left = middle + 1
        else:
            right = middle
        if left > 0 and array[left] != element:
            c=(array[left - 1])
        else:
            c=(array[left])
    return print(c)
(binary_search(array, element, left, right))
