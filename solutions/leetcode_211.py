""" Leetcode 211 - Add and Search Word - Data Structure Design

https://leetcode.com/problems/add-and-search-word-data-structure-design/

1. SM Dict-Trie: Add: [Time: O(k) Space: O(n)] Search: [Time: O(n) Space: ] 

"""


class WordDictionary:
    """ 1. SM Dict-Trie """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for x in word:
            node.setdefault(x, {})
            node = node[x]
        node['end'] = 1

    def search(self, word: str) -> bool:

        def search_helper(word, trie):
            if not word:
                if trie.get('end', False):
                    return True
                else:
                    return False

            flag = False
            if word[0] == '.':
                for x in trie.keys():
                    if x != 'end':
                        flag = search_helper(word[1:], trie[x])
                    if flag:
                        return True
            elif trie.get(word[0], False):
                flag = search_helper(word[1:], trie[word[0]])
            else:
                flag = False

            return flag

        return search_helper(word, self.trie)


if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord('a')
    obj.addWord('ab')
    print(obj.search('a'))
    print(obj.search('a.'))
    print(obj.search('.b'))
