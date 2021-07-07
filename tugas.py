class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res


# Preorder traversal
# Root -> Left ->Right


    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

# Postorder travresersal
# Left ->Right -res> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = res+self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res


cuaca = input("     ")
rot = input(str("input akar :"))
simpulkiri = input(str("(input simpul kiri :"))
simpulkanan = input(str("input simpul kanan :"))
rantingkiri = input(str("input ranting kiri :"))
rantingkanan = input(str("input ranting kanan :"))
root = Node(rot)
root.insert(simpulkiri)
root.insert(simpulkanan)
root.insert(rantingkiri)
root.insert(rantingkanan)
print(root.inorderTraversal(root))
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))

if(cuaca == "hujan") or (cuaca == "angin"):
    print("belum bisa main karena=", cuaca)
elif (cuaca == "lembab") or (cuaca == "cerah"):
    print("bisa main karena = ", cuaca)
else:
    print("cuaca salah", cuaca)
