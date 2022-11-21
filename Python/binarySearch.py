# BinarySearch - 배열이 정렬 되어 있을 때 우리가 원하는 원소 찾기
# TimeComplex : O(logn)

def binarySearch(nums, target):
    left = 0
    right = len(nums)

    while(left <= right):
        pivot = int((left + right)/2)
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            left = pivot + 1
        else:
            right = pivot - 1
    return -1

nums = [1,7,9,15,19,20]
target = 16

print(binarySearch(nums,target))