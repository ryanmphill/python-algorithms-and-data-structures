def binary_search(list, target) -> int or None:
    """ 
    Returns the index position of the target if found,
    else returns None.
    
    It is assumed that 'list' is already sorted, otherwise, the algorithm
    won't return the expected result

    Time Complexity: O(log n)
    """
    first = 0
    last = len(list) - 1 # len() is a constant time operation in python

    while first <= last:
        # Floor division (//) rounds down to 
        # nearest whole number
        midpoint = (first + last)//2
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)