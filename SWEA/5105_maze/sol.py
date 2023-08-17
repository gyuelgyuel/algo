import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [[0]*N for _ in range(N)]
    for i in range(N):
        line = input()
        for j in range(N):
            maze[i][j] = int(line[j])
            if maze[i][j] == 2:
                start = [i,j]
            if maze[i][j] == 3:
                goal = [i,j]

    distance = [[0]*N for _ in range(N)]
    now = start
    queue = []
    queue.append(now)
    finish = False
    while not finish:
        if len(queue) == 0:
            break
        now = queue.pop(0)
        x, y = now

        for delta in [[-1,0],[1,0],[0,-1],[0,1]]:
            n_x, n_y = x + delta[0], y + delta[1]
            if 0 <= n_x and n_x < N and 0 <= n_y and n_y < N:
                if maze[n_x][n_y] != 1 and distance[n_x][n_y] == 0:
                    queue.append([n_x,n_y])
                    distance[n_x][n_y] = distance[x][y] + 1
                    if n_x == goal[0] and n_y == goal[1]:
                        finish = True
                        break
                elif distance[n_x][n_y] != 0:
                    if distance[n_x][n_y] > distance[x][y] + 1:
                        distance[n_x][n_y] = distance[x][y] + 1

    #[print(maze[i], distance[i]) for i in range(N)]
    if distance[goal[0]][goal[1]] == 0:
        result = 0
    else:
        result = distance[goal[0]][goal[1]] - 1
    print(f'#{tc} {result}')
                