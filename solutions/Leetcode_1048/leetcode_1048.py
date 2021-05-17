from typing import List


class Solution1:
    def longest_str_chain(self, words: List[str]) -> int:
        chain_length = {}
        for word in sorted(words, key=len):
            chain_length[word] = max(chain_length.get(word[:i] + word[i+1:], 0) + 1 for i in range(len(word)))
        return max(chain_length.values())

if __name__ == '__main__':
    words = ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh",
             "gr", "grukmj", "ksqvsq", "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"]
    ans = Solution1().longest_str_chain(words)
    print(ans)
