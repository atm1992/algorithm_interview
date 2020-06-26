# -*- coding: UTF-8 -*-

"""
Mobvista 的第一道面试题
验证密码是否合格：
1、密码长度要大于8
2、密码中需要包含数字、小写字母、大写字母、其余字符这4种中的至少3种
3、不能重复出现超过2个字符的子字符串
"""


def validate(pwd):
    if not pwd or len(pwd) <= 8:
        return "NG"
    count = 0
    for i in pwd:
        if '0' <= i <= '9':
            count |= 0x1
        elif 'a' <= i <= 'z':
            count |= 0x2
        elif 'A' <= i <= 'Z':
            count |= 0x4
        else:
            count |= 0x8
    one_num = 0
    while count > 0:
        one_num += 1
        count &= count - 1
    if one_num < 3:
        return "NG"
    if isSame(pwd):
        return "NG"
    return "OK"


def isSame(pwd):
    if len(pwd) < 6:
        return False
    return (pwd[:3] in pwd[3:]) or isSame(pwd[1:])


if __name__ == '__main__':
    print(validate("bc09@bc97"))
