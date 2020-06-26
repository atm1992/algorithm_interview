# -*- coding: UTF-8 -*-

"""
替换空格。
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

解题思路：若是直接从前往后遍历原字符串，然后遇到一个空格，就要将后面的所有字符都后移两个字符，这样操作的时间复杂度为O(n^2)，因此不采用。

采用的方法为：先遍历一次原字符串，统计出原字符串中的空格个数，根据原字符串的长度以及空格个数新建一个指定长度的字符数组。
然后同时从后往前遍历原字符串与新的字符数组，若当前字符不是空格，则直接copy到字符数组中；若是空格，则依次将'02%'这三个字符写入字符数组。
遍历完毕后，将字符数组转换为字符串即可返回结果
"""


def replaceSpace(s):
    if not isinstance(s, str) or len(s) < 1:
        return ''
    spaceNum = 0
    for i in s:
        if i == " ":
            spaceNum += 1
    newStrLen = len(s) + spaceNum * 2
    newStr = [''] * newStrLen
    idxNew, idxOrigin = newStrLen - 1, len(s) - 1
    while idxOrigin >= 0:
        if s[idxOrigin] == " ":
            newStr[idxNew - 2:idxNew + 1] = ['%', '2', '0']
            idxNew -= 3
            idxOrigin -= 1
        else:
            newStr[idxNew] = s[idxOrigin]
            idxNew -= 1
            idxOrigin -= 1
    return ''.join(newStr)


if __name__ == '__main__':
    print(replaceSpace("  3 4j fh sj  "))
