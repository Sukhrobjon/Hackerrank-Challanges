class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
            p = Node(data)
            if head == None:
                head = p
            elif head.next == None:
                head.next = p
            else:
                start = head
                while(start.next != None):
                    start = start.next
                start.next = p
            return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        
        pass

def remove_duplicate(arr):
    cleaned = []
    for i in arr:
        if i not in cleaned:
            cleaned.append(i)
    return cleaned
arr = [1, 3, 3, 4, 1, 99]

print(remove_duplicate(arr))