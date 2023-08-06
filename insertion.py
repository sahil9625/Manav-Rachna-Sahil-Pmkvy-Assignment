def sort(nums):
    n = len(nums)
    for i in range(1, n):
        # Store the current element to be compared
        current_element = nums[i]
        
        # Find the position to insert the current element in the sorted part of the array
        j = i - 1
        while j >= 0 and nums[j] > current_element:
            nums[j + 1] = nums[j]  # Shift elements to the right
            j -= 1
        
        nums[j + 1] = current_element
        
        print(nums)  # Insert the current element in the correct position

# Example usage:
nums = [64, 34, 25, 12, 22, 11, 90]
sort(nums)

print("Sorted array:", nums)
