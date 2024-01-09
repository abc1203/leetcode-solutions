class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp = {}

        for word in strs:
            ordered_word = "".join(sorted(word))

            if mp.get(ordered_word) is not None:
                mp.get(ordered_word).append(word)
            else:
                mp[ordered_word] = [word]
        
        res = []
        for word_list in mp.values():
            res.append(word_list)
        
        return res
