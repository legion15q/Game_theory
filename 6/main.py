import numpy as np


class Node:
    def __init__(self, key, val, depth_):
        self.left = None
        self.right = None
        self.key = key
        self.val = val
        self.depth = depth_

    def _is_have_child(self, root):
        if (root.left is not None) or (root.right is not None):
            return True
        else:
            return False

    # Insert Node
    def insert(self, key, val, depth_):

        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key, val, depth_)
                else:
                    self.left.insert(key, val, depth_)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key, val, depth_)
                else:

                    self.right.insert(key, val, depth_)
        else:
            self.key = key

    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.key),
        if self.right:
            self.right.PrintTree()

    def inorderTraversal(self, root, val, side='left'):
        res = []
        if root:
            if side == 'left':
                res = self.inorderTraversal(root.left, val)
            else:
                res = self.inorderTraversal(root.right, val, 'right')
            res.append(root.key)
            if self._is_have_child(root):
                # print(root.left.val, root.right.val)
                if ((root.depth  + 1)% 2 != 0):
                    # ход игрока A
                    try:
                        if root.left.val[0] > root.right.val[0]:
                            root.val = root.left.val
                        else:
                            root.val = root.right.val
                    except:
                        self.inorderTraversal(root, val, 'right')
                else:
                    try:
                        if root.left.val[1] > root.right.val[1]:
                            root.val = root.left.val
                        else:
                            root.val = root.left.val
                    except:
                        self.inorderTraversal(root, val, 'right')
                val.append([root.left.val, root.right.val, root.left.depth])
                print(root.val, root.depth)
            if side == 'left':
                res = res + self.inorderTraversal(root.right, val)
            else:
                res = res + self.inorderTraversal(root.left, val, 'right')
        return res


def main():
    mytree = Node(6, None, 0)
    mytree.insert(8, None, 1)
    mytree.insert(4, None, 1)
    mytree.insert(2, None, 2)
    mytree.insert(5, (-2, 10), 2)
    mytree.insert(7, (4, 1), 2)
    mytree.insert(9, (8, -2), 2)
    mytree.insert(1, (5, 6), 3)
    mytree.insert(3, (-5, 10), 3)
    val = []
    tree_queue = mytree.inorderTraversal(mytree, val)
    print(tree_queue)
    print(val)


    return 1


if __name__ == '__main__':
    main()
