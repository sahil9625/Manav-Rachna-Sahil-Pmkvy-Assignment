# in this sorting first we find the min value
def sort(nums):
    for i in range(5): #in this low index is 0 and high index is 5
        minpos = i  #minpos is minimum position minpos is i start with 0 then minpos is 0
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j
# swapping
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp 

        print(nums)       




nums = [5,20,4,7,9,2]    
sort(nums)

print(nums)