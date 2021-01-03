class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None

def createNode(value):
    newNode = Node()
    newNode.value = value
    return newNode

def insertNode(root, value):
    if root == None:
        return createNode(value)
    if value < root.value:
        root.left = insertNode(root.left, value)
    elif value > root.value:
        root.right = insertNode(root.right, value)
    return root

def createTree(a, n):
    root = None
    for i in range(n):
        root = insertNode(root, a[i])
    return root

def searchNode(root, x):
    if root == None or root.value == x:
        return root
    if x > root.value:
        return searchNode(root.right, x)
    return searchNode(root.left, x)

def deleteNode(root, x):
    if root == None:
        return root
    if x > root.value:
        root.right = deleteNode(root.right, x)
    elif x < root.value:
        root.left = deleteNode(root.left, x)
    # x == node.value
    else:
        if root.right == None:
            temp = root.left
            del root
            return temp
        elif root.left == None: 
            temp = root.right
            del root
            return temp
        minNode = minValueNode(root.right)
        root.value = minNode.value    
        root.right = deleteNode(root.right, minNode.value)
    return root
    
def minValueNode(node):
    current = node
    while current.left != None:
        current = current.left
    return current

def traversalTree(root):
    if root != None:
        traversalTree(root.left)
        print(root.value)
        traversalTree(root.right, end=' ')

def size(root):
    if root == None:
        return 0
    return size(root.left) + 1 + size(root.right)

def deleteRoot(root):
    if root == None:
        return
    deleteRoot(root.left)
    deleteRoot(root.right)
    del root