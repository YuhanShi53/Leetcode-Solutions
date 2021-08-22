# [Leetcode 307 - Range Sum Query - MutableRange Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)

| Solution ID | Tag | Time | Memory | Note |
| ----------- | --- | ---- | ------ | ---- |
| 1 | Segment Tree | O(n) + O(logn) | O(n) | O(n) for create the segment tree, and O(logn) for querying and updating. |
| 2 | Fenwick Tree | O(nlogn) for constructor, O(logn) for update, O(logn) for sumRange. | O(n) | n is length of nums. Borrow from: <https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation>. |
