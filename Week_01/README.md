学习笔记
===============

## 1. 时间复杂度的学习收获
分析算法时间复杂度的基本方法为：找出所有语句中语句频度最大的那条语句作为基本语
句，计算基本语句的频度得到问题规模n的某个函数f(n)， 取其数量级用符号“O”表示即可。类似的，空间复杂度为问题规模n的函数，指的是算法所需存储空间的量度，也用“O”表示。
时间复杂度和空间复杂度是基础知识，没有什么特殊的。在极客的课程中，主定理是之前没有接触过的。主定理用了渐进符号“O”表示了计算递归函数时间复杂度的方法。在课程中，解释了四种常用的主定理分析时间复杂度的方法：二分查找（O(logn)）、二叉树的遍历（O(n)）、有序矩阵二分查找（O(n)）和归并排序（O(nlogn)）。这四种十分常见，记住即可。

## 2. 数组，链表，跳表的学习收获
学习了数组，链表，跳表的基本概念，了解到空间换时间的理念，空间是时间是相互的。树，二叉树，二叉搜索树，树是链表的升维的一种结构方式，图是树的一种演变。 递归通过一层层来计算重复性工作。通过这几天的学习又重新对链表，树，二叉树，递归又有了深刻的认识，不过还需要进行继续学习，深耕了解更多的算法知识。

## 3. 队列、栈的学习收获
队列（Queue）：是限定只能在表的一端进行插入和另一端删除操作的线性表
栈（Stack）：是限定之能在表的一端进行插入和删除操作的线性表
队列和栈的规则
队列：先进先出
栈：先进后出
队列和栈的遍历数据速度
队列：基于地址指针进行遍历，而且可以从头部或者尾部进行遍历，但不能同时遍历，无需开辟空间，因为在遍历的过程中不影响数据结构，所以遍历速度要快
栈：只能从顶部取数据，也就是说最先进入栈底的，需要遍历整个栈才能取出来，遍历数据时需要微数据开辟临时空间，保持数据在遍历前的一致性

## 4. 双端队列deque，实现用add first或add last这套新的API改写Deque的代码
deque（也称为双端队列）是与队列类似的项的有序集合。它有两个端部，首部和尾部，并且项在集合中保持不变。deque 不同的地方是添加和删除项是非限制性的。可以在前面或后面添加新项。同样，可以从任一端移除现有项。在某种意义上，这种混合线性结构提供了单个数据结构中的栈和队列的所有能力。
用python实现用add first或add last这套新的API改写Deque的代码：
假定 deque 的尾部在列表中的位置为 0，我们为抽象数据类型 deque 的实现创建一个新类。在 removeFront 中，我们使用 pop 方法从列表中删除最后一个元素。 但是，在removeRear中，pop(0)方法必须删除列表的第一个元素。同样，我们需要在 addRear 中使用insert方法（第12行），因为 append 方法在列表的末尾添加一个新元素。
如下:
```
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFirst(self, item):
        self.items.append(item)

    def addLast(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
```

## 5. 分析Queue的源码
queue 模块提供适用于多线程编程的先进先出（FIFO）数据结构。因为它是线程安全的，所以多个线程很轻松地使用同一个实例。
### (1). 先从初始化的函数来看（分析写在代码注释内）：
```
class Queue:
    def __init__(self, maxsize=0):
        # 设置队列的最大容量
        self.maxsize = maxsize
        self._init(maxsize)

        # 线程锁，互斥变量
        self.mutex = threading.Lock()
        # 由锁衍生出三个条件变量
        self.not_empty = threading.Condition(self.mutex)
        self.not_full = threading.Condition(self.mutex)
        self.all_tasks_done = threading.Condition(self.mutex)

        self.unfinished_tasks = 0

    def _init(self, maxsize):
        # 初始化底层数据结构
        self.queue = deque()
```

从这初始化函数能得到哪些信息呢？首先，队列是可以设置其容量大小的，并且具体的底层存放元素的它使用了 collections.deque() 双端列表的数据结构，这使得能很方便的做先进先出操作。这里还特地抽象为_init 函数是为了方便其子类进行覆盖，允许子类使用其他结构来存放元素（比如优先队列使用了 list）。

