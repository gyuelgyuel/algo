import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))

    for i in range(N):
        for j in range(i+1,N):
            if i % 2 == 0:
                if numbers[i] < numbers[j]:
                    temp = numbers[i]
                    numbers[i] = numbers[j]
                    numbers[j] = temp
            else:
                if numbers[i] > numbers[j]:
                    temp = numbers[i]
                    numbers[i] = numbers[j]
                    numbers[j] = temp

    prt_format = ' '.join(map(str,numbers[0:10]))
    print(f'#{tc} {prt_format}')