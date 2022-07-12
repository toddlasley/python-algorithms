# 2.1: Write code to remove duplicates from an unsorted linked list.

# Solution: p. 208

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_dups(head: 'ListNode') -> 'ListNode':
    vals = set()

    point = prev = head

    while point != None:
        if point.val in vals:
            prev.next = point.next
        else:
            vals.add(point.val)
            prev = point
        
        point = point.next
    
    return head
