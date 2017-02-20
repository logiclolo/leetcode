#!/usr/bin/env python

class Solution(object): 
    def twoSum(self, nums, target): 
        if (len(nums) <= 1):
            return False
        hash_dict = {}

        for i in range(len(nums)):
            tmp = target - nums[i] 
            if tmp in hash_dict:
                return (hash_dict[tmp], i) 
            else:
                hash_dict[nums[i]] = i

        return False


if __name__ == '__main__':

    nums = [3,3]
    target = 6 

    obj = Solution()
    print obj.twoSum(nums, target)
