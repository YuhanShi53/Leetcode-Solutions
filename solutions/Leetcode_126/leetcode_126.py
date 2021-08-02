from typing import List


class SolutionMINE:
    def find_ladders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        ladders = [[beginWord]]
        wordList = {x: True for x in wordList}
        flag = False
        while ladders:
            temp = []
            for ladder in ladders:
                next_words = self.find_next(ladder[-1], endWord, wordList, ladder)
                for next_word in next_words:
                    if next_word == endWord:
                        flag = True
                    temp.append(ladder + [next_word])
            if flag:
                return [ladder for ladder in temp if ladder[-1] == endWord]
            ladders = temp
        return []

    def find_next(self, word, endWord, wordList, visited):
        candidates = []
        for i in range(len(word)):
            if word[i] != endWord[i]:
                new_word = word[:i] + endWord[i] + word[i+1:]
                if wordList.get(new_word, False) and new_word not in visited:
                    candidates.append(new_word)
        if candidates:
            return candidates
        for i in range(len(word)):
            if word[i] != endWord[i]:
                for x in 'abcdefghijklmnopqrstuvwxyz':
                    if x != word[i]:
                        new_word = word[:i] + x + word[i+1:]
                        if wordList.get(new_word, False) and new_word not in visited:
                            candidates.append(new_word)
        return candidates