然后就是线程锁 self.mutex ，对于底层数据结构 self.queue 的操作都要先获得这把锁；再往下是三个条件变量，这三个 Condition 都以 self.mutex 作为参数，也就是说它们共用一把锁；从这可以知道诸如with self.mutex与 with self.not_empty 等都是互斥的。

基于这些锁而做的一些简单的操作：
```
class Queue:
    ...
    def qsize(self):
        # 返回队列中的元素数
        with self.mutex:
            return self._qsize()

    def empty(self):
        # 队列是否为空
        with self.mutex:
            return not self._qsize()

    def full(self):
        # 队列是否已满
        with self.mutex:
            return 0 < self.maxsize <= self._qsize()

    def _qsize(self):
        return len(self.queue)
```

### (2). 作为队列，主要得完成入队与出队的操作，首先是入队操作：
```
class Queue:
    ...
    def put(self, item, block=True, timeout=None):
        with self.not_full: # 获取条件变量not_full
            if self.maxsize > 0:
                if not block:
                    if self._qsize() >= self.maxsize:
                        raise Full # 如果 block 是 False，并且队列已满，那么抛出 Full 异常
                elif timeout is None:
                    while self._qsize() >= self.maxsize:
                        self.not_full.wait() # 阻塞直到由剩余空间
                elif timeout < 0: # 不合格的参数值，抛出ValueError
                    raise ValueError("'timeout' must be a non-negative number")
                else:
                    endtime = time() + timeout  # 计算等待的结束时间
                    while self._qsize() >= self.maxsize:
                        remaining = endtime - time()
                        if remaining <= 0.0:
                            raise Full # 等待期间一直没空间，抛出 Full 异常
                        self.not_full.wait(remaining)
            self._put(item) # 往底层数据结构中加入一个元素
            self.unfinished_tasks += 1
            self.not_empty.notify()

    def _put(self, item):
        self.queue.append(item)
```

它要处理超时与队列剩余空间不足的情况，具体几种情况如下：
#### a. 如果 block 是 False，忽略timeout参数
若此时队列已满，则抛出 Full 异常；
若此时队列未满，则立即把元素保存到底层数据结构中；

#### b. 如果 block 是 True
若 timeout 是 None 时，那么put操作可能会阻塞，直到队列中有空闲的空间（默认）；
若 timeout 是非负数，则会阻塞相应时间直到队列中有剩余空间，在这个期间，如果队列中一直没有空间，抛出 Full 异常；
处理好参数逻辑后，，将元素保存到底层数据结构中，并递增unfinished_tasks，同时通知 not_empty ，唤醒在其中等待数据的线程。

### (3). 出队操作：
```
class Queue:
    ...
    def get(self, block=True, timeout=None):
        with self.not_empty:
            if not block:
                if not self._qsize():
                    raise Empty
            elif timeout is None:
                while not self._qsize():
                    self.not_empty.wait()
            elif timeout < 0:
                raise ValueError("'timeout' must be a non-negative number")
            else:
                endtime = time() + timeout
                while not self._qsize():
                    remaining = endtime - time()
                    if remaining <= 0.0:
                        raise Empty
                    self.not_empty.wait(remaining)
            item = self._get()
            self.not_full.notify()
            return item

    def _get(self):     
        return self.queue.popleft()
```

get() 操作是 put() 相反的操作，代码块也及其相似，get() 是从队列中移除最先插入的元素并将其返回。
#### a. 如果 block 是 False，忽略timeout参数
若此时队列没有元素，则抛出 Empty 异常；
若此时队列由元素，则立即把元素保存到底层数据结构中；

#### b. 如果 block 是 True
若 timeout 是 None 时，那么get操作可能会阻塞，直到队列中有元素（默认）；
若 timeout 是非负数，则会阻塞相应时间直到队列中有元素，在这个期间，如果队列中一直没有元素，则抛出 Empty 异常；
最后，通过 self.queue.popleft() 将最早放入队列的元素移除，并通知 not_full ，唤醒在其中等待数据的线程。

