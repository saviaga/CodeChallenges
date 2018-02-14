"""
https://leetcode.com/problems/number-complement/description/
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
       """


def findComplement(num):
        """
        :type num: int
        :rtype: int
        """
        i=0
        binary_num = bin(num)[2:]
        string=list(binary_num)
        complement=""

        while i < len(string):
            if string[i]=="0":
                string[i]="1"
            else:
                string[i]="0"
            i+=1

        complement=''.join(string)

        return int(complement,2)


if __name__=="__main__":
    num=5
    result=findComplement(num)
    print(result)
