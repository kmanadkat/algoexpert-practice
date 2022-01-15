def getPermutations(array):
    # Base Cases
    if len(array) == 0:
      return []
    if len(array) == 1:
      return [array]
    
    # Get Permutations of array size less by 1
    recAns = getPermutations(array[1:])
    output = []

    # Put first item in subarrays at every index
    for subArray in recAns:
      for j in range(len(subArray) + 1):
        row = subArray[0:j] + [array[0]] + subArray[j:]
        output.append(row)
    
    return output


print(getPermutations([1,2,3]))