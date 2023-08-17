import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def search_node(n,f,edges,path):
    if len(edges[n-1]) == 0:
        path.pop()
        return False
    else:
        for e in edges[n-1]:
            if e not in path:
                path.append(e)
                if e == f:
                    return True
                else:
                    if search_node(e,f,edges,path):
                        return True
    return False

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int,input().split()))
    nodes = range(1,V+1)
    edges = []
    for _ in range(V):
        edges.append([])

    for _ in range(E):
        s_e, e_e = list(map(int,input().split()))
        edges[s_e-1].append(e_e)
        
    start_node, end_node = list(map(int,input().split()))
    path = []

    if search_node(start_node,end_node,edges,path):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
