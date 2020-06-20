import sys


class Node (object):
    def __init__(self,data, leftnode=None,rightnode=None):
        self.left=leftnode
        self.right = rightnode
        self.data=data
    def __str__(self):
        return str(self.data)

def preorder(node):
    print(node.data, end='')
    if node.left != '.': preorder(mTree[node.left])
    if node.right != '.': preorder(mTree[node.right])


def inorder(node):
    if node.left != '.': inorder(mTree[node.left])
    print(node.data, end='')
    if node.right != '.': inorder(mTree[node.right])

def postorder(node):
    if node.left != '.': postorder(mTree[node.left])
    if node.right != '.': postorder(mTree[node.right])
    print(node.data, end='')

    # def makenode(self,node, leftnode=None,rightnode=None):
    #     if self.root==None:
    #         self.root=node
    #     node.left=leftnode
    #     node.right=rightnode


num=int(sys.stdin.readline().strip())
mTree={}

for i in range(num):
    node , left, right= list(sys.stdin.readline().split())
    mTree[node]=Node(node,left,right)


preorder(mTree['A'])
# mTree.preorder()
print()
inorder(mTree['A'])
print()
postorder(mTree['A'])