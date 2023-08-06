def sort(nums):
    if len(nums) <= 1:
        return nums

    # Choose the pivot element (in this implementation, we choose the last element)
    pivot = nums[-1]

    # Partition the array into elements less than the pivot, the pivot itself, and elements greater than the pivot
    left = [x for x in nums[:-1] if x <= pivot]
    right = [x for x in nums[:-1] if x > pivot]

    print(nums)

    # Recursively sort the left and right sub-arrays
    return sort(left) + [pivot] + sort(right)

# Example usage:
nums = [64, 34, 25, 12, 22, 11, 90]
sort(nums)
print("Sorted array:", nums)
