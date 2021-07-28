sequence = input("Введите числа через пробел:").split()
additional_number = input("Добавьте еще одно любое число")
sequence.append(additional_number)

for i in range(1, len(sequence)):
    x = sequence[i]
    idx = i
    while idx > 0 and sequence[idx-1] > x:
        sequence[idx] = sequence[idx-1]
        idx -= 1
    sequence[idx] = x

def binary_search(list, item):
  low = 0
  high = len(list) - 1
  i = 0
  while low <= high:
    mid = (low + high) // 2
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
    i=i+1

bsl = binary_search(sequence, additional_number) - 1
bsr = binary_search(sequence, additional_number) + 1
print(bsl, bsr)