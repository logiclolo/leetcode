class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        forward = 0 
        backward = len(height) - 1
        maxarea = 0

        while True:

            if forward >= backward:
                break

            front = height[forward]
            rear = height[backward]

            if rear > front:
                area = front * (backward - forward)
                forward = forward + 1
            else:
                area = rear * (backward - forward)
                backward = backward - 1

            if area > maxarea:
                maxarea = area
                
        return maxarea 

"""
brute force not accepted
"""
class Solution1(object):
    area = 0
    height = []

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """ 

        self.height = height

        heights = [] 

        for i in range(len(height)):
            heights.append(i)

        print heights
        self.calculate(heights)

        return self.area
            

    def calculate(self, sub): 
        base_index = -1 
        base_edge = 0
        area = 0
        short_edge = 0
        ssub = [] 
        new_edge = 0
        count = 0

        for i in sub:

            if base_index is -1:
                base_index = i 
                base_edge = self.height[i] 
                print 'base index is %d' % base_index
                print 'base edge is %d' % base_edge 
                continue

            new_edge = self.height[i] 
            if new_edge > base_edge: 
                short_edge = base_edge
                ssub.append(i) 
                print ssub
            else:
                short_edge = new_edge 

            area = (i - base_index) * short_edge 

            if area > self.area:
                print 'max area %d (%d, %d),(%d, %d)' % (area, base_index, i, base_edge, self.height[i])
                self.area = area

        print ssub
        print '-------'
        if len(ssub) is 0:
            return
        else:
            self.calculate(ssub)
            
            

if __name__ == '__main__':

    # a = [1,2,3,3,5,6]
    # a = [1,2,99,98,5,6]
    # a = [4,6,4,4,6,2,6,7,11,2] 
    # a = [1,1]
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131]

    obj = Solution()
    print obj.maxArea(a)
