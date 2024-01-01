#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Sspace O(1) and O(n) time
        Extending the idea from attempt 1, we can also represent backward
        as a variable instead of an array
        """
        backward = 1
        forward = 1
        out = [1] * len(nums)
        for i in range(0, len(nums)):
            out[i] *= forward
            forward *= nums[i]
            out[len(nums) - i - 1] *= backward
            backward *= nums[len(nums) - i - 1]
        return out

    def attempt_1(self, nums: List[int]) -> List[int]:
        """
        Notice how output for value at idx i is
            product(nums[0:i]) * product(nums[i+1:])
        1. calculate backward prefix product
        2. Pretend forward is an array of forward prefix product (its actually a var)
            forward[0] = nums[0], forward[i+1] *= forward[i]
        2. ans[i] =
            a. if i == 0, backward[len-1-2]
            b. elif i == len - 1, forward[i-1]
            c. else, forward[len - 2]
        """
        backward = [nums[-1]]
        for i in range(1, len(nums)):
            backward.append(backward[i - 1] * nums[len(nums) - i - 1])

        forward = 1
        out = [backward[len(nums) - 2]]
        for i in range(1, len(nums) - 1):
            forward *= nums[i - 1]
            out.append(forward * backward[len(nums) - i - 2])
        out.append(forward * nums[-2])

        return out


# @lc code=end
