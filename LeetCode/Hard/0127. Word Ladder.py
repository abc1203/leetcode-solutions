class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int

        idea:
         - approach 1 (naive BFS => TLE)
             - construct graph s.t. every word is neighboured by one-diff words
             - then find shortest path by running bfs on beginWord
         - approach 2
             - instead of constructing graph, go through every letter in alphbet and
             - check if the new word in is wordList
             - still using bfs to find shortest path
        """
        
        wordList = set(wordList)
        alph = "abcdefghijklmnopqrstuvwxyz"
        visited = set([beginWord])
        q = [(beginWord, 1)]

        if endWord not in wordList: return 0

        while q:
            currWord, dis = q.pop(0)
            for i in range(len(currWord)):
                prefix, suffix = currWord[:i], currWord[i+1:]
                
                for l in alph:
                    newWord = prefix + l + suffix
                    if newWord in wordList and newWord not in visited:
                        if newWord == endWord: return dis+1
                        
                        q.append((newWord, dis+1))
                        visited.add(newWord)
        return 0

        
