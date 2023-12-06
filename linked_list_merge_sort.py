from linked_list import LinkedList

# Here, we're going to split the function up into three parts:
# - The main function (merge sort)
# - A `split` function
# - And a `merge` function
# 
# There are much more concise implementations of merge sort
# in Python out there, but they are harder to explain.
#
# Splitting it up into three parts will help the merge sort
# be easier to understand

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order

    - Recursively divide the linked list into sublists 
    containing a single node
    - Repeatedly merge the sublists to produce sorted sublists
    until one remains

    Returns a sorted linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint
    into sublists
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1) # Subtract one because size is one greater than last index

        # Assign left_half as linked_list for now.
        # Once the right_half is assigned, we can sever it from
        # the left_half
        left_half = linked_list
        # Make a new instance of LinkedList for the right_half
        right_half = LinkedList()
        # Assign the node after the midpoint node as the head of
        # the newly created `right` linked list
        right_half.head = mid_node.next_node

        # Now we can sever the connection and essentially
        # make what was the `mid node` now the `tail node` of
        # the `left` linked list by assigning the next_node of the 
        # midpoint to `None`
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes

    Returns a new, merged list
    """

    # Create a new linked list that contains
    # nodes from merging left and right
    merged = LinkedList()

    # Add a `fake` head to the linked list so that when
    # adding sorted nodes, we can reduce the amount of
    # code needed by not worrying about whether we're at the
    # head of the list. Once we're done, we can assing the first 
    # sorted node as the head and discard the `fake` head.
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node
    # of either
    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next_node on right to set loop condition to false
            right_head = right_head.next_node
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next_node on left to set loop condition to false
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current
            # to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on left is greater than right, set current
            # to right node
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node
        # Move current to next node
        current = current.next_node
    
    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)
# Output:
# [Head: 200]-> [15]-> [44]-> [2]-> [Tail: 10]

sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
# Output:
# [Head: 2]-> [10]-> [15]-> [44]-> [Tail: 200]