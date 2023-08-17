import sys
sys.stdin=open('input.txt')

for tc in range(1,11):
    T = input()

    ## 열의 합, 대각선의 합을 저장하는 배열 생성
    colcross_sum = [0]*102
    max_sum = 0
    for i in range(100):
        line = list(map(int,input().split()))

        ## 행의 합이 클경우 max 갱신
        line_sum = sum(line)
        if max_sum < line_sum:
            max_sum = line_sum

        ## 열, 대각선의 합 저장
        for j in range(len(line)):
            colcross_sum[j] += line[j]
            if i==j:
                colcross_sum[100] += line[j]
            elif i+j==99:
                colcross_sum[101] += line[j]
                
    ## 가장 큰 열, 대각선의 합이 클경우 max갱신
    if max_sum < max(colcross_sum):
        max_sum = max(colcross_sum)

    print(f'#{T} {max_sum}')