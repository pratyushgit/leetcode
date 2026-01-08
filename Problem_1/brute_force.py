from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

nums = [3,2,9,1,4,5,8]
target = 6
obj = Solution()
res = obj.twoSum(nums,target)
print(f"res: {res}")