这里有个值得注意的地方，在 put() 操作中递增了 self.unfinished_tasks ，而 get() 中却没有递减，这是为什么？
这其实是为了留给用户一个消费元素的时间，get() 仅仅是获取元素，并不代表消费者线程处理的该元素，用户需要调用 task_done() 来通知队列该任务处理完成了：
```
class Queue:
    ...
    def task_done(self):
        with self.all_tasks_done:
            unfinished = self.unfinished_tasks - 1
            if unfinished <= 0:
                if unfinished < 0: # 也就是成功调用put()的次数小于调用task_done()的次数时，会抛出异常
                    raise ValueError('task_done() called too many times')
                self.all_tasks_done.notify_all() # 当unfinished为0时，会通知all_tasks_done
            self.unfinished_tasks = unfinished

    def join(self):
        with self.all_tasks_done:
            while self.unfinished_tasks: # 如果有未完成的任务，将调用wait()方法等待
                self.all_tasks_done.wait()
```
由于 task_done()使用方调用的，当 task_done() 次数大于 put() 次数时会抛出异常。
task_done() 操作的作用是唤醒正在阻塞的 join() 操作。join() 方法会一直阻塞，直到队列中所有的元素都被取出，并被处理了（和线程的join方法类似）。也就是说 join()方法必须配合task_done() 来使用才行。

## 6. 分析Priority Queue的源码
```
from heapq import heappush, heappop
class PriorityQueue(Queue):
    '''Variant of Queue that retrieves open entries in priority order (lowest first).
    Entries are typically tuples of the form:  (priority number, data).
    '''

    def _init(self, maxsize):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        heappush(self.queue, item)

    def _get(self):
        return heappop(self.queue)
```
优先队列使用了 heapq 模块的结构，也就是最小堆的结构。优先队列更为常用，队列中项目的处理顺序需要基于这些项目的特征。
heapq 是 python 的内置模块，源码位于 Lib/heapq.py ，该模块提供了基于堆的优先排序算法。
堆的逻辑结构就是完全二叉树，并且二叉树中父节点的值小于等于该节点的所有子节点的值。这种实现可以使用 heap[k] <= heap[2k+1] 并且 heap[k] <= heap[2k+2] （其中 k 为索引，从 0 开始计数）的形式体现，对于堆来说，最小元素即为根元素 heap[0]。
可以通过 list 对 heap 进行初始化，或者通过 api 中的 heapify 将已知的 list 转化为 heap 对象。
使用优先队列的时候，需要定义 __lt__ 比较方法，来定义它们之间如何比较大小。若元素的 priority 相同，依然使用先进先出的顺序。
例如：
```
import queue
class A:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __lt__(self, other):
        return self.priority < other.priority

q = queue.PriorityQueue()
q.put(A(1, 'a'))
q.put(A(0, 'b'))
q.put(A(1, 'c'))
print(q.get().value)  # 'b'
```

对于堆的操作，本人也分析了源码。
### (1). 添加新元素到堆中的 heappush() 函数：
```
def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)
```
把目标元素放置列表最后，然后进行上浮。尽管它命名叫 down ,但这个过程是上浮的过程，这个命名也让我困惑，后来我才知道它是因为元素的索引不断减小，所以命名 down 。下沉的过程它也就命名为 up 了。
```
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
```
一样是通过 newitem 不断与父节点比较。不一样的是这里缺少了元素交换的过程，而是计算出新元素最后所在的位置 pos 并进行的赋值。显然这是优化后的代码，减少了不断交换元素的冗余过程。

### (2). 输出堆顶元素的函数 heappop():
```
def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt
```
通过 heap.pop() 获得列表中的最后一个元素，然后替换为堆顶 heap[0] = lastelt ，再进行下沉：
```
def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # 左节点，默认替换左节点
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1  # 右节点
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos  # 当右节点比较小时，应交换的是右节点
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)
```
这边的代码将准备要下沉的元素视为新元素 newitem ，将其当前的位置 pos 视为空位置，由其子节点中的小者进行取代，反复如此，最后会在叶节点留出一个位置，这个位置放入 newitem ，再让新元素进行上浮。

### (3). 将无序数列重排成堆的 heapify() 函数：
```
def heapify(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)
```
这部分就和理论上的一致，从最后一个非叶节点 (n / 2) 到根节点为止，进行下沉。
