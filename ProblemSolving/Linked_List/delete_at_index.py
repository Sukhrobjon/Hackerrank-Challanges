# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def deleteNode(head, position):
    curr = head
    # stop right before the desired postion
    for _ in range(position-1):
        curr = curr.next
    # skip over the node at the given position
    curr.next = curr.next.next

    return head
