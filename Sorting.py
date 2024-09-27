array1 = [23, 89, 7, 56, 44]
print("1. Implement the Bubble Sort Algorithm for the Dataset and sort the data into ascending order")
print(array1)
for i in range(len(array1)):
    for j in range(0, len(array1) - i - 1):
        if array1[j] > array1[j + 1]: # change the condition from ascending to descending
            array1[j], array1[j + 1] = array1[j + 1], array1[j]
print("Bubble Sorted Ascending: ")
print(array1)
print()

array2 = [12, 78, 91, 34, 62]
print("2. Implement theInsertion Sort Algorithm for the Dataset and sort the data into ascending order.")
print(array2)
for i in range(1, len(array2)):
        key = array2[i]
        j = i - 1
        while j >= 0 and key < array2[j]: # change the condition from ascending to descending
            array2[j + 1] = array2[j]
            j -= 1
        array2[j + 1] = key
print("Insertion Sorted Ascending :")
print(array2)
print()

array3 = [5, 99, 48, 15, 67]
print("3. Implement the Selection Sort Algorithm for the Dataset and sort the data into descending order.")
print(array3)
n = len(array3)
for i in range(n):
    max_idx = i
    for j in range(i + 1, n):
        if array3[j] > array3[max_idx]:
            max_idx = j
    array3[i], array3[max_idx] = array3[max_idx], array3[i]
print("Selection Sorted Descending: ")
print(array3)
print()

array4 =  [38, 82, 25, 74, 13]
print("4. Implement the Insertion Sort Algorithm for the Dataset and sort the data into descending order.")
print(array4)
for i in range(1, len(array4)):
        key = array4[i]
        j = i - 1
        while j >= 0 and key > array4[j]:
            array4[j + 1] = array4[j]
            j -= 1
        array4[j + 1] = key
print("Insertion Sorted Descending: ")
print(array4)
print()

print("5. Sort the data into ascending order and descending order each order of the dataset is inserted into a separate list/array.")
copied_values = [array1[2], array1[3],
                 array3[2], array3[3],
                 array4[2], array4[3]]
ascending_sorted = sorted(copied_values)
print("Ascending Sorted Values:", ascending_sorted)
descending_sorted = sorted(copied_values, reverse=True)
print("Descending Sorted Values:", descending_sorted)
print()

print("6. Implement the Selection Sort Algorithm and sort the data into ascending order.")
combined_array = array1 + array2 + array3 + array4
def selection_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
sorted_combined_array = selection_sort_ascending(combined_array)
print("Selection Sorted Combined Dataset Ascending: ", sorted_combined_array)
print()

print("7. Print the even and odd values of the list/array created in item number.")
even_values = [i for i in sorted_combined_array if i % 2 == 0]
odd_values = [i for i in sorted_combined_array if i % 2 != 0]
print("Even Values:", even_values)
print("Odd Values:", odd_values)
