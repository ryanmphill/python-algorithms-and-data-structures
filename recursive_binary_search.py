from typing import List, Union

def recursive_binary_search_1(lst: List[Union[int, str]], target: Union[int, str]) -> bool:
    if len(lst) == 0:
        return False
    else:
        midpoint = (len(lst))//2

        if lst[midpoint] == target:
            return True
        else:
            if lst[midpoint] < target:
                return recursive_binary_search_1(lst[midpoint+1:], target)
            else:
                return recursive_binary_search_1(lst[:midpoint], target)

def verify(result):
    print(f"Target found: {result}")

numbers = [1,2,3,4,5,6,7,8]

result = recursive_binary_search_1(numbers, 12)
verify(result)

result = recursive_binary_search_1(numbers, 6)
verify(result)

# While this demonstrates how recursion works and provides a recursive implementation 
# of binary search, this is not a good implementation. Here is the correct implementation for the 
# recursive version of binary search.

# The function has been modified to accept a start and end position with default values of 0 and 
# None respectively. The default values allow us to pass a list and target without needing to specify 
# the arguments when invoking the function. Inside the body we set the appropriate values like we did 
# when setting first and last in the iterative approach.

# We then use start and end like we did in the iterative approach to keep track of the slice of the list 
# we're searching through. The big difference here is that with each recursive call, by passing in different 
# values for start and end we can define the slice of the list we're searching through. We're not actually 
# executing a slice operation and we use only one list in memory, but each recursive call now focuses on 
# a smaller slice of the original list.

# This definitely has implications for the runtime of our code. One important point is the cost of the 
# slice operation used in the recursive version of the function. A slicing 
# operation is not a constant time operation and has a runtime of O(k) where k represents the size of 
# the slice.

# With the modified (and correct) version of recursive binary search, since we're not executing slicing 
# operations we've eliminated that cost and our code now reflects the accurate runtime of the binary 
# search algorithm at O(log n).

# Slicing is also what lends to a space complexity of O(log n) for the original recursive version since 
# each slice required additional storage. Since we're not slicing the lsit anymore, the space complexity 
# is now constant - no additional storage is used.

# It's important to keep in mind that this doesn't change the fact that Python has a maximum recursion 
# depth and an iterative approach is still preferred.

def recursive_binary_search_2(lst: List[Union[int, str]], target: Union[int, str], start: int=0, end: Union[int, None]=None) -> int:
    if end is None:
        end = len(lst) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == lst[mid]:
        return mid
    else:
        if target < lst[mid]:
            return recursive_binary_search_2(lst, target, start, mid-1)
        else:
            return recursive_binary_search_2(lst, target, mid+1, end)

def verify(index):
    if index is not -1:
        print(f"Target found at index: {index}")
    else:
        print("Target not found")

result = recursive_binary_search_2(numbers, 12)
verify(result)

result = recursive_binary_search_2(numbers, 6)
verify(result)
