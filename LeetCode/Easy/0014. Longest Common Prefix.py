class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        idea:
         - find the common pref of strs[0] and strs[1] => common_pref
         - then find common pref of common_pref and strs[2] ...
        """

        if len(strs) == 1: return strs[0]

        common_pref = strs[0]

        for s in strs[1:]:
            while common_pref != s[:len(common_pref)]:
                common_pref = common_pref[:-1]
                if common_pref == "": return ""
        
        return common_pref
