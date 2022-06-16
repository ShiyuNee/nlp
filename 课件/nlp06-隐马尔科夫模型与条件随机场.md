[toc]

# 马尔可夫模型

系统状态转移方程：

![image-20220608103203117](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608103203117.png)

- 假设1：离散的二阶马尔可夫链（当前状态只与前一个状态有关）：

  ![image-20220608103343531](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608103343531.png)

- 假设2：在假设 1 基础上，假设转态与时间无关

  ![image-20220608103531711](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608103531711.png)

==该随机过程称为马尔可夫模型==

马尔可夫模型中，==状态转移概率==$a_{ij}$需要满足

![image-20220608104009088](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608104009088.png)

状态序列的概率为

![image-20220608104432418](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608104432418.png)

# 隐马尔可夫模型（HMM）

是一个双重随机过程，我们不知道具体的状态序列，只知道状态转移的概率

![image-20220608104752388](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608104752388.png)

## HMM的组成

- 模型中的转态数为 N

- 从每个状态可能输出的不同符号数 M

- 状态转移概率矩阵

  ![image-20220608105005268](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608105005268.png)

- 从一个状态中，观察到的符号的概率分布矩阵

  ![image-20220608105235073](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608105235073.png)

- 初始状态的概率分布

  ![image-20220608105708721](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608105708721.png)

  

  ![image-20220608105735324](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608105735324.png)

## HMM流程

![image-20220608105853171](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608105853171.png)

# 前向算法

## 理论讲解

解决的问题：==已知输出序列和和给定模型，快速计算观察序列的概率==

![image-20220608110216155](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608110216155.png)

其实就是遍历所有可能产生的状态序列，然后使用这些状态序列计算生成观察序列的概率，然后求和

但是可能状态序列会很多，难以直接搜索

![image-20220608110510215](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608110510215.png)

利用前面变量计算概率。就是输出序列是固定的，对==当前时刻所有状态求和==

![image-20220608111948944](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608111948944.png)

t+1时间的前向变量可以根据 t 时刻前向变量递推得到

![image-20220608151346200](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608151346200.png)

## 算法流程

![image-20220608151611591](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608151611591.png)

复杂度为 $O(N^2T)$

# 后向算法

## 理论讲解

![image-20220608152146218](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608152146218.png)

和前向算法一样，用动态规划计算后向量

第一步

![image-20220608152326333](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608152326333.png)

概率为

![image-20220608152417038](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608152417038.png)

第二步

![image-20220608152428880](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608152428880.png)

概率为（==以后面所有情况的和来计算当前时刻的后向量==）

![image-20220608153525465](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608153525465.png)

归纳顺序为从后向前，因此称为后向算法

![image-20220608152540792](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608152540792.png)

## 流程

![image-20220608153812307](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608153812307.png)

# Viterbi搜索算法

问题：==如何发现最优状态序列，能够最好地解释观察序列==

## 第一种解释

==给定模型和输出序列，寻找每个时刻出现概率最大的状态==

![image-20220608155157194](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608155157194.png)

我们可以将上面式子转化成和前向，后向算法相关的形式

![image-20220608155618777](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608155618777.png)

- 认为模型在时间 t 到达状态 $s_i$ ，并且输出是 $O=o_1 \cdots o_T$

- 这可以拼接成前向（控制前面的输出）和后向变量（控制后面的输出）

  ![image-20220608155754121](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608155754121.png)

- 方程转化为

  ![image-20220608155810713](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608155810713.png)

分母以时间 $t$ 的状态无关，下标 $t$ 可以是任意的

![image-20220608160736142](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608160736142.png)

我们将分母与分子整合起来，得到

![image-20220608160813193](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608160813193.png)

因此，在 $t$ 时刻，最优状态是

![image-20220608160840074](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608160840074.png)

==上面这种解释可能会有问题，因为每个状态单独最优不一定使整体的状态序列最优，可能两个最优状态之间的转移概率为 0==

![image-20220608161239095](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608161239095.png)

## 第二种解释

Viterbi算法：动态搜索最优状态序列

思想：从到前一个时间的所有最优路中选一个到当前时间的最优路

![image-20220608162708058](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608162708058.png)

![image-20220608163228430](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608163228430.png)

我们得到变量的递推公式

![image-20220608163759696](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608163759696.png)

解释：对于第 $t+1$ 个时刻，会相对于 $t$ 时刻增加一个节点，对于每一个状态，其前面的路径都是最优的。

- 类比于求最短路，当前节点为 $v$ ，dis[v] = min(dis[u] + [u,v])

### 流程

![image-20220608171836178](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608171836178.png)

![image-20220608172626652](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608172626652.png)

# 参数学习

刚刚都是给定模型和输出序列，求最优的状态序列

现在是==给定一个观察序列，如何求得模型的参数，使得观察概率出现的概率最大==

## 已知状态序列（存在大量标注数据）

用最大似然估计来计算参数：==直接统计估计==

![image-20220608173602468](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608173602468.png)

![image-20220608173620811](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608173620811.png)

## 不存在大量标注数据

### 期望值最大化算法

- 初始化时随机地给模型的参数赋值（遵循约束的前提下，比如概率和为 1）
- 用当前模型，可以得到从某一状态转移到另一状态的期望次数。用这些期望次数得到新的模型参数
- 循环估计，参数收敛于最大似然估计

![image-20220608195903118](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608195903118.png)

![image-20220608195959451](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608195959451.png)

我们通过上面的值，利用下面的式子对模型参数进行重新估计

- 重新估计初始状态，转移概率和发射概率

![image-20220608200100155](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608200100155.png)

![image-20220608200110873](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608200110873.png)

## 前向后向算法

就是上面的过程

- 参数随机初始化

- 执行 EM 算法

  ![image-20220608203632952](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608203632952.png)

- 结束

# CRFs（没学懂）

基本思路：给定观察序列 $X$ ，输出标识序列 $Y$。通过计算 $P(Y|X)$ 计算最优标注序列

![image-20220608233142349](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608233142349.png)

==为了增加标注的准确率，我们添加前一个词的标签，而不是只以当前位置的输入为依据==

序列标注问题可以建模为简单的链式结构，在一定独立性限制的情况下，$(X,Y)$也是条件随机场

![image-20220608233227362](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608233227362.png)



![image-20220608233739502](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220608233739502.png)