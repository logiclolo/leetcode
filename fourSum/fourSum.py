class Solution(object):
    def fourSum_ori(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        nums = sorted(nums)

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            three_sum = target - nums[i]
            ret = self.threeSumClosest(nums[i+1:], three_sum) 
            if len(ret) is not 0:
                ret = map(lambda x: [nums[i]] + x, ret)
                res = res + ret

        return res

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        results = []
        nums = sorted(nums)

        print nums

        self.findNsum(nums, target, 4, [], results)

        return results


    def findNsum(self, nums, target, n, result, results):

        if n is 2:
            front = 0
            rear = len(nums) - 1 

            while front < rear:
                s = nums[front] + nums[rear]

                if s == target:
                    results.append(result + [nums[front], nums[rear]])
                    while front < rear and nums[rear-1] == nums[rear]:
                        rear -= 1 
                    while front < rear and nums[front+1] == nums[front]:
                        front += 1

                    rear -= 1
                    front += 1

                elif s > target:
                    rear -= 1
                else:
                    front += 1
        else:
            for i in range(len(nums) - n + 1):
                if i > 0 and nums[i] == nums[i-1]: 
                    continue 

                self.findNsum(nums[i+1:], target - nums[i], n-1, result+[nums[i]], results)


    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
	nums = sorted(nums)
        length = len(nums)
        result = nums[0] + nums[1] + nums[2]
        tmp = []

        if length < 3:
            return None

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            base = nums[i]

            front = i + 1
            rear = length - 1

            while front < rear:
                total = base + nums[front] + nums[rear]
                diff = total - target

                if total == target:
                    tmp.append([base, nums[front], nums[rear]])

                if diff > 0:
                    while rear > front and nums[rear-1] == nums[rear]: 
                        rear -= 1
                    rear -= 1
                else:
                    while rear > front and nums[front+1] == nums[front]:
                        front += 1
                    front += 1

        return tmp 

if __name__ == '__main__':

    # string = [-1,1,1,2,-1,-4] 
    # string = [1,0,-1,0,-2,2]
    string = [-1,0,-5,-2,-2,-4,0,1,-2]
    # string = [-3,-2,-1,0,0,1,2,3]
    # string = [1,1,-1] 
    # string = [0,2,1,-3] 

    # print Solution().fourSum_ori(string, 0)
    print '---------start--------------'
    print Solution().fourSum(string, -9)
