class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
    self.prev=None

class DoublyLinkedList:
  def __init__(self,value):
    new_node=Node(value)
    self.head=new_node
    self.tail=new_node
    self.length=1

  def print_list(self):
    temp=self.head
    while temp is not None:
      print(temp.value)
      temp=temp.next

  def append(self,value):
    new_node=Node(value)
    if self.length==0:
      self.head=new_node
      self.tail=new_node
      self.length +=1
    else:
      self.tail.next=new_node
      new_node.prev=self.tail
      self.tail=new_node
      self.length +=1

  def pop(self):
    if self.head is None:
      return None  
    elif self.length==1:
      t=self.head
      self.length -=1
      self.head=None
      self.tail=None
      return t
    else:
      temp=self.tail
      self.tail=self.tail.prev
      self.tail.next=None
      temp.prev=None
      self.length -=1
      if self.length==0:
        self.head=None
        self.tail=None
      return temp

  def prepend(self,value):
    new_node=Node(value)
    if self.head is None:
      self.head=new_node
      self.tail=new_node
      self.length +=1
    else:
      self.head.prev=new_node
      new_node.next=self.head
      self.head=new_node
      self.length +=1

  def pop_first(self):
    if self.head is None:
      return None
    elif self.length==1:
      t=self.head
      self.length -=1
      self.head=None
      self.tail=None
      return t
    else:
      t=self.head
      self.head=self.head.next
      self.head.prev=None
      t.next=None
      self.length -=1
      if self.length==0:
        self.head=None
        self.tail=None
      return t

  def get(self,index):
    if index<0 or index>=self.length:
      return None
    temp=self.head
    if self.length/2>index:
      for _ in range(index):
        temp=temp.next
    else:  
      temp=self.tail
      for _ in range(self.length-1,index,-1):
        temp=temp.prev
      return temp

  def set_value(self,index,value):
    temp=self.get(index)
    if temp:
      temp.value=value

  def insert(self,index,value):
    if index<0 or index>=self.length:
      return None
    if index==0:
      self.prepend(value)
      self.length +=1
    if index==self.length-1:
      self.append(value)
      self.length +=1
    new_node=Node(value)
    temp=self.get(index-1)
    new_node.next=temp.next
    temp.next.prev=new_node
    new_node.prev=temp
    temp.next=new_node
    self.length +=1

  def remove(self,index):
    if index < 0 or index >= self.length:
      return None
    if index == 0:
      return self.pop_first()
    if index == self.length - 1:
      return self.pop()

    temp=self.get(index-1)
    t=temp.next
    temp.next=t
    t.next.prev=temp
    t.prev=None
    t.next=None
    self.length -=1
    retuurn t

dll=DoublyLinkedList(7)
print(dll.head.value)