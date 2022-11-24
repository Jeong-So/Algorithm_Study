## findPivotIndex
## LeetCode 209번 문제
## Sliding Window 개념 : 일정한 범위를 가지고 있는 것을 유지하면서 이동(sliding)
# 문제 풀이 중

def minSubArrayLen1(target, nums):
    add_num = nums[0]
    arr_len = []
    arr_size = 1
    left_pivot = 0

    for idx in range(len(nums)):
        add_num += nums[idx]
        arr_size += 1

        print(arr_size)

        if add_num == target:
            arr_len.append(arr_size)
            arr_size = 0
        elif add_num > target:
            add_num -= nums[left_pivot]
            print('add_num : ', add_num)
            left_pivot += 1
            arr_size -= 1
            if add_num == target:
                arr_len.append(arr_size)
                arr_size = 0
            print('arr_size :', arr_size)        
    
        print(arr_size)

    if len(arr_len) == 0:
        return 0
    else:
        return (min(arr_len))



def minSubArrayLen2(target, nums):
    
    add_num = 0
    arr_len = 0

    for idx in range(len(nums)):
        print('idx :', idx)
        for x in range(len(nums)):
            for y in range(idx):
                add_num += nums[y]
                print('y', y)
                print('add_num : ', add_num)
            if add_num == target:
                arr_len = idx +1
                print('arr_len : ', arr_len)
                break
    return arr_len


# print(minSubArrayLen1(7, [2,3,1,2,4,3]))

print(minSubArrayLen2(7, [2,3,1,2,4,3]))
