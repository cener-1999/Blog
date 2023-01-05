<p>只关注不会的，或者程序设计的更美原则。</p>
<blockquote>
<p>以三种结构组织知识：</p>
<ul>
<li>设计的道；</li>
<li>Grammar;</li>
<li>keyword概念；</li>
</ul>
</blockquote>
<h1 id="程序之道">程序之道</h1>
<h1 id="设计">设计</h1>
<p><strong>CS科学家的品质</strong>：</p>
<ul>
<li>数学家：形式语言描述理念</li>
<li>工程师：设计产品，组装系统，评估方案</li>
<li>自然科学家：观察复杂系统的行为，构建假说，并检验预测</li>
</ul>
<p><strong>问题求解</strong>： 发现问题、 创造性地思考解决方案以及清晰准确地表达解决方案的能力。</p>
<h1 id="概念">概念</h1>
<p><strong>Python解释器</strong>：Python 解释器是一个读取并执行 Python代码的程序。</p>
<p><strong>自然语言和形式语言</strong>：</p>
<pre class="codehilite"><code>- 自然语言：不是由设计而来，而是由演化而来，人说的语言
- 形式语言：为了特殊用途设计的语言
</code></pre>

<table>
<thead>
<tr>
<th>区别</th>
<th>自然语言</th>
<th>形式语言</th>
</tr>
</thead>
<tbody>
<tr>
<td>歧义</td>
<td>充满歧义</td>
<td>没有歧义</td>
</tr>
<tr>
<td>冗余</td>
<td>多</td>
<td>简洁</td>
</tr>
<tr>
<td>字面性</td>
<td>不严格</td>
<td>严格</td>
</tr>
</tbody>
</table>
<p>形式语言的密度远远大于自然语言</p>
<p><strong>语法规则：</strong>
- token
- structure</p>
<h1 id="grammar">Grammar</h1>
<p><code>**</code>表示指数运算</p>
<h1 id="变量表达式和语句">变量、表达式和语句</h1>
<p><strong>对变量的操纵是编程语言的强大之一，变量是指向一个值的名称</strong>。考虑一下汇编语言中的每个寄存器。</p>
<p>编程模式：</p>
<ul>
<li>交互式：直接和解释器交互</li>
<li>脚本模式：把代码保存在脚本文件中。以脚本模式(script mode)运行解释器</li>
</ul>
<h1 id="grammar_1">Grammar</h1>
<p>字符串操作：</p>
<ul>
<li>拼接： +</li>
<li>重复：*</li>
</ul>
<p>查对象类型：type()</p>
<h1 id="函数">函数</h1>
<ul>
<li>在交互模式中输入函数</li>
</ul>
<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205261643819.png" alt="image-20220526164329677" style="zoom:67%;" /></p>
<ul>
<li><strong>函数对象是一个值，可以赋值给变量，或者作为实参传递。</strong></li>
</ul>
<p>```python
  def right_justify(s):
      lens = 70-len(s)
      print(" "*70+s)</p>
<p>def do_twice(f,s):
      f(s)
      f(s)</p>
<p>do_twice(right_justify,"hello")
  ```</p>
