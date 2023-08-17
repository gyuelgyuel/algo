import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]
len_A = len(A)

for tc in range(1, T+1):
    # sub set length & sub set sum
    N, K = list(map(int,input().split()))

    cnt = 0
    for i in range(1<<len_A):
        if i.bit_count()==N:
            subset_sum = 0
            for j in range(len_A):
                if i & (1<<j):
                    subset_sum+=A[j]
            if subset_sum==K:
                cnt+=1
    print(f'#{tc} {cnt}')

