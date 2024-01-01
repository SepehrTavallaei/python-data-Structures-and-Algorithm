import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.empty()) # True
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.qsize()) # 3
print(customQueue.full()) # True
print(customQueue.get()) # removes 3
print(customQueue.full()) # False
print(customQueue.qsize()) # 2