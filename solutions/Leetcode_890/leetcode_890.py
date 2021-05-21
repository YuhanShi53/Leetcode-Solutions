from typing import List

class Solution1:
    def find_and_replace_pattern(self, words, pattern):
        def normalize(word):
            mapping = {}
            for x in word:
                yield mapping.setdefault(x, len(mapping))
        p = list(normalize(pattern))
        return [word for word in words if all(x == y for x, y in zip(normalize(word), p))]

class SolutionMINE:
    def find_and_replace_pattern(self, words: List[str], pattern: str) -> List[str]:
        mapping = {}
        appeared = []
        ret = []
        for word in words:
            mapping.clear()
            appeared.clear()
            for i in range(len(word)):
                if pattern[i] not in mapping:
                    if word[i] not in appeared:
                        mapping[pattern[i]] = word[i]
                        appeared.append(word[i])
                    else:
                        break
                if mapping[pattern[i]] != word[i]:
                    break
                if i == len(word) -1:
                    ret.append(word)
        return ret

if __name__ == '__main__':
    words = ["a","b","c"]
    pattern = 'a'
    ans = Solution1().find_and_replace_pattern(words, pattern)
    print(ans)