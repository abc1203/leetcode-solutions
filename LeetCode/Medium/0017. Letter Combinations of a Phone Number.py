phone_map = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        idea:
         - letterCombinations(digits[1:]) returns all comb for digits[1:]
         - then add all possible letter for digits[0]
        """
        
        if len(digits) == 0: return []
        elif len(digits) == 1: return phone_map[digits]

        ans = []
        remaining_comb = self.letterCombinations(digits[1:])

        for letter in phone_map[digits[0]]:
            for comb in remaining_comb:
                ans.append(letter + comb)
        
        return ans


        
