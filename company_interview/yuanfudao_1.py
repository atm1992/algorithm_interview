"""
1. 有个order表：

orderid、userid、dt、fee

用sql求用户累计成单金额达到给定值的时间。
30
80
100 
输出如下：
userid、paid_sum、paidtime

考点：sql里的窗口函数
"""

csv测试数据如下：
oid,uid,dt,fee
0001,A1,20200501,25
0002,A1,20200502,35
0003,A1,20200503,15
0004,A1,20200505,23
0005,A1,20200509,93
0006,A2,20200403,43
0007,A2,20200419,39
0008,A2,20200409,10
0009,A2,20200209,56
0010,A3,20200219,26
0011,A3,20200226,47
0012,A3,20200416,79
建表语句如下：
CREATE EXTERNAL TABLE order_table
(
oid STRING ,
uid STRING ,
dt  STRING ,
fee int 
)
COMMENT '订单表'
WITH SERDEPROPERTIES("line.delim"="\n","serialization.encoding"="GBK","field.delim"=",","serialization.null.format"="")
STORED AS  INPUTFORMAT "org.apache.hadoop.mapred.TextInputFormat"
OUTPUTFORMAT "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat"
LOCATION '/user/test/order';

答案如下：
SELECT UID,
       min(accum_sum) AS fee_sum,
       min(dt) AS first_dt
FROM
  (SELECT UID,
          dt,
          accum_sum,
          CASE
              WHEN AA.accum_sum <=30 THEN 'L1'
              WHEN AA.accum_sum > 30
                   AND AA.accum_sum <=80 THEN 'L2'
              WHEN AA.accum_sum > 80
                   AND AA.accum_sum <=100 THEN 'L3'
              ELSE 'L4'
          END AS LEVEL
   FROM
     (SELECT UID,
             dt,
             sum(fee) over(partition BY UID
                           ORDER BY dt) AS accum_sum
      FROM order_table
      GROUP BY UID,
               oid,
               dt,
               fee
      ORDER BY UID,
               dt) AA) AAA
GROUP BY UID,
         LEVEL
ORDER BY UID,
         first_dt

    



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


"""
4. 用户登陆表user_login_table
*  user_name 用户名
*  date 用户登陆日期
现在想知道连续7天都登陆平台的重要用户。
输出要求如下：
*  user_name 用户名（连续7天都登陆的用户） 
"""   

SELECT aa.name,
       max(aa.dt)-min(aa.dt) diff,
       collect_set(aa.dt)
FROM
  (
  SELECT a.name,
          a.dt,
          a.dt-a.rn as num
   FROM
     (SELECT name,
             dt,
             row_number() over (partition BY name
                                ORDER BY dt) rn
      FROM user_login_table
      GROUP BY name,
               dt
      ) a      
  ) aa
GROUP BY name, num
