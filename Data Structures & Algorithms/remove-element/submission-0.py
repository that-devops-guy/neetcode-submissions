class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for i,v in enumerate(nums):
            if v == val:
                nums[i] = -1
            
        nums.sort(reverse=True)
        for num in nums:
            if num != -1:
                counter += 1
        return counter

