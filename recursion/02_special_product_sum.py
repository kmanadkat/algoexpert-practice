from typing import List

# Time Complexity = O(n)
# Space Complexity = O(Depth)
def productSum(array: List[int], level = 1):
    # Base Case.
    if len(array) == 0:
      return 0
    
    sumNums = 0
    for element in array:
      if type(element) == int:
         sumNums += element
      else:
        recSum = productSum(element, level+1) 
        sumNums += (level + 1) * recSum
    
    return sumNums



# Time Complexity = O(n)
# Space Complexity = O(Depth)
def productSumBetter(array: List[int], level = 1):
    # Base Case.
    if len(array) == 0:
      return 0
    
    sumNums = 0
    for element in array:
      if type(element) is int:
         sumNums += element
      else:
        recSum = productSum(element, level+1) 
        sumNums += recSum
    
    return sumNums * level