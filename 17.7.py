array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
comparison = 0
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array) - i - 1):
        comparison += 1
        if array[j] < array[idx_min + 1]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min + 1] = array[idx_min + 1], array[i]

print(comparison)