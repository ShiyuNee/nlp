# 1.机器翻译的困难

- 普遍存在的歧义和未知现象
- 机器翻译不仅是字符串的转换
- 机器翻译的解不唯一，而且始终存在人为的标准

# 2.基本翻译方法

- 直接转换法

  - 从源句子表层出发，将单词，短语，句子直接换成目标语言。必要时进行简单的语序调整

- 基于规则的翻译方法

  ![image-20220609002207945](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220609002207945.png)

  - 执行过程是：独立分析--独立生成--相关转换，又称为基于转换的翻译方法
  - 优点：可以较好的保持原文的结构，对语言现象已知或句法结构规范的源语言具有较强的处理能力和较好翻译效果
  - 缺点：规则由人工编写

- 基于中间语言的翻译方法

  - 方法：输入语句->中间语言->翻译结果
  - 优点：可以不考虑具体的翻译语言对，因此适合多语言之间的互译
  - 缺点：如何设计和定义中间语言的表达方式，如何维度都很难

- 基于语料库的翻译方法

  - 基于事例的
    - 方法：输入语句->与事例相似度比较->翻译结果
    - 优点：不要求源语言句子必须符号语法规定，不需要对源语言句子做深入分析
    - 缺点：两个不同句子间的相似性难以把握。难以处理事例库中没有记录的陌生语言现象，事例库大时检索效率低
  - 统计翻译
  - 神经网络机器翻译

![image-20220609204958029](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220609204958029.png)

# 3.统计机器翻译

![image-20220611150144126](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611150144126.png)

![image-20220609223840378](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220609223840378.png)

三个关键问题（S是源语句，T是目标语句）

- 估计语言模型概率 $p(T)$

  - n-gram问题

- 估计翻译概率 $p(S|T)$

  - ![image-20220609230131153](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220609230131153.png)

  - 目标语句长度为 $l$，源语句长度为 $m$ ，则二者之间有 $2^{l*m}$ 种对应关系（l*m求子集）。用来刻画这些对应关系 $A(S,T)$ 的模型叫做对位模型

    ![image-20220609230732612](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220609230732612.png)

    那如何计算 $P(S,A|T)$呢？

    ![image-20220609232912589](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220609232912589.png)

    ![image-20220609233628799](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220609233628799.png)

    

- 快速有效地搜索 $T$，设的 $p(T)p(S|T)$ 最大

## 3.1.IBM翻译模型1

![image-20220609234033601](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220609234033601.png)

根据上面的假设，我们得到

![image-20220609234057415](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220609234057415.png)

![image-20220609234253805](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220609234253805.png)

过程铁不考

![image-20220609234606796](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220609234606796.png)

### 流程

![image-20220609234444639](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220609234444639.png)

## 3.2.IBM翻译模型2

IBM翻译模型 1 中假设

![image-20220610110149500](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610110149500.png)

IBM翻译模型 2 中==根据概率公式==求得 $a_j$ 的概率，其他两个假设与上面模型一样

- ==假定概率 $P(a_j|a_1^{j-1},s_1^{j-1},m,T)$ 依赖于位置 j，对位关系 $a_j$ 和源语言句子程度 m 以及目标语言句子长度==

![image-20220610110235692](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610110235692.png)

![image-20220610111507150](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610111507150.png)

### 流程

![image-20220610111209930](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610111209930.png)

如何避免一个目标语言单词生成过多的源语言单词？

==对目标语言单词生成源语言单词的数目进行建模==

## 3.3.IBM翻译模型3

![image-20220610111927611](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610111927611.png)

- 源语言句子中所有与单词 t 对位的单词列表，称为 t 的一个片段，片段可能为空
- 一个目标语言句子 T 的多有片段的集合是一个随机变量，我们称为 T 的片段集，记作符号 R
  - T的第 i 个单词的片段记作 $R_i$
  - T的第 i 个单词片段中第 k 个源语言单词记作 $R_{ik}$

### 流程

==繁衍->空标记插入->词汇翻译->位变==

避免了一个位置的目标单词对应多个源语言单词的情况



![image-20220610115643757](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610115643757.png)

![image-20220610115847700](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610115847700.png)

![image-20220610120037917](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610120037917.png)

## 3.4.IBM4和5

![image-20220610120936273](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610120936273.png)

## 3.5.基于短语的翻译模型

从生成式模型转向判别式模型

![image-20220610215707945](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610215707945.png)

![image-20220610215733569](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610215733569.png)

### 3.5.1.基于最大熵的方法

目标：对一组特征，使得

