# -*- coding: UTF-8 -*-
"""
有N个面包，有三种吃法，每次吃1个，每次吃2个，每次吃3个。返回所有的吃法序列
例如：f(3) = [[1,1,1],[1,2],[2,1],[3]]
"""


def func(n):
    if n < 1:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1, 1], [2]]
    if n == 3:
        return [[1, 1, 1], [1, 2], [2, 1], [3]]
    res1 = func(n - 1)
    for i in res1:
        i.append(1)
    res2 = func(n - 2)
    for i in res2:
        i.append(2)
    res3 = func(n - 3)
    for i in res3:
        i.append(3)
    return res1 + res2 + res3


def func_backtrack(N, tmp):
    '''
	使用backtrack
    '''
	if N == 0:
		result.append(tmp[:])
		return 
	
	for i in range(1, 4):
		if N >= i:
			tmp.append(i)
			func_backtrack(N-i, tmp)
			tmp.pop(-1)


if __name__ == '__main__':
    print(func(4))
    
    result = []
    func_backtrack(4, [])
    print(result)
