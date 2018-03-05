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
    selfdividing = False
    for e in str(num):
        try:
            if (num % int(e)) == 0:
                selfdividing = True
            else:
                selfdividing =  False
                break
        except:
            selfdividing =  False
            break
    return selfdividing

def selfDividingNumbers(left, right):
    """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
    output = []
    while left <= right:
        #for those numbers with more than 2 digits we iterate over each digit
        if testing_selfdividing(left):
            output.append(left)
        left += 1

    return output

if __name__=="__main__":
    left = 1
    right = 22
    result = selfDividingNumbers(left,right)
    print(result)