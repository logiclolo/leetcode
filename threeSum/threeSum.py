class Solution(object):
    def threeSum(self, array):

        hash_table = {}
        result = []
    
        array = sorted(array)

        for i in range(len(array) - 2):
            base = array[i]
            if i > 0 and base == array[i-1]:
		continue
	
            left = i + 1
            right = len(array) - 1

            while left < right:
                total = array[i] + array[left] + array[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([array[i], array[left], array[right]])
                    while left < right and array[left] == array[left+1]:
                        left += 1
                    while left < right and array[right] == array[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

                
        return result

    def threeSum1(self, array):

        hash_table = {}
        result = []

        array = sorted(array)
        for i in array:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        for i in range(len(array) - 2):
            base = array[i]
            hash_table[base] -= 1

            for index in range(len(array) - i):
                j = array[index + i]
                if hash_table[j] is 0:
                    continue

                hash_table[j] -= 1
                need = -base - j
                if need in hash_table and hash_table[need] > 0:
                    tmp = sorted([array[i], j, need])

                    if tmp not in result:
                        result.append(tmp)
                hash_table[j] += 1
            hash_table[base] += 1

        return result

                

if __name__ == '__main__':

    string = [-1,0,1,2,-1,-4] 
    # string = [1,2,3,0,-1,-2,-3,-4]
    # string = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    # string = [0,4,-1,0,3,1,1,0,-3,2,-5,-4,-3,0,0,-3]
    string = [-7,2,1,10,9,-10,-5,4,13,-9,-4,6,11,-12,-6,-9,-6,-9,-11,-4,10,10,-3,-1,-4,-7,-12,-15,11,5,14,11,-7,-8,6,9,-2,9,-10,-12,-15,2,10,4,5,11,10,6,-13,6,-13,12,-7,-9,-12,4,-9,13,-4,10,4,-12,6,4,-5,-10,-2,0,14,4,4,6,13,-9,-5,-5,-13,12,-14,11,3,10,8,11,-13,4,-8,-7,2,4,10,13,7,2,2,9,-1,8,-5,-10,-3,6,3,-5,12,6,-3,6,3,-2,2,14,-7,-13,10,-13,-2,-12,-4,8,-1,13,6,-9,0,-14,-15,6,9]
    # string = [1,1,1,2]
    # string = [0,0,0]
    # string = [-2,0,1,1,2] 

    print Solution().threeSum(string)