- 统计模型在这一组上特征上的模型分布与样例中的经验分布完全一致
- 不对未知事件作任何假设，即保证模型尽可能均匀（==熵最大==）

基于词的翻译模型的问题：

- 很难处理词义消歧问题

  - 在基于词的模型中，处理词义消岐问题需要充分利用上下文信息，并对上下文信息进行有效建模

- 很难处理一对多，多对一和多对多问题

  - ![image-20220610222331860](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610222331860.png)

  

以短语为基本翻译单元

![image-20220610222404862](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610222404862.png)

![image-20220610222951521](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610222951521.png)

==短语指一个连续的词串，不一定是语言学中定义的短语==

![image-20220610224033864](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610224033864.png)

#### 3.5.1.1.短语划分模型

目标：将一个词序列如何划分成短语序列

方法：一般假设每种短语划分方式都是等概率的

#### 3.5.1.2.短语翻译模型

![image-20220610230618247](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610230618247.png)

##### 短语翻译规则抽取

![image-20220610230642558](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610230642558.png)

==对齐一致性==

- 有一个源短语（连续的词序列），目标短语（连续的词序列）

  - 如果源短语中的词在目标语句中有对应的词，则这个词一定在目标短语中
  - 如果目标短语中的词在源语句中有对应的词，则这个词一定在源短语中

  ![image-20220610230236551](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610230236551.png)

​		==就是源短语和目标短语所在的行和列上如果有黑块，一定在红色方框里才满足对齐一致性==

##### 估计短语翻译概率

![image-20220610232556359](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610232556359.png)

![image-20220610232705995](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610232705995.png)

按词来，然后算乘积

#### 3.5.1.3.短语调序模型

两种常用方法：

- 距离跳转模型
- 分类模型

##### 距离跳转模型

![image-20220610233345882](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610233345882.png)

d就是得到当前翻译短语时，要从源句子中跳转多远（看成指针位置，从前一个的源短语的末尾跳到当前的源语言的开始）

##### 分类模型（不知道用来干嘛的）

![image-20220610233811326](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610233811326.png)

#### 3.5.1.4.目标语言模型（肯定不考，谁tm记得住）

基于短语的判别式翻译模型

![image-20220610234350441](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610234350441.png)

8个特征如下所示

![image-20220610234359643](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220610234359643.png)

## 3.6.基于短语的翻译模型的解码算法

 解码算法取决于翻译模型。基于短语的翻译系统中，如下所示

![image-20220611150810497](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611150810497.png)

### 3.6.1.翻译候选生成

根据测试句子，搜索短语翻译规则表

### 3.6.2.代价估算

Score = 已翻译词所耗费的代价 + 未翻译部分的估算代价

- 已翻译：已翻译词的模型概率
- 未来的：最大概率或其他因素

### 3.6.3.柱搜索（beam search）

给定一个输入句子，生成对应的短语序列，每个短语对应一组翻译候选。

采用适当的剪枝策略

![image-20220611153229989](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611153229989.png)

![image-20220611153556477](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611153556477.png)

### 3.6.4.译文生成

从最后一个栈中找到概率最大的假设，根据其指向父亲节点的指针向前回溯，可以产生 n-best 翻译结果

## 3.7.基于短语模型的SMT系统实现（没啥东西）

## 3.8.基于层次化短语的翻译模型

- 基于短语的翻译模型能比较鲁棒地翻译==较短的子串==，短语长度扩展到3个以上的单词时，翻译的性能提高很少。==短语长度增大后，数据稀疏问题很严重==

- 很多情况下，简单的短语翻译模型==无法处理短语之间（尤其是长距离）的调序==
- ==无法处理非连续短语翻译==现象

基本思路：不破坏基于短语的翻译方法的优势，解决数据系稀疏，短语调序以及非连续短语翻译问题

![image-20220611162313667](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611162313667.png)

### 3.8.1.层次短语翻译规则学习

==定义层次化的短语由单词和子短语构成==

![image-20220611162626160](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611162626160.png)

![image-20220611162427089](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611162427089.png)

![image-20220611162851912](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611162851912.png)

基于层次化短语的翻译模型==首先利用层次化短语产生句子的局部翻译==，然后，像常规的基于短语的模型一样，==将这些局部的翻译顺序地连接起来，从而形成整个句子的翻译==

## 3.9.树翻译模型

问题：

- 基于层次短语的翻译模型只使用一个非终结符 X，==过于泛化==
- 基于层次短语的翻译模型==在处理长距离的短语调序问题时能力有限==

