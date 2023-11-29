def linear_search_1(list, target):
    """
    Returns the index position of the target if found,
    else returns None.
    Time Complexity: O(n)
    """
    for i in range(0, len(list)): 
        if list[i] == target:
            return i
    return None

# The code can be cleaned up a bit by using 'enumerate' on the list
def linear_search_2(list, target):
    """
    Returns the index position of the target if found,
    else returns None.
    Time Complexity: O(n)
    """
    for index, value in enumerate(list):
        if value == target:
            return index
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search_2(numbers, 12)
verify(result) # 'Target not found in list'

result = linear_search_2(numbers, 6)
verify(result) # 'Target found at index 5'
