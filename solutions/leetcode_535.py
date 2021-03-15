""" Leetcode 535 - Encode and Decode TinyURL

https://leetcode.com/problems/encode-and-decode-tinyurl/

1. Time: O(1) Memory: O(1)

"""

import random
import string


class Codec1:
    """ 1. Hashmap

    Borrow from: https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/100268/Two-solutions-and-thoughts

    """

    def __init__(self):

        self._alphabet = string.ascii_letters + string.digits
        self._url_to_code = {}
        self._code_to_url = {}

    def encode(self, longUrl: str) -> str:
        while longUrl not in self._url_to_code:
            code = ''.join(random.choice(self._alphabet) for _ in range(6))
            if code not in self._code_to_url:
                self._url_to_code[longUrl] = code
                self._code_to_url[code] = longUrl
        return 'http://tinyurl.com/' + self._url_to_code[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self._code_to_url.get(shortUrl[-6:], '')


if __name__ == '__main__':
    long_url = 'https://www.leetcode.com/problems/design-tinyurl'
    codec = Codec1()
    print(codec.encode(long_url), codec.decode(codec.encode(long_url)))
