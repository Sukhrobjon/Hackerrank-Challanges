class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
            p = Node(data)
            if head is None:
                head = p
            elif head.next is None:
                head.next = p
            else:
                start = head
                while(start.next is not None):
                    start = start.next
                start.next = p
            return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        """
            Remove duplicate elements and return the linked list head
        """
        # check if linked list is empty
        if(head is None):
            return None
        # set to hold unique values
        unique_values = set()
        # start at the head
        current = head
        # keep track of previous node we can set it to either None or head
        prev = None
        # traverse through the linked list until current node is none
        while(current):
            # if the current node data is in unique values set
            if(current.data in unique_values):
                # we want to skip that duplicated value and set
                # the next poitnter of previous node to current.next
                prev.next = current.next
            # if we see this value first time we add it to set
            else:
                unique_values.add(current.data)
                # set the prev to current.
                prev = current
            # now basically shift the current node to the next one
            current = prev.next
        return head
    # def removeDups(self, head):
    #     current = second = head
    #     while current is not None:
    #         while second.next is not None:   # check second.next here rather than second
    #             if second.next.data == current.data:   # check second.next.data, not second.data
    #                 second.next = second.next.next   # cut second.next out of the list
    #             else:
    #                 second = second.next   # put this line in an else, to avoid skipping items
    #         current = second = current.next


def remove_duplicate(arr):
    cleaned = []
    for i in arr:
        if i not in cleaned:
            cleaned.append(i)
    return cleaned
arr = [1, 3, 3, 4, 1, 99, 99]

print(remove_duplicate(arr))
