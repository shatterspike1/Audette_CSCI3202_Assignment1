import Lib

class IntQueue:
    
    def __init__(self):
        self.queue = q.Queue()

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
        elif pN.left == None:
            pN.assignLeft(value)
        elif pN.right == None:
            pN.assignRight(value)
        else:
            print('Parent has two children, node not added')

    def delete(self, value):
        n = self.preorder(self.root, value)
        if (n.leftc == None) and (n.rightc == None):
            n = None
        else:
            print('Node not deleted, has children')

    def pprint(self):
        self.preprint(self.root)

    def preprint(self, node):
        if node == None:
            return
        print(node.key)
        preprint(node.leftc)
        preprint(node.rightc)

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
            print('Node not found')
            return None
                
class GVert:

    def __init__(self, adj=[]):
        self.adj = adj
        self.dist = int("inf")
        self.parent = None

    def setDist(self, d):
        self.dist = d

    def setParent(self, p):
        self.parent = p

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
        if self.graph[value]:
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

    def find(self, value):
        for k, v in self.graph():
            setDist(int("inf"))
            setParent(None)

        iq = iq.IntQueue()

        self.graph[value].setDist(0)
        iq.enqueue(value)

        while not iq.isEmpty():

            u = iq.dequeue()

            for n in u.adj:
                if n.dist == int("inf"):
                    n.setDist(u.dist + 1)
                    n.setParent(u)
                    iq.enqueue(n)
