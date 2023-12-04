def merge_sort(list):
    """
    Sorts a list in ascending order

    Returns a new sorted list

    Divide: Find the midpoint of the list and
    divide into sublists

    Conquer: Recursively sort the sublists created
    in a previous step
    
    Combine: Merge the sorted sublists created in previous step

    Takes O(n * log n) time generally, but O(kn log n) in this example
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists

    Returns two sublists - left and right

    Takes overall O(log n) time

    NOTE: In reality, the slicing operation in Python takes O(k) time,
    where k is the size of the slice, giving an overall time complexity of O(k log n)
    """

    mid = (len(list)//2)
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process

    Returns a new merged list

    Takes overall O(n) time
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    
    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

a_list = [54, 62, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(a_list)
print(l)

def verify_sorted(list):
    n = len(list)

    if n == 0 or n== 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

print("Is a_list sorted? ", verify_sorted(a_list))
print("Is l sorted? ", verify_sorted(l))