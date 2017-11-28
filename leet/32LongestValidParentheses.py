class Solution(object):

  """def push(self):
    self.stack.append(")")

  def pop(self):
    if len(self.stack) >0:
      char = self.stack.pop[0]
      return char
    else:
      return None"""

  def increase(self):

  def decrease(self):

  def resetAndRecordValidadility(self):
    # if an invalid parenthese is found, then
    # 1. Record the currrent length
    # 2. Reset the counter.
    pass
    
  def longestValidParentheses(self, s):
    """
    :type s: str
    :rtype: int
    """
    #self.stack         = []
    self.s             = s
    self.currentLength = 0
    self.maxLength     = 0
    for char in self.s:
      
      


if __name__ == "__main__":
  sol = Solution()
  sol.longestValidParentheses("abc")
