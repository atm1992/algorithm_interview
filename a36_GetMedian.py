# -*- coding: UTF-8 -*-
"""
数据流中的中位数。
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

解题思路：使用两个堆来实现。前面一个大顶堆，后面一个小顶堆。堆内部的数据无需排序，只需确保大顶堆的根节点值为最大，
小顶堆的根节点值为最小 即可。大顶堆的根节点值小于等于小顶堆的根节点值（即 前面的大顶堆中所有值 都小于等于 后面的小顶堆中所有值）
通过一个flag来确保第奇数次插入新元素到前面的大顶堆中，第偶数次插入新元素到后面的小顶堆中。通过该flag还可知道当前数据流中的总数量是奇数还是偶数。
说明：若第奇数次插入到大顶堆中的新元素大于小顶堆的根节点值，则将该新元素先插入到小顶堆中，然后弹出小顶堆的根节点，将其插入到大顶堆；
若第偶数次插入到小顶堆中的新元素小于大顶堆的根节点值，则将该新元素先插入到大顶堆中，然后弹出大顶堆的根节点，将其插入到小顶堆。
"""


class Solution:
    def __init__(self):
        self.head = []
        self.tail = []
        # head_flag为True时，插入新元素到head中，插入完以后，变成False
        # 因此，head_flag为True说明此时数据流中共有偶数个元素；head_flag为False说明此时数据流中共有奇数个元素
        self.head_flag = True

    def Insert(self, num):
        if self.head_flag:
            if self.tail and self.tail[0] < num:
                self.head.insert(0, self.tail.pop(0))
                self.tail.append(num)
                min_index = self.tail.index(min(self.tail))
                self.tail.insert(0, self.tail.pop(min_index))
            elif not self.head or self.head[0] < num:
                self.head.insert(0, num)
            else:
                self.head.append(num)
        else:
            if self.head[0] > num:
                self.tail.insert(0, self.head.pop(0))
                self.head.append(num)
                max_index = self.head.index(max(self.head))
                self.head.insert(0, self.head.pop(max_index))
            elif not self.tail or num < self.tail[0]:
                self.tail.insert(0, num)
            else:
                self.tail.append(num)
        self.head_flag = not self.head_flag

    # GetMedian方法要求输入一个参数，否则验证不通过。因此这里随便写了一个形参x，实际并未用到
    def GetMedian(self, x):
        if not self.head:
            return None
        if self.head_flag:
            return (self.head[0] + self.tail[0]) / 2.0
        else:
            return self.head[0]