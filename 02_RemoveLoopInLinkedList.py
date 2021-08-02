#This approach uses Hashing

def removeLoop(self, head):
        prev=None
        curr=head
        s= set()
         
        while curr:
            if curr in s: 
                prev.next=None
                return
            
            s.add(curr)
            prev= curr
            curr=curr.next
