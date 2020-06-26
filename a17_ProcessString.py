# -*- coding: UTF-8 -*-

"""
字符串合并处理。

详细描述：
将输入的两个字符串合并。
对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。这里的下标意思是字符在字符串中的位置。
对排序后的字符串进行操作，如果字符为‘0’——‘9’或者‘A’——‘F’或者‘a’——‘f’，则对他们所代表的16进制的数进行BIT倒序的操作，
并转换为相应的大写字符。如字符为‘4’，为0100b，则翻转后为0010b，也就是2。转换后的字符为‘2’；
如字符为‘7’，为0111b，则翻转后为1110b，也就是e。转换后的字符为大写‘E’。

举例：输入str1为"dec"，str2为"fab"，合并为“decfab”，分别对“dca”和“efb”进行排序，排序后为“abcedf”，转换后为“5D37BF”
输入:两个字符串,需要异常处理
输出:合并处理后的字符串
"""


def process_string(s1, s2):
    ss = s1 + s2
    odd, even = "", ""
    # 提取奇数子串和偶数子串
    for i, v in enumerate(ss):
        if i % 2 == 0:
            even += v
        else:
            odd += v
    # 分别对奇数子串和偶数子串进行排序
    odd = "".join(sorted(odd))
    even = "".join(sorted(even))
    # n0 >= n1，偶数子串可能会比奇数子串多一个字符
    n0 = len(even)
    n1 = len(odd)
    res = ""
    char_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    # 对字符串进行转换。若字符在 '0' ~ '9' or 'a' ~ 'f' or 'A' ~ 'F'范围内，则进行转换。否则不做任何处理。
    for i in range(n0):
        t0 = even[i].upper()
        if t0 in char_list:
            # bin(8) 将十进制数转换为二进制字符串
            # [2:] 去除二进制字符串开头的"0b"
            # rjust(4, "0") 将字符串进行右对齐，若字符串的长度不足4位，则在原始字符串的左侧填充字符"0"
            # 例如：bin(2)[2:] 的结果为 '10' ；bin(2)[2:].rjust(4, "0") 的结果为 '0010'
            # [::-1] 对二进制字符串进行逆序
            # int("100111",2) 将二进制字符串转换为十进制数
            res += char_list[int(bin(char_list.index(t0))[2:].rjust(4, "0")[::-1], 2)]
        else:
            res += even[i]
        if i < n1:
            t1 = odd[i].upper()
            if t1 in char_list:
                res += char_list[int(bin(char_list.index(t1))[2:].rjust(4, "0")[::-1], 2)]
            else:
                res += odd[i]
    return res


if __name__ == '__main__':
    s1 = "DKSq8qykpgKIZxiRKmQ9QkZt909PffE6Gyfc57dBx7p20D42bWJRzKqGGCzzQ4p7Z32Dsx2Cf8G2841lPuAZNb"
    s2 = "K0fHodOVFlbl220ov260TPOrmZ328d1E89OatcL88EXr622RdklXtXazO7wMoc6DEKU45eQ5VBUy2YFjgJX"
    res = "000080844444444444C42CA2A2626A661E1E1E1E11919959BD7D73F3FBGBGBG7J7KGKHKILJNKOKOKOMOPPPQRQRQRQVSWTXUXUYVZXZX5ZDZ3Z353DBDBB7BFFgFjFkFkgkilllmlomoopqpqprqrsttutxvxwyxyyzzzz"
    print(process_string(s1, s2) == res)
    print(process_string("dec", "fab"))
