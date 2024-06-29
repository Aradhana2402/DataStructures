from types import prepare_class


class Node:
  def __init__(self,value):
      self.value=value
      self.next=None

class LinkedList:
  def __init__(self,value):
      new_node=Node(value)
      self.head=new_node
      self.tail=new_node
      self.length=1
    
  def append(self,value):
    new_node=Node(value)
    if self.length==0:
      self.head=new_node
      self.tail=new_node
    else:
      self.tail.next=new_node
      self.tail=new_node
    self.length+=1
  
  def print_list(self):
    temp=self.head
    while temp is not None:
      print(temp.value)
      temp=temp.next
      
  def pop(self):
    if self.length==0:
      return None
    elif self.length==1:
      t=self.head
      self.head=None
      self.tail=None
      self.length -=1
      return t
    else:
      temp=self.head
      while temp.next.next is not None:
        temp=temp.next
      t=temp.next
      temp.next=None
      self.tail=temp
      self.length -=1
      return t
      
  def prepend(self,value):
    new_node=Node(value)
    if self.length==0:
      self.head=new_node
      self.tail=new_node
    else:
      new_node.next=self.head
      self.head=new_node
    self.length +=1
    
  def pop_first(self):
    if self.length==0:
      return None
    else:
      t=self.head
      self.head=self.head.next
      self.length -=1
      if self.length==0:
        self.tail=None
      return t
      
  def get(self,index):
    if index<0 or index>=self.length:
      return None
    temp=self.head
    for _ in range(index):
      temp=temp.next
    return temp
    
  def set_value(self,index,value):
    temp=self.get(index)
    if temp:
      temp.value=value
      
  def insert(self,index,value):
    if index<0 or index>self.length:
      return None
    if index==0:
      self.prepend(value)
      self.length +=1
    if index==self.length-1:
      self.append(value)
      self.length +=1
    new_node=Node(value)
    temp=self.get(index-1)
    pos=temp.next
    temp.next=new_node
    new_node.next=pos
    self.length +=1

  def remove(self,index):
    if index<0 or index>=self.length:
      return None
    if index==0:
      return self.pop_first()
    if index==self.length-1:
      return self.pop()
    prev=self.get(index-1)
    t=prev.next
    prev.next=prev.next.next
    t.next=None
    self.length -=1
    return prev

  def reverse(self):
    temp=self.head
    self.head=self.tail
    self.tail=temp
    after=temp.next
    before=None
    for _ in range(self.length):
      after=temp.next
      temp.next=before
      before=temp
      temp=after

ll=LinkedList(11)
ll.prepend(9)
ll.append(12)
ll.append(13)
ll.insert(1,10)
#ll.remove(1)
#ll.pop_first()
ll.reverse()
ll.print_list()
#print(ll.head.value)