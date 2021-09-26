class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in hmap:
                return [i, hmap[diff]]
            else:
                hmap[nums[i]] = i
        return -1


a = Solution()
print(a.twoSum([2,7,11,15], 9))
