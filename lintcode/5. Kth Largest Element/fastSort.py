class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        return self.find(n, nums, 0, len(nums))

    def find(self, n, nums, start, stop):

        if start +1 >= stop:
            return nums[start]

        arr=[]

        sp = nums[start]

        arr.append(sp)
        index=0

        for i in range(start + 1, stop):
            if nums[i] <= sp:
                arr.append(nums[i])
            else:
                arr.insert(index, nums[i])
                index+=1

        if index == n-1:
            return sp
        elif index < n-1:
            return self.find(n-index-1, arr, index+1, len(arr))
        else:
            return self.find(n, arr, 0, index)

s = Solution()

assert s.kthLargestElement(3, [9,3,2,4,8]) == 4

assert s.kthLargestElement(1, [1,3,4,2]) == 4