""" This program is to find sum of two linked list containing integer in reverse order """

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        def extract_sum(num)
            curr = ListNode(None)
            while curr.next:
                num += curr.val
            return num
        num1 , num2 = extract_sum(num1), extract_sum(num2)
        print(num1)
        print(num2)
        return [num1, num2]
   