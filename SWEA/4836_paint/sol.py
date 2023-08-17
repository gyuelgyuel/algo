import sys
sys.stdin=open('input.txt')
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ## create 10*10 zero matrix
    matrix = []
    for i in range(10):
        matrix.append([0]*10)

    ## get box info & push to color matched box
    for n in range(N):
        box = list(map(int,input().split()))
        
        # paint matrix
        for r in range(box[0],box[2]+1):
            for c in range(box[1],box[3]+1):

                # paint color
                if matrix[r][c] == 0:
                    matrix[r][c] = box[4]
                
                # paint puple
                elif matrix[r][c] != box[4]:
                    matrix[r][c] = 3
    
    puple_cnt = 0
    for m in matrix:
        puple_cnt += m.count(3)
    
    print(f'#{tc} {puple_cnt}')