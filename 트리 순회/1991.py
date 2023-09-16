N = int(input())
tree = {}
for _ in range(N):
    root, left, right = map(str, input().split())
    tree[root]=[left,right]

def preorder(root):
    if root !='.':
        print(root,end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inodrder(root):
    if root !='.':
        inodrder(tree[root][0])
        print(root,end='')
        inodrder(tree[root][1])

def postorder(root):
    if root !='.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root,end='')

preorder('A')
print()
inodrder('A')
print()
postorder('A')

