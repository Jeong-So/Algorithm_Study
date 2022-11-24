## findPivotIndex
## Sliding 개념 이용하여 문제 풀이 --> O(n)에 리니어한 TimeComplex 가짐

def findPivotIndex(nums):
    add_num = sum(nums)

    left_num = 0
    right_num = add_num
    pivot_num = 0

    for idx in range(len(nums)):
        num = nums[idx]
        right_num -= num
        left_num += pivot_num
        pivot_num = num

        if right_num == left_num:
            return idx
    return -1

print(findPivotIndex([1, 8, 2, 9, 2, 3, 6]))
print(findPivotIndex([2, 5, 7]))