<p><img alt="image-20220526171423806" src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205261714030.png" /></p>
<h1 id="概念_1">概念</h1>
<ul>
<li>函数的定义与执行</li>
</ul>
<p>函数的定义和执行与其他语句一样，不同的是执行后会<u>创建函数对象</u>。函数体中语句不立刻执行，而是被调用时才执行。定义必须在执行之前。</p>
<ul>
<li>执行流程：从上当下</li>
</ul>
<h1 id="设计_1">设计</h1>
<p>为什么要用函数：</p>
<ul>
<li>一次编写，多次使用</li>
<li>易读</li>
<li>易调试</li>
</ul>
<h1 id="grammar_2">Grammar</h1>
<ul>
<li>
<p><code>print</code>会自动换行，避免换行：在结尾打印一个空格<code>print(str+end=" ")</code></p>
</li>
<li>
<p>不带参数的<code>print</code>函数会结束当前行，开始下一行</p>
</li>
</ul>
<h1 id="案例研究接口设计">案例研究：接口设计</h1>
<ul>
<li>
<p>方法(method)与函数类似，但是语法不同：方法和对象关联</p>
</li>
<li>
<p>封装：把一段代码用函数包裹起来。增加可读性，可以多次使用。</p>
</li>
<li>
<p><strong>泛化</strong>：给函数添加参数的过程叫做泛化，因为它让函数更加通用</p>
</li>
</ul>
<h1 id="grammar_3">Grammar</h1>
<p><strong>关键词参数(keyword argument)</strong> </p>
<p>在调用函数时可以加上形参的名称，避免忘记形参具体是什么，或者搞乱顺序，让程序更加可读。</p>
<p><code>polygon(bob,n=7,length=100)</code></p>
<p><strong>接口设计</strong></p>
<p>函数的接口是如何使用它的概要说明：</p>
<ul>
<li>有哪些参数</li>
<li>函数功能</li>
<li>返回值</li>
</ul>
<p>接口要尽可能简洁</p>
<p><strong>重构(refactoring)</strong></p>
<p>重新组织程序，以改善接口，提高代码复用</p>
<blockquote>
<p>实际开发中，在工程还是时往往没有足够的信息去完美设计所有的接口。有时候，重构正意味着你在编程中掌握了新东西。</p>
</blockquote>
<h1 id="设计_2">设计</h1>
<p>开发计划是写程序过程。</p>
<p>这次说明的是“封装和泛化”，具体步骤是：</p>
<ol>
<li>开始写一些简单的有功能的代码，不需要定义函数</li>
<li>识别完整的部分，把那些代码进行封装</li>
<li>泛化这个函数，添加合适的形参</li>
<li>重复1~3</li>
<li>寻找利用重构来改善程序的机会</li>
</ol>
<p>这个方法可以让你一边开发一边设计</p>
<h1 id="grammar_4">Grammar</h1>
<p>文档字符串(docstring):用在函数开头解释其接口的字符串。</p>
<pre class="codehilite"><code class="language-python">def polyline( t, n, length, angle): 　 　
    &quot;&quot;&quot; Draws n line segments with the given length and 　 　 angle (in degrees) between them. t is a turtle. 　 　&quot;&quot;&quot; 　 　 
    for i in range( n): 　 　 　 　 
        t. fd( length) 　 　 　 　 
        t. lt( angle)
</code></pre>

<h1 id="设计_3">设计</h1>
<p>docstring包含的是别人需要知道的函数的基本信息:</p>
<ul>
<li>函数是做什么的</li>
<li>解释形参对函数的行为的影响效果</li>
<li>形参的类型</li>
</ul>
<p>编写docstring是接口设计的重要部分。一个设计良好的接口是很简单就可以解释清楚的，如果不能，那这个接口设计得不算好。</p>
<h1 id="设计_4">设计</h1>
<p><strong>调试</strong></p>
<p>前置条件：调用者应该提供正确的形参——调用者的职责</p>
<p>后置条件：函数一个符合预期效果，没有意外的副作用——函数的职责</p>
<p>前置，后置都清晰定义可以帮助调试。</p>
<h1 id="条件和递归">条件和递归</h1>
<h1 id="grammar_5">Grammar</h1>
<ul>
<li>
<p>向下整除：<code>//</code></p>
</li>
<li>
<p>逻辑操作符：<code>and</code>,<code>or</code>.<code>not</code></p>
</li>
<li>
<p>条件链：</p>
</li>
</ul>
<p><code>python
  if a&lt;b:
      ...
  elif a&gt;b:
      ...
  else:
      ...</code></p>
