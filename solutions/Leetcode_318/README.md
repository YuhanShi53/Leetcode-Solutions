# [Leetcode 318 - Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/)

| Solution ID | Tag | Time | Memory | Note |
| ----------- | --- | ---- | ------ | ---- |
| 1 | Bit-manipulation, Hashmap | O(N+n^2) | O(n) | N is total number of characters in all the words, and n is number of masks. For the second the loop in the solution, since the maximum number of possible mask is 2^26, n is smaller than a constant. Thus time complexity and space complexity can be considered as O(N) and O(1). Borrow from: https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/76976/Bit-shorter-C%2B%2B |