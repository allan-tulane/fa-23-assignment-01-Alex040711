"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb
    pass

def longest_run(mylist, key):
    max_run_length = 0  # Maximum run length of key
    current_run_length = 0  # Current run length of key

    for item in mylist:
        if item == key:
            current_run_length += 1
            max_run_length = max(max_run_length, current_run_length)
        else:
            current_run_length = 0

    return max_run_length
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    def merge_results(left, right):
        # Combine results from left and right sublists
        left_size = left.left_size
        right_size = right.right_size

        longest_size = max(left.longest_size, right.longest_size,
                           left.right_size + right.left_size)

        is_entire_range = left.is_entire_range or right.is_entire_range

        return Result(left_size, right_size, longest_size, is_entire_range)

    def helper(start, end):
        if start == end:
            if mylist[start] == key:
                return Result(1, 1, 1, True)
            else:
                return Result(0, 0, 0, False)

        mid = (start + end) // 2

        # Recur for left and right halves
        left_result = helper(start, mid)
        right_result = helper(mid + 1, end)

        # Merge results from left and right halves
        merged_result = merge_results(left_result, right_result)

        # Check if we have a continuous sequence at the merge point
        if mylist[mid] == mylist[mid + 1] == key:
            merged_result.longest_size = max(
                merged_result.longest_size, left_result.right_size + right_result.left_size + 1)

        return merged_result

    # Call the helper function to start recursion
    return helper(0, len(mylist) - 1)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


