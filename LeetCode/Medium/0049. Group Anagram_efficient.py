class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Algo:
            1. decompose each string into a tuple of chars recording each freq
            2. create hashmap with key = tuple & value = string
            3. return the values of each element in the hashmap
        '''
        mp = collections.defaultdict(list)

        for s in strs:
            str_tuple = [0] * 26
            for c in s:
                str_tuple[ord(c)-ord('a')] += 1
            
            mp[tuple(str_tuple)].append(s)
        
        return mp.values()
