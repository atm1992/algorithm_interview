1. 设计模式知道哪些？观察者模式

2. Kafka:数据一致性怎么保证？

3. Spark take(n)的实现，怎么快速取n个数据
   # 源码如下：
  def take(num: Int): Array[T] = withScope {
    val scaleUpFactor = Math.max(conf.getInt("spark.rdd.limit.scaleUpFactor", 4), 2)
    if (num == 0) {
      new Array[T](0)
    } else {
      val buf = new ArrayBuffer[T]
      val totalParts = this.partitions.length
      var partsScanned = 0
      while (buf.size < num && partsScanned < totalParts) {
        // The number of partitions to try in this iteration. It is ok for this number to be
        // greater than totalParts because we actually cap it at totalParts in runJob.
        var numPartsToTry = 1L
        val left = num - buf.size
        if (partsScanned > 0) {
          // If we didn't find any rows after the previous iteration, quadruple and retry.
          // Otherwise, interpolate the number of partitions we need to try, but overestimate
          // it by 50%. We also cap the estimation in the end.
          if (buf.isEmpty) {
            numPartsToTry = partsScanned * scaleUpFactor
          } else {
            // As left > 0, numPartsToTry is always >= 1
            numPartsToTry = Math.ceil(1.5 * left * partsScanned / buf.size).toInt
            numPartsToTry = Math.min(numPartsToTry, partsScanned * scaleUpFactor)
          }
        }

        val p = partsScanned.until(math.min(partsScanned + numPartsToTry, totalParts).toInt)
        val res = sc.runJob(this, (it: Iterator[T]) => it.take(left).toArray, p)

        res.foreach(buf ++= _.take(num - buf.size))
        partsScanned += p.size
      }

      buf.toArray
    }
  }






4. Spark的调度，DagScheduler, TaskScheduler什么作用

5. reduceByKey, groupByKey区别，线上groupByKey可能会出现什么？

6. 宽窄依赖，任务怎么划分

7. 数据倾斜，线上会有哪些表现，可能会引起什么？怎么解决

8. 数据挖掘：基尼系数、信息增益、信息熵等概念，SVM高斯核

9. 两个字符串的最长公共子串。类似问题：最长公共子序列。（ https://leetcode-cn.com/problems/longest-common-subsequence/ ）
