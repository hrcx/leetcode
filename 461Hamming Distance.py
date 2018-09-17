class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a=x^y
        n=0
        while a!=0:
            n+=a&1
            a>>=1
        return n