### 3.9.1.树到串的翻译模型

- 句法分析：将源语言句子分析成一棵句法结构树（短语结构树）
- 树到串的转换：递归地将源语言句子的句法结构树转换为目标语言句子

树到串翻译规则抽取->确定满足词语对齐的树节点->对每个满足词语对齐的树节点，我们可以抽取一条最小规则

- 优势：
  - 搜索空间小，解码效率高
  - 句法分析质量较高前提下，翻译效果不错
- 不足：
  - 强烈依赖于源语言句法分析的质量（分析错了，树就不对，后面更不对）
  - 利用源语言端句法结构精确匹配，数据稀疏严重
  - 没有使用任何目标语言句法知识，无法保证目标译文符合文法

### 3.9.2.树到树的翻译模型

- 句法分析：将源语言句子分析成一棵句法结构树（短语结构树）
- 树到树的转换：递归地将源语言句子的句法结构转换为目标语言句子的句法结构，拼接叶节点得到译文

- 解码算法：对于源语言句法结构树，自底往上或自顶往下考虑每个节点，为每个节点搜索能够匹配的树到树的翻译规则。所有节点匹配完毕，得到最佳译文

树到树翻译规则抽取（抽取满足词语对齐的）->确定满足词语对齐的树节点（为每对节点抽取规则）

- 优势：
  - 搜索空间小，解码效率高

- 不足：

  - 强烈依赖于源语言和目标语言句法分析的质量

  - 利用两端句法结构精确匹配，数据稀疏严重

  - 翻译质量差

### 3.9.3.串到树的翻译模型

串到树的转换：利用串到树的转换规则，==将源语言句子分析为一棵目标语言句法结构树==，拼接叶节点得到译文

过程：串到树翻译规则抽取（抽取满足词语对齐的串到树翻译规则）->确定满足词语对齐的树节点（目标语言句法树==节点所能到达的源语言子串==与该树==节点覆盖的目标语言子串==满足词语对齐约束）

- 优势：搜索空间大，保证译文符合文法（因为是满足译文句法树的），翻译质量高
- 不足：
  - 解码速度受限
  - 未使用源语言端句法知识，存在词义消岐问题

![image-20220611223849725](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611223849725.png)

## 3.10.系统融合

![image-20220611223930601](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611223930601.png)

### 3.10.1.句子级融合

针对同一个源句子，比较多个机器翻译系统的译文输出，将最优的翻译结果作为最终的一致翻译结果。

### 3.10.2.短语级系统融合

利用多个翻译系统的输出结果，重新抽取短语翻译规则集合，并利用新的短语翻译规则进行重新解码

### 3.10.3.词语级系统融合

首先将多个翻译系统的译文输出进行词语对齐，构建一个混淆网络，对混淆网络中的每个位置的候选词进行置信度估计，最后进行混淆网络解码。

![image-20220611225937081](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611225937081.png)

## 3.11.译文评估方法

常用的主观评测指标：流畅度，充分性，语义保持性

常用的客观评测指标：

- 句子错误率：译文与参考答案不完全相同的句子为错误句子。错误句子占全部译文的比率

### 3.11.1.BLEU评价方法

- 基本思想：将机器翻译产生的候选译文与人翻译的多个参考译文相比较，越接近，候选译文的正确率越高。

- 实现方法：统计==同时出现在系统译文和参考译文中的 n 元词的个数==，最后把匹配到的 n 元词数目除以==译文系统的 n 元词数目==，得到评测结果

  ![image-20220611231210433](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611231210433.png)

  修正的计算一元语法精确度的方法：

  ![image-20220611231448307](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611231448307.png)

  ![image-20220611231555680](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611231555680.png)

![image-20220611232454139](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611232454139.png)

- 分值范围：0-----1
  - 分值越高表示译文质量越好
  - 反之越差

### 3.11.2.NIST评测方法

BLEU对各种 n 元语法同现的比例具有相同的敏感性，但是实际上 n 值交大的统计单元出现的概率较低

基本思想：用 n-gram 同现概率的算术平均值取代几何平均值。另外，如果一个n元词在参考译文中出现的次数越少，表明它含信息量越大，那么就对该n元词赋予更高的权重。

![image-20220611233046133](C:\Users\nishiyu\AppData\Roaming\Typora\typora-user-images\image-20220611233046133.png)

评分值为不小于 0 的实数，0分表示译文质量最差

模型错误：概率最高的译文是不正确的

搜索错误：概率最高的译文是正确的，但搜索算法找不到
