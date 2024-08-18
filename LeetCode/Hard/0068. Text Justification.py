class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        text = []
        i = 0
        while i < len(words):
            line = []
            line_len = 0
            while i < len(words) and line_len + len(line) + len(words[i]) <= maxWidth:
                line.append(words[i])
                line_len += len(words[i])
                i += 1
            text.append(line)
        
        ans = []
        for i in range(len(text)):
            line = text[i]
            spaces = maxWidth
            for word in line: spaces -= len(word)
            spaceCnt = max(1, len(line)-1)
            baseCnt = spaces / spaceCnt
            extraCnt = spaces % spaceCnt

            line_ans = ""
            if i != len(text)-1:
                for word in line[:-1]:
                    line_ans += word
                    for i in range(baseCnt): line_ans += " "
                    if extraCnt > 0: line_ans += " "
                    extraCnt -= 1
                line_ans += line[-1]
                for _ in range(maxWidth - len(line_ans)): line_ans += " "
            else:
                for word in line[:-1]:
                    line_ans += word
                    line_ans += " "
                line_ans += line[-1]
                for _ in range(maxWidth - len(line_ans)): line_ans += " "
            ans.append(line_ans)
            
        return ans
        
