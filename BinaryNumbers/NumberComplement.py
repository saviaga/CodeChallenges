class Solution(object):
    def findComplement(self, num):
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
    new_Complement=Solution()
    result=new_Complement.findComplement(5)
    print(result)
