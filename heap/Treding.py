n = int(input())
import queue
class Topic:
    def __init__(self, id, newScore, score):
        self.id = id
        self.newScore = newScore
        self.increment = self.newScore - score
    def __lt__(self, other):
        return self.increment > other.increment or (self.increment == other.increment and self.id > other.id)
pq = queue.PriorityQueue()
for i in range(n):
    id, score, post, likes, comments, shares = map(int, input().split())
    newScore = post * 50 + likes * 5 + comments * 10 + shares * 20 
    pq.put(Topic(id, newScore, score))

for i in range(5):
    r = pq.get()
    print(r.id, r.newScore)
