#Zip a linked list
#1->2->3->4>5->6 = 1->6->2->5->3->4 

'''
ALGORITHM
1. Split the list in the middle (first middle if even)
2. Reverse second half
3. Merge nodes from both list 
'''

import sys
sys.path.append("./mylib/")
import LinkedListLibrary

class LLNode:
	def __init__(self,data):
		self.data = data
		self.next = None


#1. split input into 2 at the first middle
#2. return head to the second list
def splitInMiddle(node):
	slow = node
	fast = node
	#until valid next node 
	while fast.next:
		#jump 2hops?
		if fast.next.next:
			fast = fast.next.next 
			slow = slow.next      #reaches first middle for even
		else:
			break
	#split input into 2
	tmp = slow.next
	#end first list
	slow.next = None
	#return start of second list 		
	return tmp

def reverse(node):
	prev=None
	while node:
		tmp = node.next
		node.next = prev
		prev = node
		node = tmp
	return prev


def merge(a,b):
	head = a
	while b:
		at = a.next
		bt = b.next
		a.next = b
		b.next = at
		a = at
		b = bt
	return head

head1 = LLNode(1)
for i in range(2,6):
	newNode = LLNode(i)
	LinkedListLibrary.Insert2End(head1,newNode)



print("input >>>")
LinkedListLibrary.PrintLinkedList(head1)
#step 1: split into two
head2 = splitInMiddle(head1)
#step 2: reverse the second list
head2 = reverse(head2)
#step 3: merge both the list
head3 = merge(head1,head2)

print("zipped result >>>")
LinkedListLibrary.PrintLinkedList(head3)

