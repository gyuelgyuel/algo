import sys
sys.stdin=open('input.txt')
T = int(input())

for tc in range(1,T+1):
    N, M = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    max_val = 0
    min_val = 10000*N
    for i in range(N-M+1):
        interval_sum = 0
        for j in range(M):
            interval_sum += numbers[i+j]
        if interval_sum > max_val:
            max_val = interval_sum
        if interval_sum < min_val:
            min_val = interval_sum
    print(f'#{tc} {max_val-min_val}')
