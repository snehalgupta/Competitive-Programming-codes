class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
 

def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
def findpath(root,k):
    global path
    if root is None:
        return False
    path.append(root.val)
    if root.val == k:
        return True
    if((root.left is not None and findpath(root.left,k))or (root.right is not None and findpath(root.right,k))):
        return True
    path.pop()
    return False
def lca(root, n1, n2):
    if root is None:
        return None
    if(root.val > n1 and root.val > n2):
        return lca(root.left, n1, n2)
    if(root.val < n1 and root.val < n2):
        return lca(root.right, n1, n2)
    return root
path=[]
n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
r=Node(x[0])
for i in range(1,n):
    insert(r,Node(x[i]))
c=lca(r,a,b)
findpath(c,a)
findpath(c,b)
sum1=sum(path)-c.val
print(sum1)
    
    
