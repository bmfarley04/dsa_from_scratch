def binary_search(nums, target):

    top = len(nums) - 1
    bottom = 0

    while top >= bottom:

        choice = top + bottom // 2

        if nums[choice] == target:
            return choice
        elif nums[choice] > target:
            top = choice - 1
        else:
            bottom = choice + 1
    return -1

        
            

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums1 = [1,2,3,4,5,6]
print(binary_search(nums, 10))
