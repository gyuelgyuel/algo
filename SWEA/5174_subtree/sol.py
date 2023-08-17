import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

class node:
    def __init__(self,node_num):
        self.node_num = node_num
        self.parent = None
        self.left = None
        self.right = None
    def SetParent(self,parent_node):
        self.parent = parent_node
    def SetChild(self,child_node):
        if self.left == None:
            self.left = child_node
        elif self.right == None:
            self.right = child_node
        else:
            print('already have 2 child')
    def IsRoot(self):
        if self.parent == None:
            return True
        else:
            return False
    
T = int(input())

for tc in range(1, T+1):
    E, N = map(int,input().split())
    line = list(map(int,input().split()))
    # 노드 생성
    node_list = []
    for i in range(1,E+2):
        node_list.append(node(i))
    # 노드 연결 (트리 생성)
    for i in range(E):
        parent_num = line[2*i]
        child_num = line[2*i+1]
        node_list[parent_num-1].SetChild(node_list[child_num-1])
        node_list[child_num-1].SetParent(node_list[parent_num-1])

    # 서브 트리 루트 노드
    sub_root = node_list[N-1]
    sub_node_queue = []
    cnt = 1
    now = sub_root
    sub_node_queue.append(now)
    while len(sub_node_queue):
        now = sub_node_queue.pop(0)
        if now.left != None:
            sub_node_queue.append(now.left)
            cnt += 1
        if now.right != None:
            sub_node_queue.append(now.right)
            cnt += 1
    print(f'#{tc} {cnt}')