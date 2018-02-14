"""
      Given an array of 2n integers, your task is to group these integers into n pairs of integer,
      say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
      Input: [1,4,3,2]
      Output: 4
      Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

      """

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #sorted returns a new list, while sort() does the sorting in-place [::2]extracts the even indexes of the list
        return  sum(sorted(nums)[::2])



if __name__=="__main__":
    array=[1,4,3,2]
    PairSum = Solution()
    result=PairSum.arrayPairSum(array)
    print(result)
