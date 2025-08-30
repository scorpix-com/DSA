
# ⚠️ Selection Sort

arr = [1,5,7,3,2]

n = len(arr)
for i in range(n -1):
    min=i
    for j in range(i + 1, n):
        if arr[j] < arr[min]:
            min = j
    arr[min], arr[i] = arr[i], arr[min]

print(arr)