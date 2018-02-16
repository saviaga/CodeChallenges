"""
https://leetcode.com/problems/reverse-string/description/
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".


We can reverse string in Python in 5 different ways

1) Using loop
2)Using recursion
3)Using stack
4)Using extended slice syntax
5)Using reversed

"""

import time

class ReverseString:
    def __init__(self):
        self.s = s
        self.string=""


    def reverseStringLoop(self,s):
        """
        :type s: str
        :rtype: str
        """
        str = ""
        for l in self.s:
            str = l + str

        return str

    def reverseStringRecursion(self,s):
        """
        :type s: str
        :rtype: str
        """
        l=len(s)
        if l == 1:
            return s
        else:
            return self.reverseStringLoop(s[int(l/2):]) + self.reverseStringLoop(s[:int(l/2)])


    def reverseStringStack(self, s):
        """
        :type s: str
        :rtype: str
        """
        str=""
        stack = []
        for l in self.s:
            stack.append(l)

        while stack:
            str=str + stack[-1]
            #print(str)
            del stack[-1]
        return str

    def reverseStringSlice(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s[::-1]

        return s

    def reverseStringReverse(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = "".join(reversed(s))
        return s


if __name__=="__main__":

    s = "hello"
    reverse = ReverseString()
    #Loop Solution

    start = time.time()

    result = reverse.reverseStringLoop(s)
    print(result)
    end = time.time()
    print("Using Loop:", end - start)

    #Recursion Solution
    start = time.time()

    result = reverse.reverseStringRecursion(s)
    print(result)
    end = time.time()
    print("Using Recursion:", end - start)

    #Stack Solution
    start = time.time()
    result = reverse.reverseStringStack(s)
    print(result)
    end = time.time()
    print("Using stack:", end - start)

    # Slice Solution
    start = time.time()
    result = reverse.reverseStringSlice(s)
    print(result)
    end = time.time()
    print("Using stack:", end - start)

    # Reverse Solution
    start = time.time()
    result = reverse.reverseStringReverse(s)
    print(result)
    end = time.time()
    print("Using Reversed:", end - start)
