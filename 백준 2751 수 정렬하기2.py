'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

1
2
3
4
5

Python3을 사용하면 시간초과
PyPy3을 사용
'''

# 병합정렬 구현
def mergesort(array):
  if len(array) <= 1:
      return array
  mid = len(array) // 2
  left = mergesort(array[:mid])
  right = mergesort(array[mid:])

  i, j, k = 0, 0, 0

  while i < len(left) and j < len(right):
      if left[i] < right[j]:
          array[k] = left[i]
          i += 1
      else:
          array[k] = right[j]
          j += 1
      k+=1
  
  if i == len(left):
      while j < len(right):
          array[k] = right[j]
          j += 1
          k += 1
  elif j == len(right):
      while i < len(left):
          array[k] = left[i]
          i += 1
          k += 1

  return array


n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num = mergesort(num)

for i in num:
    print(i)