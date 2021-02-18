class Solution:
    def romanToInt(self, s: str) -> int:
        sm = 0
        mp = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        bl = False
        for i in range(len(s)):
            try:
                if(bl):
                    bl = False
                    continue
                if(mp[s[i+1]]>mp[s[i]]):
                    sm+=mp[s[i+1]]-mp[s[i]]
                    bl = True
                else:
                    sm+=mp[s[i]]
            except:
                sm+=mp[s[i]]
        return sm