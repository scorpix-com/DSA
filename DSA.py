
# ⚠️ Bubble Sort

arr = [1,5,7,3,2]

n = len(arr)
swap = False

for i in range(n -1):
    for j in range(n -1):
        if arr[j] > arr[j + 1]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            swap = True
    print(arr)
    if swap == False:
        break
    else:
        swap = False

print(f"Result: {arr}")