<p><code>elif</code>是else if的缩写</p>
<ul>
<li>键盘输入</li>
<li>python提供的内置函数<code>input</code>,用户按下回车键程序会恢复执行，input以字符串形式返回用户输入</li>
<li>可以接受提示输入信息作为参数</li>
<li>如果要的是<code>int</code>，可以用<code>int(a)</code>来转换</li>
</ul>
<h1 id="设计_5">设计</h1>
<p><strong>对调试有用的信息：</strong></p>
<ul>
<li>错误类型</li>
<li>发生错误的地方</li>
</ul>
<p>报错不一定都对</p>
<h1 id="grammar_6">Grammar</h1>
<p><code>print</code>拼接：</p>
<ul>
<li><code>+</code>：两者都是字符串时，否则</li>
</ul>
<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205270204178.png" alt="image-20220527020400063" style="zoom:67%;" /></p>
<ul>
<li><code>,</code>: 任何时候都可以</li>
</ul>
<p>画图模块<code>turtle</code></p>
<pre class="codehilite"><code class="language-python">import turtle #引入

# 新建对象
bob = turtle.Turtle()
# 速度
bob.delay = 0.01
# 前进像素
bob.fd(100)
# 后退
bob.bk(50)
# 左右旋转度
bob.rt(30)
bob.lt(60)
# 笔尖朝下——会画出痕迹 pendown
bob.pd()
# 朝上——只是移动  penup
bob.pu()

# 打印
turtle.mainloop()
</code></pre>

<p>~递归真的可以画出很多奇怪的图~</p>
<h1 id="有返回值的函数">有返回值的函数</h1>
<h1 id="设计_6">设计</h1>
<p><strong>增量开发</strong>：</p>
<ul>
<li>在写复杂函数时，调试变得困难。</li>
<li>增量开发的目标是每次只增加和测试一部分的代码，来避免长时间的调试过程</li>
<li>增量开发的关键点</li>
<li>以正确的，小的，可以运行的程序开始。每次只做小的修改，一错就应该知道哪错了</li>
<li>使用<em>临时变量</em>来保存中间结果，方便检查和显示</li>
<li>当程序完成是，可能会删掉一些手脚架代码或者把多个语句综合在一个复杂的表达式中。<strong>注意要兼顾代码的易读性</strong></li>
</ul>
<p><strong>手脚架代码(scaffolding)：</strong></p>
<ul>
<li>指在测试过程中的<code>print</code>语句</li>
<li>在确认函数编写正确时就要删掉</li>
<li>是构建程序的一部分，但不属于最终产品</li>
</ul>
<p><strong>坚持信念</strong></p>
<p>阅读程序时不跟踪程序执行流程，而是假定函数可以正确工作，并且返回正确结果。</p>
<p><strong>检查类型</strong></p>
<p>守卫(guardian)：用条件检查类型，以保护后面的代码，以免出现错误。</p>
<p><strong>调试：</strong></p>
<p>将一个大程序分解为-&gt;小函数，自然而然引入了调试的<em>检查点</em>。</p>
<p>如果一个函数不能正常工作，有三种可能性：</p>
<ol>
<li>函数获得的实参有问题，某个前置条件没有达到；</li>
</ol>
<blockquote>
<p>解决：</p>
<ul>
<li>在函数开始的地方加上<code>print</code>来显示实参的<u>值</u>和<u>类型</u>；</li>
<li>或者增加代码显式地检查前置条件；</li>
</ul>
</blockquote>
<ol>
<li>函数本身有问题，某个后置条件没有达到；</li>
</ol>
<blockquote>
<p>在<code>return</code>语句前加<code>print</code>语句，显示返回值</p>
</blockquote>
<ol>
<li>函数的返回值有问题，或者使用方式不准确</li>
</ol>
<blockquote>
<p>检查调用它的代码，看返回值是否被正确使用</p>
</blockquote>
<p>消减调试的时间的方法：<strong>二分调试</strong></p>
<p>把问题分成两半，找一个可以检查的中间结果，添加<code>print</code>语句。要是结果是错的，就是前半截错了，反之就是后半截。</p>
<h1 id="迭代">迭代</h1>
<h1 id="概念_2">概念</h1>
<ul>
<li>迭代：重复运行一段代码语句块的能力</li>
<li>重新赋值</li>
<li>更新：新值依赖旧值   <code>x=x+2</code></li>
</ul>
<h1 id="设计_7">设计</h1>
<p>对一个变量进行多次重新赋值，可能会让程序难以阅读和调试，谨慎多次重新赋值</p>
<h1 id="grammar_7">Grammar</h1>
<p><strong>比较两个float是否相等：</strong></p>
<p>使用内置函数<code>abs</code>来计算两数之差的绝对值</p>
<pre class="codehilite"><code class="language-python">if abs(y-x)&lt;epsilon:
    break
