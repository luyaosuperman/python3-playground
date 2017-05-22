#!/usr/bin/python3
import unittest

class Solution(unittest.TestCase):

	#Wrong Wrong Wrong
	def sol(self, n):
		dividentSet = set()
		for i in range(n,1,-1):
			if len(dividentSet) == 0:
				dividentSet.add(i)
			else:
				add = True
				for j in dividentSet:
					if j % i == 0:
						add = False
						break
				if add == True:
					dividentSet.add(i)

		#print(dividentSet)
		'''i = 0
		while True:
			i += 1
			found = True
			for j in dividentSet:
				if i % j != 0:
					found = False
					break
			if found:
				print(i)
				return
		'''


		#print(dividentSet)
		dividentList = list(dividentSet)
		dividentList.sort(reverse = True)
		removeList = []
		for i in range(len(dividentList)):
			for j in range(i+1,len(dividentList)):
				for k in range(j+1,len(dividentList)):
					if i!= j and j!= k and i!= k:
						i1 = dividentList[i]
						j1 = dividentList[j]
						k1 = dividentList[k]
						if (i1 * j1) % k1 == 0:
							print("{0} {1} remove {2}".format(i1,j1,k1))
							removeList.append(k1)
						#if (j1 * k1) % i1 == 0:
						#	print("{0} {1} remove {2}".format(j1,k1,i1))
						#	removeList.append(i1)
						#if (i1 * k1) % j1 == 0:
						#	print("{0} {1} remove {2}".format(i1,k1,j1))
						#	removeList.append(j1)
		print("dividentList", dividentList)
		print("removeList", removeList)
		dividentSet = set(dividentList) - set(removeList)
		print("dividentSet", dividentSet)
		print("*****")

		dividentList = list(dividentSet)
		dividentList_ = list()
		removeList = []
		for i in range(len(dividentList)):
			for j in range(i+1, len(dividentList)):
				i1 = dividentList[i]
				j1 = dividentList[j]
				hcf = self.computeHCF(i1,j1)
				
				dividentList_.append(hcf)
				dividentList_.append(i1//hcf)
				dividentList_.append(j1//hcf)
				if hcf != 1:
					removeList.append(i1)
					removeList.append(j1)
		dividentSet = set(dividentList_) - set(removeList)
		print("dividentList_", dividentList_)
		print("removeList", removeList)
		print("dividentSet", dividentSet)
		print("+++++")

		result = 1
		for i in list(dividentSet):
			result *= i
		print(result)

	def computeHCF(self,x, y):
   		# choose the smaller number
	    if x > y:
	        smaller = y
	    else:
	        smaller = x
	    for i in range(1, smaller+1):
	        if((x % i == 0) and (y % i == 0)):
	            hcf = i
	            
	    return hcf


	def test_1(self):
		self.sol(10)
		print("----------------")
		self.sol(20) #232792560

		#self.assertEqual(

		#	)

if __name__ == '__main__':
    unittest.main()