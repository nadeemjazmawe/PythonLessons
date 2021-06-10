from Node import *


class Tree:

    def __init__(self, data=None):
        self._root = Node(data)

    def getRoot(self):
        return self._root

    def setRoot(self, data):
        self._root = Node(data)

    def add(self, data, helper=None):
        if helper is None:
            helper = self._root

        if self._root.getData() is None:
            self.setRoot(data)

        else:
            if data < helper.getData():
                if helper.getLeft() is None:
                    helper.setLeft(data)
                    return
                else:
                    return self.add(data, helper.getLeft())

            else:
                if helper.getRight() is None:
                    helper.setRight(data)
                    return
                else:
                    return self.add(data, helper.getRight())

    def search(self, data, helper=None):
        if helper is None:
            helper = self._root

        if helper.getData is None:
            print("data does not exist")

        elif self._root.getData() == data:
            print("data is at the root")
            return self._root

        else:
            if helper.getData() == data:
                print("data exist")
                return helper

            elif data < helper.getData() and helper.getLeft() is not None:
                return self.search(data, helper.getLeft())

            elif data > helper.getData() and helper.getRight() is not None:
                return self.search(data, helper.getRight())

            else:
                print("data does not exist")
                return None

    def findMaxNum(self):
        if self._root.getData() is None:
            return None;

        ans = self._root.getData()
        helper = self.getRoot()
        while helper.getRight() is not None:
            helper = helper.getRight()

        return helper.getData()

    def findMinNum(self):
        if self._root.getData() is None:
            return None;

        ans = self._root.getData()
        helper = self.getRoot()
        while helper.getLeft() is not None:
            helper = helper.getLeft()

        return helper.getData()
