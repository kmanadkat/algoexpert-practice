import sys

class TreeNode:
  def __init__(self, data) -> None:
      self.value = data
      self.left = None
      self.right = None


# Time Complexity: O(n)
def findClosestValueInBst(tree: TreeNode, target):
    # Write your code here.
    if tree == None:
      return -sys.maxsize - 1

    currClose = tree.value
    leftClose =  findClosestValueInBst(tree.left, target)
    rightClose = findClosestValueInBst(tree.right, target)

    ans = None
    if abs(target - leftClose) < abs(target - rightClose):
      if abs(target - leftClose) < abs(target - currClose):
        ans = leftClose
      else:
        ans = currClose
    
    else:
      if abs(target - rightClose) < abs(target - currClose):
        ans = rightClose
      else:
        ans = currClose

    return ans


# Time Complexity: O(height) 
def findClosestValueInBst(tree: TreeNode, target):
    # Write your code here.
    if tree == None:
      return -sys.maxsize - 1

    currClose = tree.value
    nextClose = -sys.maxsize - 1

    # Edge Case - diff is 0
    if target - currClose == 0:
      return currClose

    # Target larger then root - Search right for more closer value
    if tree.right and target > currClose:
      nextClose = findClosestValueInBst(tree.right, target)
    else:
      nextClose = findClosestValueInBst(tree.left, target)

    ans = nextClose
    if abs(target - ans) > abs(target - currClose):
      ans = currClose

    return ans


# Time Complexity: O(height) 
# Iterative
def findClosestValueInBst(tree: TreeNode, target):
  if tree == None:
    return
  
  closest = -sys.maxsize - 1
  currentNode = tree
  while currentNode != None:
    if abs(target - currentNode.value) < abs(target - closest):
      closest = currentNode.value
    
    # Update Current Node
    if target > currentNode.value:
      currentNode = currentNode.right
    elif target < currentNode.value:
      currentNode = currentNode.left
    else:
      break

  return closest