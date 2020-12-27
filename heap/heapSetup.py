h = [20, 12, 6, 10, 17, 15, 2, 4]
# index of node parent = len(h) // 2 - 1
def minHeapify(i):
    smallest = i
    leftNode = i * 2 + 1
    rightNode = i *2 + 2
    if leftNode < len(h) and h[leftNode] < h[smallest]:
        smallest = leftNode
    if rightNode < len(h) and h[rightNode] < h[smallest]:
        smallest = rightNode
    if smallest != i:
        h[i], h[smallest] = h[smallest], h[i]
        minHeapify(smallest)

def buildHeap(n):
    for i in range(n // 2 - 1, -1, -1):
        minHeapify(i)

def addNodeToHeap(value):
    h.append(value)
    indexOfValue = len(h) - 1
    while indexOfValue != 0 and h[(indexOfValue - 1) // 2] > h[indexOfValue]:
        h[(indexOfValue - 1) // 2], h[indexOfValue] = h[indexOfValue], h[(indexOfValue - 1) // 2]
        indexOfValue = (indexOfValue - 1) // 2

def popHeap():
    length = len(h)
    if length == 0:
        return
    h[0] = h[length - 1]
    h.pop()
    minHeapify(0)


buildHeap(len(h))
print(h)