import time

def find_max(nums):
    max = 0
    for i in range(len(nums)):
        if i == 0:
            max = nums[i]
        if nums[i] > max:
            max = nums[i]
    return max

def reverse_in_place(nums):
    for i in range(len(nums)//2):
        tmp = nums[i]
        print(tmp)
        nums[i] = nums[len(nums)-1-i]
        print(nums[i])
        nums[len(nums)-i-1] = tmp
        print(nums[len(nums)-1-i])
    return nums

def remove_duplicates(nums):
    seen = []
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.append(nums[i])
    return seen

def move_zeros(nums):
    zero_count = 0
    for i in range(len(nums)):
        while nums[i] == 0:
            # stop condition
            if i > len(nums)-zero_count:
                break 

            # increment
            zero_count += 1

            #slide
            for j in range(i+1, len(nums)):
                nums[j-1] = nums[j]

            # set last
            nums[len(nums)-1] = 0   

    return nums

def move_zeros_2(nums):
    # initialize pointers
    p1 = 0
    p2 = 0

    while (p1 != len(nums) and (p2 != len(nums))):
        # p1 finds first zero
        for i in range(p1, len(nums)+1):
            if i == len(nums):
                p1 = i
                break
            if nums[i] == 0:
                p1 = i
                print("found zero")
                break

        # p2 finds first nonzero
        for j in range(p2, len(nums)+1):
            if j == len(nums):
                p2 = j
                break
            if nums[j] != 0:
                p2 = j
                print("found nonzero")
                break

        # swap as long as the zero is before the nonzero
        if (p1 < p2):
            print(f"swapping {p1} and {p2}")
            tmp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = tmp

            #advance pointers
            p1 =+ 1
            p2 += 1

        time.sleep(2)

    print(f"ended with p1 as {p1} and p2 as {p2}")
    return nums

# ============== TEST ================

nums1 = [6, -12, 12, 17, 23, 4]
nums2 = [1,1, 2, 3, 3, 4, 5]
nums3 = [0, 1, 0, 3, 12]
nums4 = [0, 0, 0, 1]
# print(find_max(nums1))

# print(reverse_in_place(nums1))
# print(reverse_in_place(nums2))

# print(remove_duplicates(nums2))

print(move_zeros_2(nums3))
# print(move_zeros_2(nums4))
