class Node:
  def __init__(self):
    self.countWord = 0;
    self.child = dict();

def addWord(root, word):
  temp = root
  for char in word:
    if char not in temp.child:
      temp.child[char] = Node()
    temp = temp.child[char]
  temp.countWord += 1

def findWord(root, word):
  temp = root
  for char in word:
    if char not in temp.child:
      return False
    temp = temp.child[char]
  return temp.countWord > 0;

def isWord(node):
  return node.countWord != 0

def isPrefix(node):
  return len(node.child) > 0

def isEmpty(node):
  return len(node.child) == 0

def removeWord(root, word, level, length):
  if root == None:
    return False
  
