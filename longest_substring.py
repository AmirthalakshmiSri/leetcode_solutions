class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res=set()
        r=0
        l=0
        for i in range(0,len(s)):
            while s[i] in res:
                res.remove(s[l])
                l=l+1
            res.add(s[i])
            r=max(r,i-l+1) 
        return r       
