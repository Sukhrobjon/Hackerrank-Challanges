# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    curr = head
    for i in range(position):
        curr = curr.next
    
    new_node = SinglyLinkedListNode(data)
    new_node.next = curr.next
    curr.next = new_node

    return head

