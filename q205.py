class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # a -> b, c -> b NO
        # a -> a YES
        # a -> c, a -> d NO
        # loop through s and t using i:
        # -> if letterMap[s[i]] == None: 
        #       if t[i] in letterMap.values(): return False
        #       else: letterMap[s[i]] = t[i]
        # -> elif letterMap[s[i]] != None:
        # ->    if letterMap[s[i]] != t[i]: return False
        # return True
        letterMap = {}
        for i in range(len(s)):
            if not s[i] in letterMap.keys(): 
                if t[i] in letterMap.values(): return False
                else: letterMap[s[i]] = t[i]
            elif s[i] in letterMap.keys():
                if letterMap[s[i]] != t[i]: return False

        return True
