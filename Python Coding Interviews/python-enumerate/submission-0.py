from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i,n in enumerate(nums):
        if n == 7:
            return i
        continue
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:

    first_occurence_index = -1
    second_occurence_index = -1
    for i,n in enumerate(nums):
        if n == 7 and first_occurence_index == -1:
            first_occurence_index = i
            # print(f"first_occurence_index {first_occurence_index}")
        elif n == 7 and (first_occurence_index > -1 and second_occurence_index == -1):
            second_occurence_index = i
            # print(f"second_occurence_index {second_occurence_index}")
        else:
            continue
    difference = second_occurence_index - first_occurence_index
    return difference



# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
