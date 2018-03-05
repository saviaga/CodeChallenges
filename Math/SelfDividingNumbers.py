"""
https://leetcode.com/problems/self-dividing-numbers/description/
Self Dividing Numbers
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000

"""

def testing_selfdividing(num):
    for e in str(num):
            if int(e) == 0 or (num % int(e)) > 0:
                return False
    return True

def selfDividingNumbers(left, right):
    """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
    output = []
    for n in range(left, right + 1):
        #for those numbers with more than 2 digits we iterate over each digit
        if testing_selfdividing(n):
            output.append(n)

    return output

if __name__=="__main__":
    left = 1
    right = 22
    result = selfDividingNumbers(left,right)
    print(result)