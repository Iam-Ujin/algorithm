# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_right, bisect_left

n, x = map(int, input().split())
array = list(map(int, input().split()))

left = bisect_left(array, x)
right = bisect_right(array, x)

result = right - left
print(result)