</code></pre>

<p><code>epsilon</code>的值是0.0000001</p>
<h1 id="字符串">字符串</h1>
<h1 id="grammar_8">Grammar</h1>
<p><strong>字符串：</strong></p>
<p>字符串是一个序列(sequence)，一个由其他值组成的有序集合。</p>
<ul>
<li>访问字符串的单独字符：使用index，从0开始。可以使用负数，表示倒着数。</li>
</ul>
<p><code>python
  fruit = "apple"
  letter = fruit[2]
  last_letter = fruit[-1]
  length = len(fruit)</code></p>
<ul>
<li>
<p><code>len</code> 获得长度</p>
</li>
<li>
<p>字符串切片(slice): <code>[n,m]</code>返回字符串从第n个字符到第m个字符，左闭右开。</p>
</li>
<li>
<p>省略n，从头开始</p>
</li>
<li>省略m，到结尾</li>
<li>
<p>可以接受第三个下标来指定“步长”</p>
<ul>
<li>步长=2取接下来第二个</li>
<li>步长=-1，表示相反的方向访问字符串，<code>[::-1]</code>表示逆序访问</li>
</ul>
</li>
<li>
<p><strong>字符串是不可变的</strong>，只能新建</p>
</li>
<li>
<p><code>upper()</code>，返回全部大写</p>
</li>
<li>
<p><code>find()</code>，查找子字符串，返回位置，没有则返回-1</p>
</li>
<li>
<p>可以有第二个实参，表示从哪开始找，第三个，到哪结束</p>
</li>
</ul>
<p><code>python
  word.find('ab')
  word.find('c',3,8)</code></p>
<p><img alt="image-20220527163006749" src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205271630792.png" /></p>
<ul>
<li>
<p>操作符<code>in</code>，返回布尔值，操作与两个字符串，若a是b的子串，返回True</p>
</li>
<li>
<p>字符串比较:</p>
</li>
<li>
<p><code>==</code>：是否相等</p>
</li>
<li>
<p><code>&gt;</code>,<code>&lt;</code>，比较字母顺序</p>
</li>
<li>
<p><code>replace(old, new[, count])</code></p>
</li>
</ul>
<p>返回字符串的副本，其中出现的所有子字符串 <em>old</em> 都将被替换为 <em>new</em>。 如果给出了可选参数 <em>count</em>，则只替换前 <em>count</em> 次出现。</p>
<ul>
<li><code>split</code></li>
</ul>
<p><img alt="" src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205271638610.png" /></p>
<ul>
<li><code>strip</code></li>
</ul>
<p><img alt="image-20220527163849457" src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205271638524.png" /></p>
<ul>
<li><code>count(sub[, start[,end]])</code></li>
</ul>
<p>返回子字符串 <em>sub</em> 在 [<em>start</em>, <em>end</em>] 范围内非重叠出现的次数。 可选参数 <em>start</em> 与 <em>end</em> 会被解读为切片表示法。</p>
<h1 id="设计_8">设计</h1>
<p>变量名称选得好，python会读起来很想英语</p>
<h1 id="案例分析文字游戏">案例分析：文字游戏</h1>
<h1 id="设计_9">设计</h1>
<ul>
<li>另一种程序开发计划：缩减问题规模，<u>回归成之前解决过的问题</u>。</li>
</ul>
<p>如果识别到当前问题是一个已经解决问题的特例，可以直接利用现有的解决方案。</p>
<ul>
<li>Program testing can be used to show the presence of bugs, but never to show their absence! </li>
</ul>
<h1 id="grammar_9">Grammar</h1>
<p><strong>文件读取：</strong></p>
<ul>
<li><code>open()</code> 接受文件名，返回文件对象。</li>
</ul>
<p><code>python
  fin = open("text.txt")
  for line in fin:
      word = line.strip()
      print(word)</code></p>
