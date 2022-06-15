def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero = one = 0
    two = len(nums) - 1

    while one <= two:
        if nums[one] < 1:
            temp = nums[one]
            nums[one] = nums[zero]
            nums[zero] = temp
            zero += 1
            one += 1
        elif nums[one] > 1:
            temp = nums[one]
            nums[one] = nums[two]
            nums[two] = temp
            two -= 1
        else:
            one += 1