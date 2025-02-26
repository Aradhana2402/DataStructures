class Node:
  def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None


class BinarySearchTree:
  def __init__(self):
      self.root = None

  def insert(self, value):
      new_node = Node(value)
      if self.root is None:
          self.root = new_node
          return True
      temp = self.root
      while (True):
          if new_node.value == temp.value:
              return False
          if new_node.value < temp.value:
              if temp.left is None:
                  temp.left = new_node
                  return True
              temp = temp.left
          else: 
              if temp.right is None:
                  temp.right = new_node
                  return True
              temp = temp.right

  def contains(self, value):
      if self.root is None:
          return False
      temp = self.root
      while (temp):
          if value < temp.value:
              temp = temp.left
          elif value > temp.value:
              temp = temp.right
          else:
              return True
      return False

  def BFS(self):
      curr=self.root
      queue=[]
      result=[]
      queue.append(curr)
      while len(queue)>0:
          curr=queue.pop(0)
          result.append(curr.value)
          if curr.left is not None:
              queue.append(curr.left)
          if curr.right is not None:
              queue.append(curr.right)
      return result

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())



"""
  EXPECTED OUTPUT:
  ----------------
  [47, 21, 76, 18, 27, 52, 82]

"""