<ul>
<li>
<p><code>fin</code>是用来表示文件对象作为输入源时常用的名称。</p>
</li>
<li>
<p><strong>文件对象</strong>提供了几个方法来读内容：</p>
</li>
<li>
<p><code>readline</code>：从文件里读，遇到换行符后停下<code>\n</code></p>
</li>
<li><strong>文件对象会记住它读到了文件的那个位置</strong></li>
</ul>
<h1 id="列表">列表</h1>
<h1 id="grammar_10">Grammar</h1>
<p>列表(list)也是值的序列，与字符串相似。</p>
<ul>
<li>
<p>列表的值被称为元素(element)，可以是任何类型，<u>列表中的元素可以不是同一类型的</u>,列表可以嵌套。</p>
</li>
<li>
<p>创建列表的方式：用<code>[]</code></p>
</li>
</ul>
<p><code>python
  [1,2,3,4]
  a = ['apple',2.0,5,[10,20]]</code></p>
<ul>
<li>
<p>列表可以赋值给变量</p>
</li>
<li>
<p>列表是可变的</p>
</li>
<li>
<p>访问列表也是用下标索引。</p>
</li>
<li>
<p>-1：倒着访问</p>
</li>
<li>
<p><code>IndexError</code></p>
</li>
<li>
<p>列表操作</p>
</li>
<li>
<p><code>+</code>：拼接列表</p>
<p><code>python
a = [1,2,3]
b = [4,5,6]
c = a + b # c = [1,2,3,4,5,6]</code></p>
</li>
<li>
<p><code>*</code> 重复一个列表多次</p>
<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205271708342.png" alt="image-20220527170832300" style="zoom:67%;" /></p>
</li>
<li>
<p>切片：</p>
<ul>
<li>
<p>如果两个都省略，表示获得一个完整副本</p>
</li>
<li>
<p>如果切片在赋值语句左侧，则可以更新多个元素</p>
</li>
</ul>
<p><img alt="" src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205271711678.png" /></p>
</li>
<li>
<p>添加：</p>
<ul>
<li>
<p><code>append</code>在列表尾部添加元素</p>
</li>
<li>
<p><code>extend</code>接收一个列表做参数，把它有的元素附加进去。参数不被影响</p>
</li>
</ul>
<p><img alt="image-20220527171239849" src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205271712900.png" /></p>
</li>
<li>
<p>删除：</p>
<ul>
<li>
<p><code>pop()</code>，参数是index,返回删除的值，如果不提供参数，就删除最后</p>
</li>
<li>
<p><code>del()</code>，同上，但不返回删除的值</p>
</li>
<li>
<p>还能使用切片</p>
<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205271716510.png" alt="image-20220527171652464" style="zoom:67%;" /></p>
</li>
<li>
<p><code>remove()</code>，参数是要删除的元素</p>
</li>
</ul>
</li>
<li>
<p><code>sort</code>，排列</p>
</li>
<li>
<p><code>sort</code> 累加</p>
</li>
</ul>
<h1 id="grammar_11">Grammar</h1>
<p><strong>字符串和列表</strong></p>
<p>都是序列，但是不同。</p>
<p><strong>str-&gt;list：</strong></p>
<ul>
<li>用<code>list()</code>：函数把字符串拆解成单个字符。</li>
</ul>
<pre class="codehilite"><code class="language-python">s = &quot;apple&quot;
t = list(s) # t = ['a','p','p','l','e']
</code></pre>

<ul>
<li>用<code>split</code>把字符串拆解成单词，还能接受一个可选形参分隔符(delimiter)，用于指定用那个字符分隔单词</li>
</ul>
<pre class="codehilite"><code class="language-python">s = &quot;hello my dear friend&quot;
t = s.split()
# t = [&quot;hello&quot;,&quot;my&quot;,&quot;dear&quot;,&quot;friend&quot;]
s1 = &quot;hello-my-dear-friend&quot;
t2 = s.split('-')
</code></pre>

