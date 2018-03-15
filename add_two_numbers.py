class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add,finalsum = 0,ListNode(0)
        changed = False
        while(l1 != None or l2 != None or add != 0):
            a = l1.val if l1!=None else 0
            b = l2.val if l2!=None else 0
            l1 = l1.next if l1!=None else None
            l2 = l2.next if l2!=None else None
            
            onesum = (a + b + add)%10
            add = int((a + b + add)/10)
            
            if changed==False:
                sumnode = ListNode(onesum)
                finalsum = sumnode
                changed = True
            else:    
                sumnode.next = ListNode(onesum)
                sumnode = sumnode.next
        
        return finalsum