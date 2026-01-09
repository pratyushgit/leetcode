from typing import List
from collections import OrderedDict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        scanned_numbers = OrderedDict()
        for i in range(len(nums)):
            expected_num1 = target - nums[i]
            if expected_num1 in scanned_numbers.keys():
                index_for_matching_num1 = scanned_numbers[expected_num1]
                return [index_for_matching_num1,i]
            else:
                scanned_numbers[nums[i]] = i
        return []

nums = [3,2,9,1,4,5,8]
target = 6
obj = Solution()
res = obj.twoSum(nums,target)
print(f"res: {res}")


