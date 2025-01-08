class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        countR = {}
        countM = {}


        for i in range(len(magazine)):
            countM[magazine[i]] = 1 + countM.get(magazine[i], 0)


        for i in range(len(ransomNote)):
            countR[ransomNote[i]] = 1 + countR.get(ransomNote[i], 0)


        for char in countR:
            if countR[char] > countM.get(char, 0):
                return False

        return True

