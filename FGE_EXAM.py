x = [1, 2, 3, 4, 5]
y = []
z = []

y.append(x.pop())
y.append(x.pop())

z.append(x.pop())
z.append(x.pop())
z.append(x.pop())

z.sort(reverse=False)

print('x =', x)
print('y = ', y)
print('z = ', z)


x = [1, 2, 21, 33, 45, 65, 12]

print()
print("Insertion Sort Algorithm to sort the list Before descending order: ")
print(x)
array = []
for i in range(1,len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]:
        array[j+1]=array[j]
        j-=1
        array[j+1] = key
        x.sort(reverse= False)
print("Insertion Sort Algorithm to sort the list After descending order: ")
print(x)

print()
x = [1, 2, 21, 33, 45, 65, 12]
print("Selection Sort Algorithm to sort the list Before ascending order: ")
print(x)
for i in range(len(array)):
    min_idx = i
    for j in range (i + 1, len(array)):
        min_idx = arr[i], arr[min_idx] = arr[min_idx], arr[i]
        x.sort()
print("Selection Sort Algorithm to sort the list After ascending order: ")
print(x)