<p><strong>list -&gt; str:</strong></p>
<ul>
<li><code>join</code>是<code>split</code>的逆操作，接受字符串列表，拼接每个元素</li>
<li>用法：是字符串方法，所以必须在分隔符上调用它，并传入列表作为实参</li>
</ul>
<pre class="codehilite"><code class="language-python">t = [&quot;hello&quot;,&quot;my&quot;,&quot;dear&quot;,&quot;friend&quot;] 
delimiter = ' '
s = delimiter.join(t)
</code></pre>

<h1 id="grammar_12">Grammar</h1>
<p><strong>对象和值：</strong></p>
<ul>
<li>相等(equivalent)和相同(identical)。</li>
<li>对两个列表，相等是有相同元素，不相同是因为不是同一个对象</li>
</ul>
<p><strong>别名</strong></p>
<p>一个对象有多个引用，并且引用有不同的名称，则这个对象有别名</p>
<h1 id="设计_10">设计</h1>
<p>在处理可变对象时，避免使用别名会更安全。而对于字符串这样的不可变对象，使用别名不会有问题。</p>
<h1 id="grammar_13">Grammar</h1>
<ul>
<li>使用列表来作为参数，如果函数修改了列表，则列表中的数据会切实改变。</li>
<li>区分修改列表操作/新建列表操作很重要</li>
<li><code>append</code>是修改</li>
<li><code>+</code>是新建，切片也是新建</li>
</ul>
<h1 id="设计_11">设计</h1>
<p>对列表（或者其他可变对象）的不慎使用，可能会导致长时间的调试。</p>
<p><strong>常见陷阱：</strong></p>
<ol>
<li>大部分列表方法都是修改参数，并返回None。这和字符串方法正好相反，字符串方法都是新建一个字符串，然后保留原始字符串。</li>
</ol>
<blockquote>
<p>解决：在使用列表方法之前，仔细阅读文档，并在交换模式中测试</p>
</blockquote>
<ol>
<li>
<p>选择一种风格，并坚持不变。同样的事情有太多可用的方法，尽量使用同一种。</p>
</li>
<li>
<p>通过复制来避免别名</p>
</li>
</ol>
<pre class="codehilite"><code class="language-python">t = [2,3,1]
t1 = t[:]
t1.sort()
</code></pre>

<h1 id="字典">字典</h1>
<h1 id="grammar_14">Grammar</h1>
<p><strong>字典</strong></p>
<ul>
<li>
<p>键值对，映射关系</p>
</li>
<li>
<p>新建：<code>dict()</code></p>
</li>
<li>
<p>添加：</p>
</li>
</ul>
<p><code>python
  a = dict()
  a['one'] = 'apple'
  b = {'one':'a','two':'b','three':'c'}
  flag = 'one' in a # True</code></p>
<ul>
<li>
<p><strong>字典是无序的</strong>，与输入顺序无关。</p>
</li>
<li>
<p>通过key值来查找</p>
</li>
<li>
<p><code>in</code>，是否是key，不包括value</p>
</li>
<li>
<p><code>values</code>，返回一个值的集合</p>
</li>
</ul>
<p><code>python
  # 用 in ,values 结合
  vals = a.values()
  'a' in vals # True</code></p>
<ul>
<li>遍历字典：要按顺序遍历所有键，可以使用内置函数<code>sorted</code></li>
</ul>
<p><code>python
  for key in sorted(h):</code></p>
<ul>
<li>反向查找：v -&gt; k  没有简单语法，只能搜索</li>
</ul>
<p><code>python
  def reverse_lookup(d,v):
      for key in d:
          if d[k] == v:
              return k
          raise LookupError()</code></p>
<ul>
<li>
<p><code>raise</code>语句会产生一个异常。</p>
</li>
<li>
<p><code>LookupError</code>是一个内置异常，通常表示查找失败</p>
</li>
<li>
<p>反向查找远远慢于正向查找，对性能由影响</p>
</li>
</ul>
<p><code>in</code> 操作符的搜索算法对list和dict使用不同的算法实现。</p>
<ul>
<li>list：顺序搜索，当列表变长时，搜索时间也会变长；</li>
<li>dict：使用散列表，不论字典有多少项，<code>in</code>操作符花费的时间差不多。</li>
</ul>
<h1 id="grammar_15">Grammar</h1>
<p><u>字典是通过散列表的方式实现的，所以键必须是可散列的。</u>可变类型是不可散列的。</p>
<p>散列是一个函数，接受值并返回一个整数。</p>
<p>字典使用这些被称为散列值的整数来保存和查找键值对。</p>
<h1 id="设计_12">设计</h1>
<p><strong>备忘：</strong></p>
<p>将之前计算的值保存起来，以便后面使用的方法称为备忘(memo)</p>
<h1 id="grammar_16">Grammar</h1>
<p>给全局变量赋值：</p>
<ul>
<li>如果指向不可变的值，要先声明这个全局变量。</li>
</ul>
<pre class="codehilite"><code class="language-python">been_called = False

