# Python program to check if a given Binary Tree is 
# symmetric or not
 
# Node structure
class Node:
 
    # Utility function to create new node
       


# Returns True if trees with roots as root1 and root 2 
# are mirror
def isMirror(root1 , root2):
    # If both trees are empty, then they are mirror images
    #base condition 1
    

    """ For two trees to be mirror images, the following three
        conditions must be true
        1 - Their root node's key must be same
        2 - left subtree of left tree and right subtree
          of right tree have to be mirror images
        3 - right subtree of left tree and left subtree
           of right tree have to be mirror images
    """
    
    # If neither of above conditions is true then root1
    # and root2 are not mirror images
    
 
def isSymmetric(root):
    # Check if tree is mirror of itself
    return isMirror(root, root)
 
if __name__=="__main__":
    # Driver Program 
    # Let's construct the tree show in the above figure
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)
    print "Symmetric" if isSymmetric(root) == True else "Not Symmetric"
