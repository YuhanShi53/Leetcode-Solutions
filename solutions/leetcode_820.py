# https://leetcode.com/problems/short-encoding-of-words/
# Time:69% Memory:100%

class Solution:
    def minimum_length_encoding(self, words):
        words.sort(key=lambda x: len(x), reverse=True)
        self.trie = {}
        self.minimum_length = 0

        for word in words:
            self.insert_to_trie(word[::-1], self.trie)

        return self.minimum_length

    def insert_to_trie(self, word, trie):
        path_length = 1
        flag = False
        for x in word:
            path_length += 1
            if x not in trie:
                trie[x] = {}
                flag = True
            trie = trie[x]
        if flag:
            self.minimum_length += path_length

if __name__ == "__main__":
    words = ["time", "me", "bell"]
    res = Solution().minimum_length_encoding(words)
    print(res)