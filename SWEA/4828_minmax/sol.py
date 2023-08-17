import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1,T+1):
    N = input()
    num_list = list(map(int,input().split()))
    num_max = max(num_list)
    num_min = min(num_list)
    print(f'#{i} {num_max-num_min}')
