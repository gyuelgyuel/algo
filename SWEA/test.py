class Tree:
    depth = 0
    node_cnt = 0
    root = None

class node(Tree):
    def __init__(self,val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
    def add_tree(self):
        if Tree.node_cnt == 0:
            Tree.root = self
        Tree.node_cnt += 1

    def IsRoot(self):
        if self.parent == None:
            return True
        else:
            return False

tree1 = Tree()
tree2 = Tree()
node1 = node(3)
node2 = node(4)
node3 = node(5)
node1.add_tree()
print(tree1.node_cnt, tree1.root.val)
print(tree2.node_cnt, tree2.root.val)