import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int,input().split()))
    word_mat = []
    strings = []
    circular_string = ''

    ## word_mat 작성
    for n in range(N):
        word_mat.append(input())

    ## 가로 string 추출
    for i in range(N):
        for m in range(N-M+1):
            strings.append(word_mat[i][m:M+m])
    
    ## 전치행렬
    r_word_mat =[]
    for i in range(N):
        r_word_mat.append(['']*N)

    for i in range(N):
        for j in range(N):
            r_word_mat[i][j] = word_mat[j][i]

    r_word_mat = list(map(''.join,r_word_mat))
        
    ## 세로 string 추출
    for j in range(N):
        for start_i in range(N-M+1):
            strings.append(word_mat[j][m:M+m])

    ## 회문인지 검사
    for s in strings:
        r_s = s[::-1]
        if s == r_s:
            circular_string = s
    
    print(f'#{tc} {circular_string}')