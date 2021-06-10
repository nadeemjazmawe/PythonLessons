from Tree import Tree

tree = Tree()
print(tree.getRoot().getData())
tree.add(4)
print(tree.getRoot().getData())
tree.add(5)
print(tree.getRoot().getRight().getData())
tree.search(4)
tree.search(5)
tree.search(6)


