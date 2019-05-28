class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    # def is_empty(self):
    #     return self.root is None

    def getHeight(self, root):
        #Write your code here
        left_height = 0
        right_height = 0
        if root is None:
            return 0
        if root.left:
            # return 3
            left_height = self.getHeight(root.left) + 1
        if root.right:
            right_height = self.getHeight(root.right) + 1

        return max(left_height, right_height)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
