class Treenode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,value):
        if not self.root:
            self.root = Treenode(value)
        else:
            self._insert(self.root,value)
    def _insert(self,node,value):
        if value<node.value:
            if node.left is None:
                node.left = Treenode(value)
            else:
                self._insert(node.left,value)
        else:
            if node.right is None:
                node.right = Treenode(value)
            else:
                self._insert(node.right,value)
    def pre_order(self):
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current:
                print(current.value, end=" ")
                stack.append(current.right)
                stack.append(current.left)

    def in_order(self):
        stack = []
        current = self.root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print(current.value, end=" ")
                current = current.right
    def post_order(self):
        stack = []
        current = self.root
        last = None
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peeknode = stack[-1]
                if peeknode.right and last != peeknode.right:
                    current = peeknode.right
                else:
                    print(peeknode.value, end=" ")
                    last = stack.pop()



bst = BST()

print("Menu:")
print("1. Insert")
print("2. In-order Traversal")
print("3. Pre-order Traversal")
print("4. Post-order Traversal")
print("5. Exit")

while True:
  choice = int(input("Enter your choice: "))
  if choice == 1:
    value = int(input("Enter the value to insert: "))
    bst.insert(value)
  elif choice == 2:
    print("In-order Traversal:")
    bst.in_order()
    print()
  elif choice == 3:
    print("Pre-order Traversal:")
    bst.pre_order()
    print()
  elif choice == 4:
    print("Post-order Traversal:")
    bst.post_order()
    print()
  elif choice == 5:
    break
  else:
    print("Invalid choice. Please try again.")
