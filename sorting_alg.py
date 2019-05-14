# Bubble sort
def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(len(L)):
            swap = True
            if L[j-1] > [j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j - 1] = temp 


def selection_sort(L):
    suffixSet = 0;
    while suffixSet != len(L):
        for i in range(suffixSet, len(L)):
            if L[i] > L[suffixSet]:
                L[suffixSet], L[i] = L[i], L[suffixSet]
        suffixSet += 1

# merge 
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])  
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])    
        j += 1
    return result
# merge sort
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])    
        right = merge_sort(L[middle:])
        return merge(left, right)

print(merge_sort([1,3,4,2,12,6,7]))