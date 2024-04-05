class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s문자열과 t문자열을 t문자가 s에 전부 포함되어있으면 true 그렇지 않으면 False 출력
        
        countS, countT = {}, {}

        if len(s) != len(t): #애초에 길이가 안맞으면 false 출력
            return False

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0) 


        return countS == countT 