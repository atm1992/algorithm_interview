"""
1. 有个order表：

orderid、userid、paidtime、paidfee

用sql求用户累计成单金额达到给定值的时间。
2000
3000
5000 
10000
输出如下：
userid、paid_sum、paidtime

考点：sql里的窗口函数
"""


"""
2. 求n的m次方
"""
def func0(n, m):
    def func(n, m):
        if m == 0:
            return 1
        elif m == 1:
            return n    
        else:
            ret = func(n, m/2)
            if m % 2 == 0:                
                return  ret * ret
            else:
                return  ret * ret * n
            
    if m < 0:
        ret = func(n, 0-m)
        return float(1) / ret
    else:
        ret = func(n, m)
        return ret
        
"""
3. 含有非负整数的数组，相邻两个数不能同时取，求能拿到的最大和

考点：动态规划
"""        

def func2(arr):
    
    dp = [0 for i in range(len(arr)+1)]    
    dp[1] = arr[0]
    
    for i in range(1, len(arr)):
        dp[i+1] = max(arr[i]+dp[i-1], dp[i])
        
    return dp[-1]
