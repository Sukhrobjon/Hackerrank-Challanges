# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def deleteNode(head, position):
    """
    Delete a node at a specific location, position is guaranteed to
    be in a right range.
    """
    curr = head
    # stop right before the desired postion
    for _ in range(position-1):
        curr = curr.next
    # skip over the node at the given position
    curr.next = curr.next.next

    return head
