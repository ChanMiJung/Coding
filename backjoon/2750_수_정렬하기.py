# 제출한 코드
N = int(input())
num_list = [int(input()) for _ in range(N)]

start = time.time()

## 버블 정렬
for i in range(N-1, 0, -1):
    for j in range(i):
        if num_list[j] > num_list[i]:
            num_list[j], num_list[i] = num_list[i], num_list[j]

for num in num_list: print(num)


# 정렬 시간 테스트
import random
import time
N = 1000
num_list = random.sample(range(-1000, 1001), N)

## 내장모듈 sort()
start = time.time()

num_list.sort()

end = time.time() - start

print()
print(f'sort()')
print(f'걸린 시간 : {end}초')
print()

## 내장 모듈 sorted()
start = time.time()

result_list = sorted(num_list)

end = time.time() - start

print()
print(f'sorted()')
print(f'걸린 시간 : {end}초')
print()

## 버블 정렬
start = time.time()
for i in range(N-1, 0, -1):
    for j in range(i):
        if num_list[j] > num_list[i]:
            num_list[j], num_list[i] = num_list[i], num_list[j]

end = time.time() - start
print()
print(f'버블 정렬')
print(f'걸린 시간 : {round(end, 2)}초')
print()
print(num_list)

## 선택 정렬
start = time.time()
for i in range(N):
    min_idx = i
    for j in range(i+1, N):
        if num_list[j] < num_list[min_idx]:
            min_idx = j
    
    num_list[min_idx], num_list[i] = num_list[i], num_list[min_idx]

end = time.time() - start
print()
print(f'선택 정렬')
print(f'걸린 시간 : {round(end, 2)}초')
print()
# print(num_list)

## 삽입 정렬
start = time.time()

for i in range(1, N):
    now_idx = i
    while now_idx > 0:
        if num_list[now_idx] < num_list[now_idx-1]:
            num_list[now_idx], num_list[now_idx-1] = num_list[now_idx-1], num_list[now_idx]
            now_idx -= 1
        else:
            break


end = time.time() - start
print()
print(f'삽입 정렬')
print(f'걸린 시간 : {round(end, 2)}초')
print()
# print(num_list)

## 셸 정렬
start = time.time()
def shell_sort(sort_list):
    length = len(sort_list)
    k = length // 2

    while k > 0:
        for i in range(k, length):
            idx = i - k
            value = sort_list[i]
            while idx > -1 and value < sort_list[idx]:
                sort_list[idx+k] = sort_list[idx]
                idx -= k
            sort_list[idx+k] = value
            
        k //= 2
    return sort_list

result_list = shell_sort(num_list)

end = time.time() - start
print()
print(f'셸 정렬')
print(f'걸린 시간 : {round(end, 2)}초')
print()
# print(num_list)

## 힙 정렬
## 오름차순 : 최소 힙
## heapq 모듈 사용하기 - 최소 힙 알고리즘 제공함
import heapq
start = time.time()

result_list = []
heapq.heapify(num_list)
while num_list:
    result_list.append(heapq.heappop(num_list))

end = time.time() - start
print()
print(f'힙 정렬')
print(f'걸린 시간 : {end}초')
print()
# print(result_list)

## 퀵 정렬
def quick_sort(sort_list):
    if len(sort_list) <= 1:
        return sort_list
    small, same, big = [], [], []
    pivot = sort_list[0]
    for value in sort_list:
        if value < pivot:
            small.append(value)
        elif value > pivot:
            big.append(value)
        else:
            same.append(value)
    return quick_sort(small) + same + quick_sort(big)

start = time.time()

result_list = quick_sort(num_list)

end = time.time() - start
print()
print(f'퀵 정렬')
print(f'걸린 시간 : {end}초')
print()
# print(result_list)


## 병합(합병) 정렬
### 재귀로 작성
def merge_sort(sort_list):
    if len(sort_list) == 1:
        return sort_list

    length = len(sort_list)
    h = length//2 + 1
    result_list = []
    result_list.extend(merge_sort(sort_list[:h]))
    result_list.extend(merge_sort(sort_list[h:]))

    result_list.sort()

    return result_list

start = time.time()

result_list = merge_sort(num_list)

end = time.time() - start

print()
print(f'병합 정렬')
print(f'걸린 시간 : {end}초')
print()
print(result_list)


    