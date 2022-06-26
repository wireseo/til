# knowledge: X
# concepts: BST, serialization
# comment: not as difficult; just do preorder
# runtime: X, not mine
# memory usage: X, not mine

class Codec:
    def serialize(self, root):
        # OLR (preorder)
        def preorder(node):
            if node:
                serial.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                serial.append('N')
        serial = []
        preorder(root)
        return ' '.join(serial)

    def deserialize(self, data):
        def preorder():
            val = next(serial)
            if val == 'N':
                return None
            node = TreeNode(int(val))
            node.left = preorder()
            node.right = preorder()
            return node
        serial = iter(data.split())
        return preorder()