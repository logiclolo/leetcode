class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import sys

	nums = sorted(nums)
        length = len(nums)
        result = sys.maxint
        # result = nums[0] + nums[1] + nums[2]

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
                    return total

                if abs(diff) < abs(target-result):
                    result = total  

                if diff > 0:
                    rear -= 1
                else:
                    front += 1

        return result 

if __name__ == '__main__':

    string = [-1,1,1,2,-1,-4] 
    string = [1,1,-1] 
    # string = [1,2,3,0,-1,-2,-3,-4]
    # string = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    # string = [0,4,-1,0,3,1,1,0,-3,2,-5,-4,-3,0,0,-3]
    string = [-7,2,1,10,9,-10,-5,4,13,-9,-4,6,11,-12,-6,-9,-6,-9,-11,-4,10,10,-3,-1,-4,-7,-12,-15,11,5,14,11,-7,-8,6,9,-2,9,-10,-12,-15,2,10,4,5,11,10,6,-13,6,-13,12,-7,-9,-12,4,-9,13,-4,10,4,-12,6,4,-5,-10,-2,0,14,4,4,6,13,-9,-5,-5,-13,12,-14,11,3,10,8,11,-13,4,-8,-7,2,4,10,13,7,2,2,9,-1,8,-5,-10,-3,6,3,-5,12,6,-3,6,3,-2,2,14,-7,-13,10,-13,-2,-12,-4,8,-1,13,6,-9,0,-14,-15,6,9]
    # string = [1,1,1,2]
    string = [0,2,1,-3] 

    print Solution().threeSumClosest(string, 1)
