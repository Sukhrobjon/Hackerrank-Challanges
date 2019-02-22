class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next
    
    def insert(self, head, data):
        """ 
            Initially head->null 
            Insert new node to the tail of the linked list
        """
        if head == None:
            head = Node(data)
        else:
            head.next = self.insert(head.next, data)

        return head

def insert(self, head, data):
    #Complete this method

    pass



mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
