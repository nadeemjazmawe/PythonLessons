from Tree import Tree

tree = Tree()
print(tree.getRoot().getData())
tree.add(4)
print(tree.getRoot().getData())
tree.add(8)
tree.add(3)
tree.add(2)
tree.add(1)
tree.add(0)
tree.add(6)
tree.add(7)
tree.add(10)
tree.add(6.5)
tree.add(9)



print(tree.getRoot().getRight().getData())
tree.search(4)
tree.search(5)
tree.search(6)
print(tree.findMaxNum())
print(tree.findMinNum())