def ex2():
    global been_called
    been_called = True
</code></pre>

<p><code>global</code>语句告诉编译器，been_called是指全局变量，而不是新建一个局部变量。</p>
<ul>
<li>如果全局变量指向可变的值，不用声明就可以修改。但是如果是要给全局变量重新赋值，那还是要声明</li>
</ul>
<pre class="codehilite"><code class="language-python">known = {0:0,1:1}

def ex3():
    known[2] = 1

def ex4():
    known = dict()
</code></pre>

<p>本质还是：是修改还是新建</p>
<h1 id="设计_13">设计</h1>
<p>如果全局变量用多了，可能代码会难以调试</p>
<h1 id="设计_14">设计</h1>
<p><strong>调试大数据集</strong></p>
<ul>
<li>缩小输入：减小数据集的尺寸，使用最小样本，然后在逐渐增大。</li>
<li>检查概要信息和类型：不是print整个数据集，而是概要信息，比如数量，和，类型。</li>
<li>编写自检查逻辑：健全检查，一致性检查</li>
<li>格式化输出：搭建手脚架代码，以人可读的方式来输出</li>
</ul>
<h1 id="元组">元组</h1>
<h1 id="grammar_17">Grammar</h1>
<p><code>tuple</code></p>
<ul>
<li>
<p>元组是不可变的</p>
</li>
<li>
<p>元素的值可以是任何类型</p>
</li>
<li>
<p>一般用<code>()</code>包围</p>
</li>
<li>
<p>新建</p>
</li>
</ul>
<p><code>python
  t = 'a',
  t1 = 'a','b','c'
  t2 = tuple("hello")</code></p>
<ul>
<li>只有一个元素的元组，要加<code>,</code></li>
<li>
<p>可以用内置函数<code>tuple</code></p>
<ul>
<li>没有参数时，新建一个空元组</li>
<li>参数时序列时（字符串，列表，元组），结果是包含序列元素的元组</li>
</ul>
</li>
<li>
<p>读取：也用下标，切片</p>
</li>
<li>
<p>关系运算符适用于元组和其他序列，python从比较每个序列的第一个元素开始。</p>
</li>
</ul>
<h1 id="grammar_18">Grammar</h1>
<p><strong>元组赋值</strong></p>
<pre class="codehilite"><code class="language-python"># 一般的交换
tmp = a
a = b
b = tmp

# 更优雅的交换
a,b = b,a

# 很漂亮的拆分
addr = &quot;cen@qq.com&quot;
uname,domain = addr.split('@')
</code></pre>

<p>用做返回值</p>
<pre class="codehilite"><code class="language-python">t =divmod(7,3) # t = 2,1 商和余数
</code></pre>

<p>在循环中赋值</p>
<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205290040284.png" alt="image-20220529004005230" style="zoom:67%;" /></p>
<h1 id="grammar_19">Grammar</h1>
<p><strong>可变长参数元组</strong></p>
<p>函数可以接受不定个数的参数。以<code>*</code>开头的参数名会<strong>收集</strong>所有的参数到一个元组上。</p>
<pre class="codehilite"><code class="language-python">def printall(*args):
    print(args)
</code></pre>

