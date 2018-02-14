class Solution:
        def hammingDistance(self, x, y):
            """
            :type x: int
            :type y: int
            :rtype: int
            """
            return bin(x ^ y).count("1")


if __name__=="__main__":
    distance = Solution()
    result=distance.hammingDistance(3,4)
    print(result)



