class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        j = 0
        count = 1
        for i in range(len(chars)-1):
            currChar = chars[i]

            if chars[i] != chars[i+1]:
                chars[j] = currChar
                j += 1
                if count > 1:
                    for c in str(count):
                        chars[j] = c
                        j += 1
                
                if i+1 == len(chars)-1:
                    chars[j] = chars[i+1]
                    j += 1
                count = 1
            elif i+1 == len(chars)-1:
                chars[j] = currChar
                j += 1
                for c in str(count+1):
                    chars[j] = c
                    j += 1
            else: count += 1
        return j if j != 0 else 1

        
