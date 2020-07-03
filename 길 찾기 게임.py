
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class SearchTree(object):
    def __init__(self):
        self.root=None

    def insert(self,data):
        self.root=self.insert_value(self.root,data)
        return self.root is not None

    def insert_value(self,node,data):
        if node is None:
            node=Node(data)
        else:
            if data[1][1]<=node.data[1][1] :
                if data[1][0]<=node.data[1][0]:
                    node.left=self.insert_value(node.left,data)
                else:
                    node.right=self.insert_value(node.right,data)
        return node

    def preOrder(self,result):
        def preOrderTraversal(root):
            if root is None:
                pass
            else:
                # print(root.data[0],end=' ')
                if root.data[0] is not None:
                    result.append(root.data[0])
                preOrderTraversal(root.left)
                preOrderTraversal(root.right)
        preOrderTraversal(self.root)


    def postorder(self,result):
        def postOrderTraversal(root):
            if root is None:
                pass
            else:
                postOrderTraversal(root.left)
                postOrderTraversal(root.right)
                if root.data[0] is not None:
                    result.append(root.data[0])
        postOrderTraversal(self.root)



def solution(nodeinfo):
    answer = []
    tree=SearchTree()

    for i in range(len(nodeinfo)):
        answer.append([i+1,nodeinfo[i]])
    answer.sort(key=lambda x:(-x[1][1],x[1][0]))
    # print(answer)
    for i in range(len(nodeinfo)):
        tree.insert(answer[i])

    arr=[[],[]]
    arr.append(tree.postorder(arr[0]))

    arr.append(tree.preOrder(arr[1]))

    return [arr[1],arr[0]]
    # print([arr[1],arr[0]])


solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])