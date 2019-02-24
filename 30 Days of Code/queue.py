class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    

    def enqueue(self, data):
        """
            Add a new queue to the tail of queues 
        """
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self):
        """ 
            FIFO. Remove and returns the first element of the queue 
        """
        if self.head is None:
            return None
        else:
            removed = self.head.data
            self.head = self.head.next
            return removed
    def is_empty(self):
        return self.head is None

if __name__ == "__main__":
    a_queue = Queue()

    a_queue.enqueue("5")
    a_queue.enqueue("10")
    a_queue.enqueue("11")
    print(a_queue.is_empty())
    first = a_queue.dequeue()
    second = a_queue.dequeue()
    # third = a_queue.dequeue()
    print(a_queue.is_empty())
    # print(first)
