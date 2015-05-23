# 7 Useful Git Tips for Beginners.md
写给Git初学者的7个建议
当我刚刚开始使用 Git 的版本控制时，我根本不确定我付出那么多时间是不是会得到回报。
Branch、Stage、Stash，这些 Git 名词对我来说都非常陌生。而今天的我已不能想象生活没有 Git 会变成什么样。Git 不仅提供了我非常需要的版本控制功能，还让我变成一个更优秀的程序员。
这里有一系列可以帮助你的小贴士，可以让 Git 成为你开发工作中非常重要的一部分。

## 第一条：花时间去学习 Git 的基本操作
学习 Git 的基本操作并不是要求你把整个 Git 文档从头到尾读完（但如果这就是你的方式，我也不会反对）。
Git 里面有太多的教育内容，我很确定里面一定有对你胃口的最佳学习方式。
写给Git初学者的7个建议
看一下以下这些 Git 学习资源吧：
怎么快速开始使用 Git
试试 Git - 15 分钟的 Git 交互教程
提示和技巧（Ry 的 Git 教学）是常见 Git 功能的实践教程
Git 简单指南
Git Ready 是一个收藏有许多简单而简短的 Git 提示的网站
Git 作弊码
Git Tower 学习区是一个在我的网站上的 Git 学习资源列表
Git 官方教程
Training: Git Basics (视频)是 YouTube 上的一个视频列表
Pro Git 一本让你深入了解 Git 的在线书籍

## 第二条：从简单的 Git 工作流开始
少即是多。
常常的，Git 会和一个复杂的工作流联系起来。不过我可以这么说：你还暂时不需要为了 Git 的诸多好处，而一下子变成 Git 大师。
Git 的工作流是可以非常简单的 —- 而且在许多情况下你需要的就是这么简单。你当然可以用 multiple remote repositories、issue pull request、rebase changes 等等，但是你不想用这些的话完全可以不用。
从简单的工作流入手也会使日后添加复杂性或者使用 Git 高级功能变得简单。当你需要使用这些功能的时候，Git 已经准备好了。
这里有一些不同的 Git 工作流的例子，你可以从他们的想法中得到启发
设计者的 Git 工作流
Markus Prinz 的 Git 工作流
Yehuda Katz 的普通 Git 工作流
Agile 团队的 Git 工作流
总的来说：不要因为觉得 Git 什么都要学就压力很大，你完全可以从今天开始使用 Git。

## 第三条：不要再害怕犯错误
Git 最出色的一点是：它几乎是 100% 易上手误操作的。
记住以下几点会让你晚上睡得更香：
Git 基本上不删除数据。即使是那些看起来是删除数据的操作，实际上是为了让你更快的撤销删除，而在向系统添加数据。
Git 基本可以撤销所有操作。我鼓励你更多的实验和探索你的想法，因为这就是使用版本控制系统系统的最主要的好处之一。
你团队的每一个成员都在他／她的计算机中有各自的副本。本质上这更像是整个版本控制项目中的冗余备份（包括包括整个历史纪录），你捅了大娄子而且还没办法还原这种情况是极其少见的。

## 第四条：理解分支概念
在 Git 里面，分支这个概念是你一开始能学到的最有用的东西了。分支允许你隔离开发你的项目，而要想成为一个高效的 Git 用户，这是非常关键的一点。
一开始这听起来好像不是什么大事，但一旦你完全的理解了分支概念，你会开始想没有这个你怎么活下去。
尽管其他的版本控制系统也会使用分支概念，Git 是第一个实现它，并让它变的好用的系统。
写给Git初学者的7个建议
这里有一些有助你了解 Git 分支概念的资源：
LearnGitBranching!是一个 Git 分支的交互式教程
Git 基本分支和合并
分支术是一个 Git 分支和合并的简短介绍
Git 分支是一个很多绘图的 Git 教程
一个成熟的 Git 分支模型

## 第五条：学习暂存区
当你的提交里面只包含一些相关的变化时，版本控制会变的非常有用[b]，它保证了你的提交可以被没有任何副作用的回滚，经常提交的习惯也可以让你的同事更好的了解你的进度。
Git 有个功能叫暂存区让这一切都变为可能
学习使用暂存区，并爱上它，因为这是 Git 里面最重要最独立的一个模块。
为什么暂存区那么有用
用暂存区的好处在哪 —- 一个有关 Git 暂存区的讨论主题
啊哈！学习 Git 的那些时候 —- 一篇博客文章
Git 上有关暂存区的简短教程

## 第六条：用 Git 图形界面
尽管使用图形界面绝对不会是一个要求，但我还是高度推荐使用。
使用图形界面让大多数操作都变得简单，让你在项目开始时便占尽优势。
不管怎么说，使用 Git 不应该只是记住各种命令和参数，而是改进你的编程工作流。如果图形界面可以做到这一点的话，没有理由让简单的事变的困难嘛。

看一下这些 Git 界面吧：
Tortoise Git - Windows 平台下的开源 Git 图形界面
GitX (L) - Mac OS X 下的开源 Git 客户端
SourceTree - Windows 和 Mac 下的免费 Git 或 Mecurial 界面
git-cola - 一款开源 Git 界面
Tower - 我们公司为 Mac 用户所出的 Git 界面
使用图形界面并不能减轻你学习 Git 基础的负担，不过一旦你快乐的征服了 Git，使用这些工具会让你的生活变得更轻松。

## 第七条：对自己承诺你会用 Git
使用一个新工具一开始会让人非常头疼，走过这条学习曲线的方法只有一个：继续走下去。
做一个充分的承诺，不要回头。在你平常的工作流里引入 Git 很快就会被证明这是你近期做的最大的，最有意义的决定。
避免这种情况：「我会在这个项目里使用 Git，但其他项目就再说了。」至少一开始不要这样。
充分承诺的这种心态会让你有更多的机会去练习，让事情变得更加简单，因为你知道你现在这个项目用了版本控制系统。而更重要的是，让 Git 成为你的编程习惯。
未来不久，你就会看到只有那么一些情况不需要用到 Git，
对自己做一个 100% 的承诺，作为 Git 征服之路的开始。
翻译： 伯乐在线 - 吴鹏煜译文链接： http://blog.jobbole.com/50603/