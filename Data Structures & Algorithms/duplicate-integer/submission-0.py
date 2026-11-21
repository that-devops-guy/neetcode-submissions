class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        actual_vals = set(nums)
        # print(f"actual_vals {actual_vals}")
        if len(actual_vals) == len(nums):
            return False
        return True