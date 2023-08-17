import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

class Tree:
    depth = 0
    root = None

class node:
    node_cnt = 0
    def __init__(self,val):
        node.node_cnt += 1
        self.node_num = node.node_cnt
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

    def add_tree(self,tree):
        depth = 2
        if tree.root == None:
            tree.root = self
            tree.depth = 1
        else:
            now = tree.root
            while now:
                if now.val > self.val:
                    if now.left == None:
                        if now.parent != None:
                            if now.parent.parent != None:
                                if now.parent.right == None:
                                    temp = now.parent.parent
                                    if temp.left.val == now.parent.val:
                                        temp.left = now
                                    elif temp.right.val == now.parent.val:
                                        temp.right = now
                                    now.parent.left = now.right
                                    now.right = now.parent
                                    now.parent.parent = now
                                    self.parent = now
                                    now.left = self
                                    now.parent = temp
                                    node.node_cnt += 1
                                    if tree.depth < depth:
                                        tree.depth = depth
                                    break
                                elif now.parent.left == None:
                                    temp = now.parent.parent
                                    if temp.left.val == now.parent.val:
                                        temp.left = self
                                    elif temp.right.val == now.parent.val:
                                        temp.right = self
                                    now.parent.right = self.left
                                    self.left = now.parent
                                    self.right = now
                                    now.parent.parent = self
                                    now.parent = self
                                    self.parent = temp
                                    node.node_cnt += 1
                                    if tree.depth < depth:
                                        tree.depth = depth
                                    break
                                else:
                                    now.left = self
                                    self.parent = now
                                    node.node_cnt += 1
                                    if tree.depth < depth:
                                        tree.depth = depth
                                    break
                            else:
                                if now.parent.right == None:
                                    now.parent.left = now.right
                                    now.right = now.parent
                                    now.parent.parent = now
                                    self.parent = now
                                    now.left = self
                                    now.parent = None
                                    tree.root = now
                                    node.node_cnt += 1
                                    if tree.depth < depth:
                                        tree.depth = depth
                                    break
                                elif now.parent.left == None:
                                    now.parent.right = self.left
                                    self.left = now.parent
                                    self.right = now
                                    now.parent.parent = self
                                    now.parent = self
                                    self.parent = None
                                    tree.root = self
                                    node.node_cnt += 1
                                    if tree.depth < depth:
                                        tree.depth = depth
                                    break
                                else:
                                    now.left = self
                                    self.parent = now
                                    node.node_cnt += 1
                                    if tree.depth < depth:
                                        tree.depth = depth
                                    break
                        else:
                            now.left = self
                            self.parent = now
                            node.node_cnt += 1
                            if tree.depth < depth:
                                tree.depth = depth
                            break
                    else:
                        now = now.left
                        depth += 1
                elif now.val < self.val:
                    if now.right == None:
                        if now.parent != None:
                            if now.parent.parent != None:
                                if now.parent.right == None:
                                    temp = now.parent.parent
                                    if temp.left.val == now.parent.val:
                                        temp.left = self
                                    elif temp.right.val == now.parent.val:
                                        temp.right = self
                                    now.parent.left = self.right
                                    self.left = now
                                    self.right = now.parent
                                    now.parent.parent = self
                                    now.parent = self
                                    self.parent = temp
                                    node.node_cnt += 1
                                    depth -= 1
                                    if tree.depth < depth:
                                        tree.depth = depth
                                    break
                                elif now.parent.left == None:
                                    temp = now.parent.parent
                                    if temp.left.val == now.parent.val:
                                        temp.left = now
                                    elif temp.right.val == now.parent.val:
                                        temp.right = now
                                    now.parent.right = now.left
                                    now.left = now.parent
                                    now.right = self
                                    now.parent.parent = now
                                    self.parent = now
                                    now.parent = temp
                                    node.node_cnt += 1
                                    depth -= 1
                                    if tree.depth < depth:
                                        tree.depth = depth
                                    break
                                else:
                                    now.right = self
                                    self.parent = now
                                    node.node_cnt += 1
                                    if tree.depth < depth:
                                        tree.depth = depth
                                    break
                            else:
                                if now.parent.right == None:
                                    now.parent.left = self.right
                                    self.left = now
                                    self.right = now.parent
                                    now.parent.parent = self
                                    now.parent = self
                                    self.parent = None
                                    tree.root = self
                                    node.node_cnt += 1
                                    depth -= 1
                                    if tree.depth < depth:
                                        tree.depth = depth
                                    break
                                elif now.parent.left == None:
                                    now.parent.right = now.left
                                    now.left = now.parent
                                    now.right = self
                                    now.parent.parent = now
                                    self.parent = now
                                    now.parent = None
                                    tree.root = now
                                    node.node_cnt += 1
                                    depth -= 1
                                    if tree.depth < depth:
                                        tree.depth = depth
                                    break
                                else:
                                    now.right = self
                                    self.parent = now
                                    node.node_cnt += 1
                                    if tree.depth < depth:
                                        tree.depth = depth
                                    break
                        else:
                            now.right = self
                            self.parent = now
                            node.node_cnt += 1
                            if tree.depth < depth:
                                tree.depth = depth
                            break
                    else:
                        now = now.right
                        depth += 1
                else:
                    print('samevalue')
                    break

    def IsRoot(self):
        if self.parent == None:
            return True
        else:
            return False
        
t1 = Tree()
n1 = node(3)
n2 = node(4)
n3 = node(5)
n4 = node(6)
n5 = node(1)
n6 = node(2)

for i in range(6):
    temp = node(i+1)
    temp.add_tree(t1)
if t1.root!=None:
    print(t1.depth,t1.root.val,t1.root.right.right.right.val)
# T = int(input())

# for tc in range(1, T+1):
    # N = int(input())
    # M = int(N/2)
    # depth = 0
    # while 2**depth < N+1:
    #     depth += 1
    # root = 2**(depth-2)-1 + N%(2**(depth-1))+1 + 1
    # print(N,depth,root)
    # depth = 0
    # while M//2 != 0:
    #     M = M//2
    #     depth += 1
    # width = int(N/2)%(2**(depth-1))

    # print(f'#{tc} {int((N+2)/2)} {N}')