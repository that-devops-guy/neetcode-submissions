class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        last_element = -1

        # pick first element and find max element in right

        for i in range(len(arr)):
            cur_element = arr.pop(0)
            max_right = max(arr, default=-1)
            cur_element = max_right
            result.append(cur_element)
        return result

