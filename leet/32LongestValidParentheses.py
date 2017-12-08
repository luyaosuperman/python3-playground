class Solution(object):

  def findFirstPair(self, s, start,finish):
    for i in range(start+1,finish):
      if s[i-1] == "(" and s[i] == ")":
        return (i-1,i)
    return None,None

  def longestValidParentheses(self, s):
    if s is None or len(s) <= 1:
      return 0

    l,r = self.__longestValidParentheses(s)
    print("++++++ l",l,"r",r)
    return r - l + 1
    
  def __longestValidParentheses(self, s, start=-1, finish=-1):
    """
    :type s: str
    :rtype: int
    """
    #self.stack         = []
    #if s is None or len(s) <= 1:
    #  return 0

    if start == -1:
      start = 0
      finish = len(s)


    leftVisited,rightVisited = self.findFirstPair(s, start,finish)
    #start = 0
    #finish = len(s)
    if leftVisited is None: # can't find a pair at all
      return -100,-100

    leftValid = True
    rightValid = True
    # expand to left and right from here.
    # Corner case 1: reach the edge
    while True:
      print(leftValid, rightValid,leftVisited,rightVisited,s[leftVisited:rightVisited+1])
      if leftValid == True:
        print("leftValid == True")
        if leftVisited >= 2 and \
            s[leftVisited - 2] == "(" and s[leftVisited - 1] == ")":
          print("cond 1")
          leftVisited -= 2
          continue

        elif leftVisited >= 1 and s[leftVisited - 1] == "(":
          print("cond 2")
          leftVisited -= 1
          leftValid = False
          continue

      if rightValid == True:
        print("rightValid == True")
        if rightVisited < len(s) - 2 and \
            s[rightVisited + 1] == "(" and s[rightVisited + 2] == ")":
          print("cond 3")
          rightVisited += 2
          continue

        elif rightVisited < len(s)-1  and s[rightVisited + 1] == ")":
          print("cond 4")
          rightVisited += 1
          rightValid = False
          continue

      #it can reach here in two cases
      # leftValid or rightValid is False
      # it is still valid, but hit the edge
      print("*", leftValid, rightValid, leftVisited,rightVisited)

      if leftValid == False and rightValid == False:
        #need to decide if to continue
        if leftVisited == 0 and rightVisited == len(s):
          break
        if leftValid == rightValid:
          print("-reset as entire pair is valid")
          leftValid = True
          rightValid = True
      else:
        break

      

      

    print("--", leftValid, rightValid,         leftVisited,rightVisited,s[leftVisited:rightVisited+1])

    #current = rightVisited - leftVisited + 1
    #if not leftValid:
      #current -= 1
    #if not rightValid:
      #current -= 1
    if not leftValid:
      leftBoundary = leftVisited + 1
    else:
      leftBoundary = leftVisited

    if not rightValid:
      rightBoundary = rightVisited -1
    else:
      rightBoundary = rightVisited 
    print("-- leftBoundary", leftBoundary, "rightBoundary", rightBoundary)

    if leftValid:
      llBoundary, lrBoundary = self.__longestValidParentheses(s, start, leftVisited)
      if lrBoundary >= leftBoundary - 1 and lrBoundary != -100:
        leftBoundary = llBoundary

    if rightValid:
      rlBoundary, rrBoundary = self.__longestValidParentheses(s, rightVisited + 1, finish)
      if rlBoundary <= rightBoundary + 1 and rlBoundary != -100:
        rightBoundary = rrBoundary

    return leftBoundary, rightBoundary

    '''return max(
      self.longestValidParentheses(s, start, leftVisited),
      current,
      self.longestValidParentheses(s, rightVisited + 1, finish)
      )'''


      


if __name__ == "__main__":
  sol = Solution()
  tests = [
    {"input"  : "(())(())","output" : 8},
    {"input"  : "(()","output" : 2},
    {"input"  : "()","output" : 2},
    {"input"  : ")()())","output" : 4},
    {"input"  : "()(()","output" : 2}, # lef par brakes the rule
    {"input"  : "(()(((()","output" : 2},
    {"input"  : "()(())","output" : 6},
    {"input"  : ")()())()()(","output" : 4},
    {"input"  : ")(((((()())()()))()(()))(","output" : 22},
  ]
  errorCount = 0
  for test in tests:
    print("testing %s ===============" % test["input"])
    output = sol.longestValidParentheses(test["input"])
    try:
      assert(output == test["output"]
      )
    except:
      print(
        "\033[91m****Error input: %s ==> output: %s , expect: %s\033[0m" % 
        (
          test["input"],
          output,
          test["output"]
          )
        )
      errorCount += 1

  if errorCount > 0:
    print("\033[91mTotal %s error(s)\033[0m" % errorCount)
