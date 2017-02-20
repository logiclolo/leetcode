class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # make sure length of nums1 < length of nums2
        if len(nums1) > len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp


        while len(nums1) > 1 and len(nums2) > 1: 
            print nums1
            print nums2
            print '------'

            if self.getMedian(nums1) > self.getMedian(nums2): 

                remove = len(nums1)/2
                
                nums1 = nums1[:len(nums1)-remove]
                nums2 = nums2[remove:]
            else:

                remove = len(nums1)/2

                nums1 = nums1[remove:]
                nums2 = nums2[:len(nums2)-remove]

        print nums1
        print nums2

        if len(nums1) == 0:
            return self.getMedian(nums2)
        elif len(nums1) == 1:
            # return self.getMedian(sorted(nums1+nums2))
            element = nums1[0]
            for i in range(len(nums2)): 
                if element > nums2[i]:
                    continue
                else:
                    nums2[i:i] = [element]
                    return self.getMedian(nums2)

            nums2[i+1:i+1] = [element]
            return self.getMedian(nums2)



    def getMedian(self, nums): 

        if len(nums) == 0:
            return float(0) 
        
        if len(nums) % 2 is 1:
            return float(nums[len(nums)/2])
        else:
            return (float(nums[len(nums)/2 - 1]) + float(nums[len(nums)/2])) / 2


if __name__ == '__main__':
    
    a = [1,2,4,5,7]
    b = [1,55,66,99]
    a = [3,5]
    b = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    a = [1,4]
    b = [2,3]
    print Solution().findMedianSortedArrays(a,b)






