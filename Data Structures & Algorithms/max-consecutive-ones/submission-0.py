class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        temp_max_consecutive = 0
        
        for num in nums:
            if num == 1:
                temp_max_consecutive += 1
                max_consecutive = max(max_consecutive, temp_max_consecutive)
            else:
                temp_max_consecutive = 0
                print(f"max: {max_consecutive}")
            
        return max_consecutive