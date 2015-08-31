from queue import *

class IntQueue:
    
    def __init__(self):
        self.queue = Queue()

    def enqueue(self, x):
        if isinstance(x, int):
            self.queue.put(x)
        else:
            print('Item isn\'t integer, can\'t enqueue')

    def dequeue(self):
        return self.queue.get()

    def isEmpty(self):
        return self.queue.empty()

class IntStack:

    def __init__(self):
        self.stack = list()

    def push(self, x):
        if isinstance(x, int):
            self.stack.append(x)
        else:
            print('Item isn\'t integer, can\'t push')

    def pop(self):
        return self.stack.pop()

    def checkSize(self):
        return len(self.stack)

class BTNode:

    def __init__(self, k, p=None, leftchild=None, rightchild=None):
        self.key = k
        self.parent = p
        self.leftc = leftchild
        self.rightc = rightchild
        
    def assignLeft(self, v):
        self.leftc = BTNode(v, self)

    def assignRight(self, v):
        self.rightc = BTNode(v, self)

class BTree:

    def __init__(self, x):
        if isinstance(x, int):
            self.root = BTNode(x)
        else:
            raise TypeError('Item isn\'t node')

    def add(self, value, parentValue):
        pN = self.preorder(self.root, parentValue)
        if pN == None:
            print('Parent not found')
        elif pN.leftc == None:
            pN.assignLeft(value)
        elif pN.rightc == None:
            pN.assignRight(value)
        else:
            print('Parent has two children, node not added')

    def delete(self, value):
        n = self.preorder(self.root, value)
        if (n.leftc == None) and (n.rightc == None):
            if n.parent.leftc == n:
                n.parent.leftc = None
            else:
                n.parent.rightc = None
        else:
            print('Node not deleted, has children')

    def pprint(self):
        self.preprint(self.root)

    def preprint(self, node):
        if node == None:
            return
        print(node.key)
        self.preprint(node.leftc)
        self.preprint(node.rightc)

    def preorder(self, node, value):
        if node == None:
            return None
        elif node.key == value:
            return node
        lc = self.preorder(node.leftc, value)
        rc = self.preorder(node.rightc, value)
        if lc != None:
            return lc
        elif rc != None:
            return rc
        else:
            return None
                
class GVert:

    def __init__(self):
        self.adj = []

    def addAdj(self, n):
        if n in self.adj:
            print("Edge already exists.")
        else:
            self.adj.append(n)

    def printAdj(self):
        print(self.adj)


class GGraph:

    def __init__(self):
        self.graph = {}

    def addVertex(self, value):
        if value in self.graph:
            print("Vertex already exists")
        else:
            self.graph[value] = GVert()

    def addEdge(self, value1, value2):
        if (value1 in self.graph) and (value2 in self.graph):
            self.graph[value1].addAdj(value2)
            self.graph[value2].addAdj(value1)
        else:
            print("One or more vertices cannot be found.")

    def findVertex(self, value):
        if value in self.graph:
            self.graph[value].printAdj()
        else:
            print("Vertex not found.")


tuquo = IntQueue()
print("\nTesting Queue")
for i in range(1,11):
    tuquo.enqueue(i)
for i in range(1,11):
    l = tuquo.dequeue()
    print(l)

plates = IntStack()
print("\nTesting Stack")
for i in range(1,11):
    plates.push(i)
for i in range(1,11):
    l = plates.pop()
    print(l)

print("\nTesting Binary Tree")
poplar = BTree(1)
poplar.add(2, 1)
poplar.add(3, 1)
poplar.add(4, 2)
poplar.add(5, 2)
poplar.add(6, 3)
poplar.add(7, 3)
poplar.add(8, 4)
poplar.add(9, 4)
poplar.add(10, 5)
poplar.pprint()
print("\nDeleting Children")
poplar.delete(10)
poplar.delete(8)
poplar.pprint()

print("\nTesting Graph")
spreadsheet = GGraph()
for i in range(1, 11):
    spreadsheet.addVertex(i)
spreadsheet.addEdge(1, 2)
spreadsheet.addEdge(1, 3)
spreadsheet.addEdge(1, 4)
spreadsheet.addEdge(1, 10)
spreadsheet.addEdge(2, 3)
spreadsheet.addEdge(2, 4)
spreadsheet.addEdge(4, 9)
spreadsheet.addEdge(3, 6)
spreadsheet.addEdge(3, 7)
spreadsheet.addEdge(3, 8)
spreadsheet.findVertex(1)
spreadsheet.findVertex(2)
spreadsheet.findVertex(3)
spreadsheet.findVertex(4)
spreadsheet.findVertex(10)

