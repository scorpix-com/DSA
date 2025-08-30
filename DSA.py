
#  ⚠️ Merge sort


def MergeSort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[: middle]
        right = array[middle:]

        MergeSort(left)
        MergeSort(right)

        lp = 0
        rp = 0
        fp = 0
        while lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                array[fp] = left[lp]
                lp += 1
            else:
                array[rp] = right[rp]
                rp += 1
            fp += 1
        
        while lp < len(left):
            array[fp] = left[lp]
            lp += 1
            fp += 1
        while lp < len(right):
            array[fp] = right[rp]
            rp += 1
            fp += 1

array = [3, 2, 1, 4]
print("Before sorting: ",array)
MergeSort(array)

print("After sorting: ",array)