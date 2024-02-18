
class Node:

  def __init__(self, data=None):
    self.data = data
    self.next = None

class Head:

  def __init__(self):
    self.head = None

  def print(self):
    val = self.head
    while val is not None:
      print(val.data)
      val = val.next


pointer = Head()
pointer.head = Node('1')
p2 = Node('12')
p3 = Node('13')
p4 = Node('14')
p5 = Node('15')

pointer.head.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
pointer.print()






