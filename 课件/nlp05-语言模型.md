[toc]



# 基本概念

设法减少历史基元的个数，将历史映射到等价类，使等价类的数目远远小于原来不同历史基元的数目

![image-20220605162922910](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220605162922910.png)

将两个历史映射到同一个等价类，当且仅当这两个历史中的最近的 n-1 个基元相同

![image-20220605162740746](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220605162740746.png)

这种情况下的语言模型称为 ==n-gram 模型==，其实就是==一个位置的概率仅与其前面的 n-1 个位置有关==。

- n = 1时，基元 $w_i$ 独立于历史，不用算条件概率
- n = 2时，bi-gram被称为1阶马尔科夫链
- n = 3时，tri-gram被称为2阶马尔科夫链
- 以此类推

为了保证条件概率在 i = 1时有意义，同时保证句子内所有字符串的概率和为1，可以在句子首尾增加开始<BOS>和结束<EOS>标志

![image-20220605164701973](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220605164701973.png)

## 例子

![image-20220605164833395](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220605164833395.png)

- 基于二元文法

![image-20220605164847989](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220605164847989.png)

## 应用

在给定拼音翻译成汉字的任务中，我们可以得到目标方程

![image-20220605165237969](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220605165237969.png)

如果汉字总数为 N

- 一元语法
  - 样本空间为 N
  - 只选择使用出现频率最高的汉字
- 二元语法
  - 样本空间是 $N^2$
  - 效果明显提高

那我们如何获得 n-gram 语法模型呢（模型里面的一些概率，需要知道才能求整个句子的概率）

# 参数估计

采用最大似然估计的方法，就是直接统计，==用历史串出现且$w_i$出现的次数除以历史串出现的次数当做条件概率==

![image-20220605170423332](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220605170423332.png)

这样算，由于数据集不能包含所有情况的出现，会引起零概率问题，连乘有一项是0，整个结果就是0，一票否决了其他项的概率，这是不合理的。

# 数据平滑

思想：使零概率增大，非零概率减小，消除零概率

目标：测试样本的语言模型==困惑度越小越好==

## 困惑度

![image-20220605174055028](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220605174055028.png)

![image-20220605174517544](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220605174517544.png)

## 加 1 平滑

每一种情况出现的次数加 1（对于所有的基元，每种基元出现的次数都加 1）

## 减值法/折扣法

修改训练样本中事件的实际计数，使实际出现的不同事件的概率之和小于1，剩余的概率量分配给未见概率

### Good-Turing估计

设 N 是原来训练样本数据的大小，$n_r$ 是在样本中正好出现 $r$ 次的事件的数目

- 平滑：==保持出现的总样本数不变，但是将一些样本数分给了在样本中没有出现过的事件==
  - 没出现的样本数指的是没出现样本的==数学期望==

![image-20220607000532445](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607000532445.png)

==实际应用中，问题都是离散的，出现次数最多的样本的出现次数不变，因为不存在 $n_{r+1}$==

平滑后，时间出现的概率如下：

![image-20220607000554144](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607000554144.png)

原样本中所有时间的概率之和为：

![image-20220606233146043](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220606233146043.png)

$\frac{n_1}{N}\\$ 的概率剩余量可以分给没出现的事件（r=0），是没有出现过的样本的概率总和

#### 例子

对以read开头的bi-gram进行平滑，要==注意的是最后一项没变==

![image-20220607000914940](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607000914940.png)

- 以 read 开始，没有出现过的bi-gram的概率总和为 $p_0 = \frac{n_1}{N}\\$

- 以 read 开始，没出现过的bi-gram的个数为（==假定语料库中每次词都可以出现在 read 后面==）

  ![image-20220607001050555](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607001050555.png)

- 以 read 为开始的2-gram的 概率平均为 $\frac{p_0}{n_0}\\$

  ![image-20220607001241540](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607001241540.png)

**适用于大词汇集产生的符合多项式分布的大量的观察数据**

### Back-off（后退/后备）方法

对每个计数 $r > 0$ 的 n 元文法的出现次数减值，把因减值而省下来的剩余概率根据低阶的 （n-1）gram分配给未见事件。

![image-20220607215434646](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607215434646.png)

![image-20220607215506766](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607215506766.png)

### 绝对减值法

==每个计数 r 中减去同样的量==，剩余的概率量由未见事件均分

![image-20220607215845225](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607215845225.png)

