from queue import Queue

q = Queue()

print(q.isEmpty())
q.enqueue(2)
q.enqueue(4)

print(list(q.items))
