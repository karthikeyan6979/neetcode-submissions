class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i
        for i in nums:
            diff = target - i
            if diff in indices and indices[diff] != nums.index(i) :
                return[nums.index(i), indices[diff]]