class BinaryTree:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_node(self, data):
        if data == self.data:  # if binary tree already has an element -> return
            return
        elif data < self.data:
            # if element < than data -> add left node
            if self.left:
                self.left.insert_node(data)
            else:
                self.left = BinaryTree(data)
        else:
            # if element > than data -> add right node
            if self.right:
                self.right.insert_node(data)
            else:
                self.right = BinaryTree(data)

    def in_order_traversal(self): # left -> root -> right
        tree_data = list()
        if self.left:
            tree_data += self.left.in_order_traversal()
        tree_data.append(self.data)
        if self.right:
            tree_data += self.right.in_order_traversal()
        return tree_data

node = BinaryTree(3)
print(node.data)

#modification 1
#another-branch
#branch to pull
