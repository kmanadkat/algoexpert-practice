# Space Complexity = O(n * 2^n)
# Time Complexity = O(n * 2^n)
# Recursive Solution
def powerset(array):
    if len(array) == 0:
      return [[]]

    recAns = powerset(array[1:])
    output = []
    firstElement = [array[0]]

    for element in recAns:
      output.append(element)
      output.append(firstElement + element)

    return output


# Iterative Solution
def powersetItr(array):
  if len(array) == 0:
    return [[]]

  output = [[]]
  for element in array:
    initialLength = len(output)
    for index in range(initialLength):
      subArray = output[index]
      output.append(subArray + [element])
  
  return output



print(powerset([1,2,3]))
print(powersetItr([1,2,3]))