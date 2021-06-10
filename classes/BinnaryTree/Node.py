class Node:

    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def setData(self, data):
        self._data = data

    def getData(self):
        return self._data

    def setLeft(self, left):
        self._left = Node(left)

    def getLeft(self):
        return self._left

    def setRight(self, right):
        self._right = Node(right)

    def getRight(self):
        return self._right


# def printN():
#     print("hello world213")
#
# x = 10
# n = Node(10)
# print("hello" + n.getData())