- $N$ 是各种 $r$ 的和
- $R$ 是所有可能事件的数目，当事件为 n-gram 时，如果统计基元为词，且词汇集大小为 L，则 $R = L^n$

- 对于出现了的事件，每个都贡献了 $\frac{b}{N}\\$ 的概率给没有出现的事件（和为 $n_0$）

### 线性减值法

从每个计数 $r$ 中==减去与该计数成正比的量==

![image-20220607220426968](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607220426968.png)

每个存在计数贡献概率为 $\alpha*\frac{N_r}{N}\\$，对 $r$ 求和，得到存在计数总的贡献概率为 $\alpha$

==绝对减值法产生的 n-gram 通常优于线性减值法==

### 总结

![image-20220607220847403](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607220847403.png)

## 删除插值法

用低阶语法估计高阶语法

- 3-gram不能准确估计时用 2-gram 代替
- 下面同理

![image-20220607221157247](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607221157247.png)

将训练语料分为两部分，从原始语料中删除一部分作为留存数据

![image-20220607221251250](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607221251250.png)

# 语言模型的自适应

训练语言模型时的语料往往来自不同的领域，语言模型对训练文本的类型，主题等都很敏感

n元语言模型的独立性假设的前提在很多情况下不成立

## 基于缓存的语言模型

==问题：在文本中刚刚出现过的一些词在后边句子中再次出现的可能性往往较大，大于 n-gram模型预测的概率==

解决的思路：语言模型通过 n-gram 的线性插值求得

![image-20220607222349964](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607222349964.png)

- 通常的做法，认为前面 K 个词在缓存中，一个词的概率等于其在缓存中出现的概率

  ![image-20220607222547423](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607222547423.png)

  - 缺陷：缓存中词的重要性独立于该词与当前词的距离

- 改进：缓存中每个词对当前词的影响随与该词的距离的增大呈指数级衰减

  - ==缓存中不止存 K 个，而是存前面所有的词，影响程度随距离增大而衰减==

  ![image-20220607222803480](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607222803480.png)

## 基于混合方法的语言模型

问题：训练数据往往是不同领域的，但是测试语料一般是同源的。为了获得最佳心梗，模型必须适应各种不同类型的语料对其的影响

处理方法：==将语言模型划分成 n 个子模型，整个模型通过线性插值得到==

![image-20220607223026399](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607223026399.png)

### 基本方法：

- 将训练语料聚类
- 模型运行时识别测试语料的主题
- 确定适当的训练语料自己，分别建立特定的语言模型
- 插值获得整个语言模型

### EM迭代计算插值系数（感觉可以不看）

- 对 n 个类，随机初始化插值系数 $\lambda$

- 根据整个模型计算概率和期望

- 更新

  ![image-20220607224138541](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607224138541.png)

- 不断迭代，直到收敛

## 基于最大熵的语言模型

结合不同信息源的信息构建一个语言模型，每个信息源提供一组关于模型参数的约束条件。

==在所有满足约束的模型中，选择熵最大的模型。==

比如有两个信息源，$f，g$ 分别是两个模型定义的函数（约束）

![image-20220607230600458](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607230600458.png)

![image-20220607230606796](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607230606796.png)

- 这两个信息源都分别提供了一组约束

- 我们并不是让这些公式对所有可能的历史都成立，而是更宽松的限制。即它们在训练数据上的平均成立即可

  ![image-20220607230719962](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220607230719962.png)

# 语言模型应用举例

## 基于语言模型的分词方法

最基本的做法是以词为独立的统计基元，但效果不大好

![image-20220608001453854](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608001453854.png)

具体实现时，将词分类，将词序列转成词类序列

![image-20220608002233252](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608002233252.png)

词序列变类序列

![image-20220608002329478](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608002329478.png)

求概率

![image-20220608002449672](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608002449672.png)

![image-20220608002544361](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608002544361.png)

## 分词与词性标注一体化

![image-20220608002713509](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608002713509.png)

### 基于词性的三元统计模型

![image-20220608002830537](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608002830537.png)

### 基于单词的三元统计模型

![image-20220608002947964](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608002947964.png)

### 分词与词性标注一体化模型

![image-20220608003008129](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608003008129.png)

舍弃一部分没有用的

![image-20220608003641388](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608003641388.png)

计算 $\beta$

![image-20220608004058262](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608004058262.png)
