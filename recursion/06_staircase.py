# Time Complexity : O(steps ^ height)
def staircaseTraversal(height, maxSteps):
  if height <= 1:
    return 1


  numWays = 0
  for i in range(1, min(maxSteps, height) + 1):
    numWays += staircaseTraversal(height - i, maxSteps)
  
  return numWays
  


# TIme Complexity: O(steps * height)
def staircaseTraversalBetter(height, maxSteps, dt={0:1, 1:1}):
  if height <= 1:
    return 1

  if dt.get(height) != None:
    return dt[height]

  numWays = 0
  for i in range(1, min(maxSteps, height) + 1):
    smallHeightSteps = staircaseTraversalBetter(height - i, maxSteps, dt)
    numWays += smallHeightSteps

  # Memoize Ans
  dt[height] = numWays

  return numWays



# TIme Complexity: O(steps * height)
# DP
def staircaseTraversalDP(height, maxSteps):
  if height <= 1:
    return 1
  
  waysToTop = [0 for _ in range(height+1)]
  waysToTop[0] = 1
  waysToTop[1] = 1

  for currentStep in range(2, height + 1):
    delta = 1
    numWays = 0
    while delta <= maxSteps:
      prevStep = currentStep - delta
      # Check index >= 0 for waysToTop
      if(prevStep >= 0):
        numWays += waysToTop[prevStep]
      delta += 1
    
    waysToTop[currentStep] = numWays
  
  return waysToTop[height]

print(staircaseTraversalDP(4,4))