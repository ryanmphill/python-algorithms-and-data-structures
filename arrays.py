# Since this is Python, the values of the list aren't stored directly in memory.
# Instead, the values 1, 2, and 3 are stored elsewhere in memory, and
# the array (list) stores references to each of those values.
 
new_list = [1, 2, 3]
# To access a value, we use a subscript with the index of that value.
# Since the array has a reference to the base location in memory,
# the position of any element can be determined pretty easily. We don't
# have to iterate over the entire list.
# All we need to do is a simple calculation of an offset from the base memory
# since we're guaranteed that the memory is contiguous. 
# 
# (In a contiguous memory 
# allocation, elements are stored in consecutive memory locations, which makes 
# it easy to access them sequentially using indices or pointers.)
#
# For this reason, access is a constant time operation on an array or a
# Python list.
# This is also why an array crashes if you try
# to access a value using an index that is out of bounds of what the
# array stores.
result = new_list[0]
print(result)