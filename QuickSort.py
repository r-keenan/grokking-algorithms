def quick_sort(array):
    # base case
    if len(array) < 2:
        return array
    else:
        # recursive case
        pivot = array[0]
        # Sub-array of all the elements of less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # Sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([10, 5, 2, 3]))