class Solution(object):
  def checkSubarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if k == 0:
      for i in range(1,len(nums)):
        if nums[i] == nums[i-1] and nums[i]==0:
          return True
      return False
    else:
       k = abs(k)

    #if len(nums) == 2:
    #  return sum(nums) % k == 0

    sumList = []
    for num in nums:
      if len(sumList) ==0:
        sumList.append(num%k)
      else:
        sumList.append((num + sumList[-1])%k)
    #print("nums", nums)
    #print("sumList", sumList)
    kMap = set()
    for i in range(len(sumList)):
    #for n in sumList:
      n = sumList[i]
      if n in kMap or (n == 0 and i != 0):
        return True
      else:
        kMap.add(n)
    return False

    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
 
if __name__ == "__main__":
  sol = Solution()
  tests = [
    #{"input":, "output":},
    {"input1":[23, 2, 4, 6, 7], "input2": 6, "output": True},
    {"input1":[23, 2, 4, 6, 7], "input2": 0, "output": False},
    {"input1":[23, 2, 4, 6, 7], "input2": -6, "output": True},
    {"input1":[0,0], "input2": 0, "output": True},
    {"input1":[1,1], "input2": 2, "output": True},
    {"input1":[1,2,3], "input2": 6, "output": True},
  ]
      
  for test in tests:
    print(bcolors.OKGREEN + "===========testing ",test["input1"]," with ", test["input2"], bcolors.ENDC)
    try:
      output = sol.checkSubarraySum(test["input1"], test["input2"])
      assert(output == test["output"])
    except:
      print(bcolors.FAIL, "*******expect %s got %s " % (test["output"], output), bcolors.ENDC)
