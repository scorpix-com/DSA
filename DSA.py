
#⚠️ Insertion Sort

arr = [10, 12, 5, 6, 2,4]

for i in range(1, len(arr)):
    curr = arr[i]
    j = i - 1               # Sorted array beginning
    while j >= 0 and curr < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = curr

print(arr)