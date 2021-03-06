学习笔记
===============

## 学习总结 
本周学习了动态规划算法。
动态规划作为算法中比较难的部分，往往让人难以理解。
经过了本周的学习，对于动态规划算法有了切实的体会与提高。

### 1. 动态规划算法
动态规划（Dynamic programming，简称DP），是大家都觉得比较难以掌握的算法。为了应付面试，我们经常会背诵一下斐波那楔数列或者背包问题的源码，其实，只要理解了思想，掌握基本的模型，然后再来点写代码的套路，动态规划并没有那么难。

#### 思想与性质
动态规划最重要的是掌握他的思想，动态规划的核心思想是把原问题分解成子问题进行求解，也就是分治的思想。
那么什么问题适合用动态规划呢？我们通过一个现实中的例子，来理解这个问题。大家可能在公司里面都有一定的组织架构，可能有高级经理、经理、总监、组长然后才是小开发，今天我们通过这个例子，来讲讲什么问题适合使用动态规划。又到了一年一度的考核季，公司要挑选出三个最优秀的员工。一般高级经理会跟手下的经理说，你去把你们那边最优秀的3个人报给我，经理又跟总监说你把你们那边最优秀的人报给我，经理又跟组长说，你把你们组最优秀的三个人报给我，这个其实就动态规划的思想！

- 首先，是重叠子问题。不同的问题，可能都要求1个相同问题的解。假如A经理想知道他下面最优秀的人是谁，他必须知道X,Y,Z,O,P组最优秀的人是谁， 甲总监想知道自己下面最优秀的人是谁，也要去知道X,Y,Z组里面最优秀的人是谁？这就有问题重叠了，两个人都需要了解X,Y,Z三个小组最优秀的人。

- 其次是最优子结构，最优解肯定是有最优的子解转移推导而来，子解必定也是子问题的最优解。甲总监下面最优秀的3个人肯定是从X,Y,Z提交上来的3份名单中选择最优秀的三个人。例如Q哥是X组长下面的第5名，那么他肯定不可能是甲总监下面最优秀的三个。

- 第三是无后效性，这个问题可能比较难理解，也就是求出来的子问题并不会因为后面求出来的改变。我们可以理解为，X组长挑选出三个人，即便到了高级经理选出大部门最优秀的三个人，对于X组来说，最优秀的还是这3个人，不会发生改变。

#### 过程
动态规划问题，大致可以通过以下四部进行解决。

- 划分状态，即划分子问题，例如上面的例子，我们可以认为每个组下面、每个部门、每个中心下面最优秀的3个人，都是全公司最优秀的3个人的子问题

- 状态表示，即如何让计算机理解子问题。上述例子，我们可以实用f[i][3]表示第i个人，他手下最优秀的3个人是谁。

- 状态转移，即父问题是如何由子问题推导出来的。上述例子，每个人大Leader下面最优秀的人等于他下面的小Leader中最优秀的人中最优秀的几个。

- 确定边界，确定初始状态是什么？最小的子问题？最终状态又是什么。例如上述问题，最小的子问题就是每个小组长下面最优秀的人，最终状态是整个企业，初始状态为每个领导下面都没有最优名单，但是小组长下面拥有每个人的评分。

#### 经典模型

##### 线性模型

最经典的问题就是斐波那楔数列的问题，每个数的值都是一个状态，可以用F[i]表示表示第i个数的值是多少。每个数都是由F[i-1]+F[i-2]转移而来。

另外一个经典的问题就是最长上升自序列（LIS），有一串序列，要求找出它的一串子序列，这串子序列可以不连续，但必须满足它是严格的单调递増的且为最长的。把这个长度输出。示例：1 7 3 5 9 4 8 结果为4。

我们非常容易表示他的状态，我们用f[i]表示以第i个数结尾的，最大的上升自序列是多少？那么它是怎么转移的呢？非常容易想到肯定是从左边的的数转移而来，能转移的数满足什么条件呢？肯定是比a[i]更小的。

线性模式还可以拓展成二维问题，例如背包问题，用f[i][j]表示前i个物品，凑成大小为j的背包，最大的价值是多少。

这类问题非常的多，但是思路都是这样，无非就是从左往右，从上到下，从低维到高维进行转移。

##### 区间模型

对于每个问题，都是由子区间推导过来的，我们称之为区间模型，下面是一个例子。

我们有一个连续的序列，每个序列上面都是一个数字c[i]，每次我们都能够消灭一个连续的回文子序列，消灭之后左右会合并，成为一个新序列，问最少需要多少次才能够把整个序列消灭掉。回文就是从左到有从右到左读到的序列都是一样的。题目比较抽象，我们通过一些例子来说明这个问题吧？例如一开始的序列是1 4 4 2 3 2 1，那么我们最少需要2次，先消灭掉4 4 ， 然后再消灭调1 2 3 2 1.第二个例子是 1 2 3 4 5 5 3 1，我们先消灭掉2 然后再消灭掉4， 最后消灭 1 3 5 5 3 1， 需要3次。

我们经常用f[i][j]来表示消灭i,j区间需要的代价，文末有链接详细叙述这个问题，大家感兴趣的可以看一看。

##### 树状模型

我们在数据结构树上面进行最求最优解、最大值等问题，上述我们讲的这个绩效考核就是一个树状模型，具体不再累叙。

实现的套路

我们实现动态规划算法，常用的是2个实现套路，一个是自底向上，另外一个是自顶向下。无论是何种方式，我们都要明确动态规划的过程，把状态表示、状态转移、边界都考虑好。

- 1.自底向上，简单来说就是根据初始状态，逐步推导到最终状态，而这个转移的过程，必定是一个拓扑序。如何理解这个拓扑序问题呢，甲总监下面有X,Y,Z两个小组，甲总监不会一拿到X组最优秀的三个人，就立马去跟A经理汇报，而是要等到Y,Z小组也选出来之后，也就是自己下面所有子问题都解决了，才会继续向汇报。如果推导的过程不是一个拓扑序，那么要么得到错误的结果，要么算法就要退化。

自底向上一般用来解决什么问题呢？那就是可以轻松确定拓扑序的问题，例如线性模型，都是从左往右进行转移，区间模型，一般都是从小区间推导到大区间。自底向上的一个经典实现是斐波那楔数列的递推实现，即F[i] = F[i - 1] + F[i - 2] 。

- 2.自顶向下，也就是从最终状态出发，如果遇到一个子问题还未求解，那么就先求解子问题。如果子问题已经求解，那么直接使用子问题的解，所以自顶向下动态规划又有一个形象生动的名字，叫做记忆化搜索，一般我们采用递归的方式进行求解。

自顶向下，我们一般用在树上面，因为我们根据父亲结点，很容易找到所有的子问题，也就是所有的子结点，而自底向上的话，我们要去统计这个结点的所有兄弟结点是否已经实现。会稍微复杂一点，而且比较难理解。

无论是自顶向下还是自底向上，都只是代码实现的一种套路，随便你采用哪一个，都是可以解的，只是看你的选择而已。

---
动态规划，更多的还是要多练习，题目很多，但万变不离其宗，还是要多多练习。后面还会分享出更多动态规划面试算法真题，大家有兴趣的话可以关注。谢谢大家。