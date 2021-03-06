学习笔记
===============

## 学习总结 
本周的字典树对我来说，是一个新概念。

Trie树，即字典树，又称单词查找树或键树，是一种树形结构，是一种哈希树的变种。典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。它的优点是：最大限度地减少无谓的字符串比较，查询效率比哈希表高。
　　Trie的核心思想是空间换时间。利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。

它有3个基本性质：
- 根节点不包含字符，除根节点外每一个节点都只包含一个字符。
- 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串。
- 每个节点的所有子节点包含的字符都不相同。

字典树，又称 Trie 树，是一种树形结构。典型应用是用于统计，排序和保存大量的字符串（但不仅限于字符串）。主要思想是利用字符串的公共前缀来节约存储空间。 

在实际运用中，比如我们要储存大量的单词在一个文本中，而且还要查找某个单词是否存在，如果存在，请输出出现了多少次。考虑到有大量的单词而且还要询问出现了多少次，考虑到无法用字符串直接存储并进行遍历，所以就有了字典树这种高级数据结构。字典树的主要思想是利用字符串的公共前缀来节约存储空间。

如上图所示，从根节点开始到每一个红色标记的结点都是一个单词，上图中储存的字符串有"abc"、"abcd" 、"abd" 、"b"、"bcd"、"efg"、"hi"。当有大量单词是就可以利用字典树这种高级数据结构就可以节约存储空间。

字典树的实现方式有两种，1：通过结构体指针来实现，2：通过数组来实现

两种实现方式主要区别在于，数组实现的字典树比结构体指针实现的字典更节省内存，只要不是特别卡内存，笔者建议用结构体指针实现，比较好写也易于理解，要是MLE了，就改为数组实现吧。考虑到结构体指针实现的字典树比较好写，下面笔者就详细讲解一下字典树的结构体指针实现。

既然字典树是利用公共前缀的思想来节约存储空间，那么字典树的建立就是将单词一个一个插入到字典树中，每次插入一个单词就看字典树中有没有和当前要插入的单词的公共前缀。通俗一点来讲：就是将单词也就是字符串分为一个一个的字符，按照从根节点开始查看，根结点不存储任何字符，然后将字符串中的字符从第一个开始一个一个遍历，看字典树中有没有相同的字符。除根结点外，第一个字符对应第一层，第二个字符对应第二层，如果在查看的时候有就不用进行任何操作，因为本身字典树就是用来存储公共前缀的，如果没有这个字符就把这个字符插入到当前结点的子结点中。比如字典树中本来只存储了"ab"这个字符串，现在输入一个"abc",开始遍历会依次查找到'a'、'b',但是没有查找到'c',所以要在'b'的子结点上插入'c',大致原理就是这样。

字典树的具体实现，由于我们要记录字符串中字符的先后顺序和字符串出现的次数，所以字典树用结构体指针实现。由于一共有26个字符所以每一个结点都有26个结构体指针，通过指针是否为空来判断字符是否存在，还要记录字符串出现的次数，所以还需要一个变量。其实结构体指针的微妙之处在于，其实字典树中存储的其实不是字符而是指针，只是记录了前驱和后继的关系，而把字符通过处理转换成了对应结构体指针数组的下标，通过判断结构体指针数组某个下标所对应的指针是否为空来判断所对应的字符是否存在。为了叙述方便，下面出现的结点为不是真正的结点，结点字符'c'表示的是结点所对应的结构体指针数组中'c'。就拿上图中可以看见的字符串"abc"在一棵空字典树的操作来理解，对于字符串的第一个字符'a'，判断根结点的子结点'a'-'a'所对应数组下标的指针是否为空，当前为空，所以新建一个结点，作为根结点的子结点，接下来插入'b'、'c'同理，由于字符遍历完了，所以以当前结点字符'c'结尾的数字记录+1代表这个单词出现，如果接下来要插入"abcd",也从根结点开始遍历，发现根结点的子结点中有'a',就遍历下一个字符'b',结果字典树中的那个结点'a'所对应的子结点也有'b',所以继续遍历下一个字符，直到遍历完字符’c'，接下来遍历字符'd',由于字符'c'没有字符为'c'的子结点，所以新建一个结点插入字符'c'，最后'c'字符所对应结点的记录单词的数据+1。查找的时候一样，从根结点开始遍历，直到结尾字符，看结尾字符所对应的数据是否为0来判断字符串是否存在。