<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205290019175.png" alt="image-20220529001912706" style="zoom:67%;" /></p>
<p><strong>分散</strong></p>
<p>搜集的反面是分散(scatter)。如果有一个序列的值，想将它们作为可变长参数传入函数中，可以使用<code>*</code>操作符。</p>
<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205290021239.png" alt="image-20220529002138181" style="zoom:67%;" /></p>
<pre class="codehilite"><code class="language-python">def sumall(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

# 成功
tmp = 1,2,3,4,5,6
print(sumall(*tmp))

# 报错: TypeError:unsupported operand types for +:'int' and 'tuple'
tmp = (1,2,3,4,5,6)
print(sumall(tmp))

# 报错: TypeError:unsupported operand types for +:'int' and 'tuple'
tmp = (1,2,3,4,5,6)
print(sumall(*tmp))
</code></pre>

<h1 id="grammar_20">Grammar</h1>
<p><code>zip()</code> “拉链”</p>
<ul>
<li>
<p>接收两个或者多个序列，并返回一个元组列表。</p>
</li>
<li>
<p>每个元组包含来自每个序列的一个元素。</p>
</li>
<li>
<p><strong>结果是一个zip对象</strong></p>
</li>
<li>
<p><code>zip</code>对象是一个迭代器</p>
<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205290030784.png" alt="image-20220529003001720" style="zoom:67%;" /></p>
</li>
<li>
<p>它知道如何遍历每个<em>元素对</em>，使用<code>zip</code>最常用的方法是for</p>
<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205290032647.png" alt="image-20220529003207584" style="zoom:67%;" /></p>
</li>
<li>
<p>不能用index来选择对象</p>
</li>
<li>
<p>可以给<code>zip</code>对象制作一个列表<code>list</code></p>
<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205290034953.png" alt="image-20220529003353842" style="zoom:67%;" /></p>
</li>
<li>
<p>序列长度不同，按照木桶原理</p>
</li>
</ul>
<h1 id="grammar_21">Grammar</h1>
<ul>
<li>同时组合使用<code>zip</code>,<code>for</code>预计元组赋值，可以同时遍历多个序列</li>
</ul>
<pre class="codehilite"><code class="language-python">def has_match(t1,t2):
    for x,y in zip(t1,t2):
        if x == y:
            return True
        return False
</code></pre>

<ul>
<li>同时遍历元素和它们的下标，可以使用<code>enumerate</code></li>
<li><code>enumerate</code>的结果是一个枚举对象，这个对象迭代一个对序列</li>
</ul>
<pre class="codehilite"><code class="language-python">def index, element in enumerate('abc'):
    print(index,element)
</code></pre>

<h1 id="grammar_22">Grammar</h1>
<p><strong>dict -&gt; tuple</strong> : <code>items</code></p>
<ul>
<li>返回一个元组的序列，每个元组是一个键值对</li>
</ul>
<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205290050710.png" alt="image-20220529005011651" style="zoom:67%;" /></p>
<ul>
<li>结果是一个<code>dict_item</code>对象，是一个迭代器</li>
</ul>
<p><strong>tuple -&gt; dict</strong></p>
<ul>
<li>直接<code>dict</code></li>
</ul>
<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205290052398.png" alt="image-20220529005203347" style="zoom:67%;" /></p>
<ul>
<li>组合使用<code>dict</code> 和 <code>zip</code> 可以得到一个简洁的创建字典的方法`</li>
</ul>
<p><img src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202205290053797.png" style="zoom:67%;" /></p>
<ul>
<li>字典方法<code>update</code>，接收一个元组列表，并将它们作为键值对添加到一个<em>已有</em>的字典中</li>
</ul>
<p><strong>使用元组作为字典的键是很常见的</strong></p>
<pre class="codehilite"><code class="language-python">d[last,first] = number

for last, first in d:
    print(first, last, d[last,first])
</code></pre>

<h1 id="设计_15">设计</h1>
<p><strong>如何选择使用什么序列：<code>str</code> ,<code>tuple</code>,<code>list</code>,<code>dict</code>  ?</strong></p>
<ul>
<li><code>str</code> 限制最多：必须是字符，不能改变</li>
<li><code>list</code>可以改变</li>
<li><code>tuple</code>优先的情况：</li>
<li>返回语句，因为创建元组简单</li>
<li>字典的键，因为不可变</li>
<li>传入参数</li>
</ul>