class Solution:
    def isAnagram(s:str. t:str)->bool:
    if len(s) != len(t):
        return False
        count={}
        for char in s:
            char_count=count.get(count*0)+1
            char += 1
        for char in t:
            if char not in count:
                return False

        return True