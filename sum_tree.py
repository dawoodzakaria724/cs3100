#This code has been adapted from the following sources:

#https://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree

#https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/




# A Node class that represents a node in a binary tree

class Node:

    def __init__(self, data):

        self.left = None

        self.right = None

        self.data = data




# A binary tree class

class BinaryTree:

    #Creating a class variable root

    def __init__(self):

        self.root = None



    #Function to recursively insert a node inside the tree

    #It takes the a single data node and insert it in order

    def insert(self, data):

        #If this is an empty tree, then you should insert

        #the node at the root

        if self.root is None:

            self.root = Node(data)

        else:

            #If not empty, call the recursive private function

            #_add

            self._add(data, self.root)

    # A private function that inserts a data to the right

    #or left tree of the given node based on the value of the node

    def _add(self, data, node):

        #If the new data is smaller, then insert to the left

        if data < node.data:

            if node.left is not None:

                # Recusive call if the tree is not empty

                self._add(data, node.left)

            else:

                node.left = Node(data)

        else:

            if node.right is not None:

                # Recusive call if the tree is not empty

                self._add(data, node.right)

            else:

                node.right = Node(data)


    # This function takes an array and creates a complete

    #tree from the given array

    def insertComplete(self, arr):

        #call the private recursive function

        self.root = self._insertComplete(arr,self.root, 0, len(arr))


    # Private recursive function that constructs a complete BT

    def _insertComplete(self, arr,node,i,n):

        if i < n:

            node = Node(arr[i])

            node.left = self._insertComplete(arr, node.left, 2*i+1,n)

            node.right = self._insertComplete(arr, node.right, 2*i+2,n)

            return node


    # Print a tree. It calls the private recursive function

    def printTree(self):

        if self.root is not None:

            self._printTree(self.root)


    # Private recursive function that prints a tree in order

    def _printTree(self, node):

        if node is not None:

            self._printTree(node.left)

            print(node.data, end = " " )

            self._printTree(node.right)

    def _sum(self, node):

        if node is None:

            return 0

        else:

            # recursive call to get the sum of node + left + right.
            # the sum is returned.
            return self._sum(node.right) + node.data + self._sum(node.left)

    def isSumTree(self):
        # Check if root is empty
        if self.root is None:

            return 0

        else:

            # calling _isSumTree
            return self._isSumTree(self.root)


    # A private recursive function that checks if a tree is a sum tree
    # It takes a node as an input
    def _isSumTree(self, node):
        # base case:
        if (node is None) or ((node.left is None) and (node.right is None)):

            return 1

        # both sides of the tree are summed into a single variable.
        left = self._sum(node.left)
        right = self._sum(node.right)

        # recursive call:
        if (node.data == left + right) and (self._isSumTree(node.left) and (self._isSumTree(node.right))):

            return 1

        return 0


def main():

    arr = [32,13,3,4,5,2,1,2,2] #Should return true

    bComplete = BinaryTree()

    bComplete.insertComplete(arr)

    bComplete.printTree()

    print()

    print(bComplete.isSumTree())

    if bComplete.isSumTree():

        print("this is a sum tree")

    else:

        print("not a sum tree")


    arr = [12,13,3,4,5,2,1,2,2] #Should return false

    bComplete2 = BinaryTree()

    bComplete2.insertComplete(arr)

    bComplete2.printTree()

    print()

    print(bComplete2.isSumTree())

    if bComplete2.isSumTree():

        print("this is a sum tree")

    else:

        print("not a sum tree")




if __name__ == "__main__":

    main()
