#exceeded time limit
"""
def rotate(self, head, k):
        if head is None:
            return head
        temp=head
        lst=[]
        for i in range(k):
            lst.append(temp.data)
            temp=temp.next
            
        head=temp
        temp=head
        
        while temp:
            if temp.next:
                temp=temp.next
        
        for i in range(len(lst)):
            newnode= Node(lst[i])
            temp.next= newnode
            newnode.next=None
            temp=temp.next
        
        return head
 """
