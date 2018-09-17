#Ture,False大写
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        A = 0
        B = 0
        for i in moves:
            if i == 'R':
                A += 1
            if i == 'L':
                A -= 1
            if i == 'U':
                B += 1
            if i == 'D':
                B -= 1

        if A == 0 and B == 0:
            return True
        else:
            return False