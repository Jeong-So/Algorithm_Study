# moveZeros - 배열에서 0값 오른쪽(왼쪽) 정렬
# 문제풀이 idea - 숫자를 찾아서 왼쪽으로 보냄

# 풀이 1
# 0과 숫자 swap
def moveZeros1(nums):
    zeroIdx = 0  # zeroIdx: 0을 가르키는 인덱스
    for idx in range(len(nums)):  # idx : 숫자를 가르키는 인덱스
        if nums[idx]!=0:
            # 0과 숫자 swap
            nums[zeroIdx], nums[idx] = nums[idx], nums[zeroIdx]
            zeroIdx += 1 # 파이썬은 증감 연산자(++/--)가 없다
    return nums

# 풀이 2
# 숫자 카피 후 나머지 0 overriding
# nums[idx]를 복사하여 nums[zeroIdx]에 써준 후 
# idx가 배열 밖으로 나간 순간 zeroIdx 인덱스부터 끝까지 0으로 덮어써줌
def moveZeros2(nums):
    zeroIdx = 0  # zeroIdx: 0을 가르키는 인덱스
    for idx in range(len(nums)):  # idx : 숫자를 가르키는 인덱스
        if nums[idx]!=0:
            nums[zeroIdx] = nums[idx]
            zeroIdx += 1 # 파이썬은 증감 연산자(++/--)가 없다
    for newIdx in range(zeroIdx, len(nums)):
        nums[newIdx] = 0
    return nums

print(moveZeros1([0,0,3,5,2,0,0,3,0,2,0,5,4,3,0]))

print(moveZeros2([0,0,3,5,2,0,0,3,0,2,0,5,4,3,0]))