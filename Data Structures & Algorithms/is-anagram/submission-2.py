class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)
        t1 = list(t)
        countS = {}
        countT = {}
        count = 1
        print (s1,t1)
        if(len(s1) != len(t1)):
            return False
        for i in range(0,len(s1)):
                if(s1[i] in countS):
                        countS[s1[i]] = countS[s1[i]] + 1
                if(s1[i] not in countS):
                        countS[s1[i]] = count

                if(t1[i] in countT):
                        countT[t1[i]] = countT[t1[i]] + 1
                if(t1[i] not in countT):
                        countT[t1[i]] = count
        if(countT == countS):
                return True
        
        return False
                
        