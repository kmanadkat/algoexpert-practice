# Method 1: 
# Time = O(2^n)
def getNthFib(n):
  # Base Case
  if n <= 0:
    return 0
  if n <= 2:
    return n - 1 

  # Recursive Call
  ans = getNthFib(n-2) + getNthFib(n-1)

  return ans


# Method 2
# Time = O(n)
# Space = O(n)
def getNthFibLoop(n):
  # Base Case
  if n <= 0:
    return 0
  if n <= 2:
    return n - 1 

  # Memoization
  dt = {}
  dt[0] = 0
  dt[1] = 0
  dt[2] = 1
  for i in range(3, n):
    dt[i] = dt[i-1] + dt[i-2]
  
  dt[n] = dt[n-1] + dt[n-2]
  ans = dt[n]

  return ans


  
# Method 3
# Time = O(n)
# Space = Constant
def getNthFibLoopBetter(n):
  # Base Case
  if n <= 0:
    return 0
  if n <= 2:
    return n - 1 

  # Memoization
  dt = [0,1]
  for _ in range(3, n):
    numSum = dt[0] + dt[1]
    numLast = dt[1]
    dt[0] = numLast
    dt[1] = numSum
  
  ans = dt[0] + dt[1]

  return ans


  
# Method 4
# Time = O(n)
# Space = O(n)
def getNthFibRecBetter(n, dt={}):
  # Base Case
  if n <= 0:
    return 0
  if n <= 2:
    dt[1] = 0
    dt[2] = 1 

  if dt.get(n) != None:
    return dt[n]

  dt[n-1] = getNthFibRecBetter(n - 1, dt)
  dt[n] = dt[n-1] + dt[n-2]
  return dt[n]

print(getNthFibRecBetter(1))
print(getNthFibRecBetter(2))
print(getNthFibRecBetter(3))
print(getNthFibRecBetter(4))
print(getNthFibRecBetter(5))