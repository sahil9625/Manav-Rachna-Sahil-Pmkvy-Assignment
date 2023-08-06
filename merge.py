def sort(nums):
    if len(nums) <= 1:
        return nums
    
    # Divide the array into two halves
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]
    
    # Recursively sort each half
    left_half = sort(left_half)
    right_half = sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    # Append any remaining elements from the left and right arrays
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    print(nums)
    
    return merged


# Example usage:
nums = [64, 34, 25, 12, 22, 11, 90]
sort(nums)
print("Sorted array:", nums)
