# Sublime_Tutorial_For_Beginers.md

<!-- MarkdownTOC -->

- 写在前面
- 二.安装Sublime
- 三.常用快捷键
- 四.好用的插件
- 参考资料

<!-- /MarkdownTOC -->

时间 2015-05-28 23:13:44 黯羽轻扬

原文:[sublime指南](http://ayqy.net/blog/sublime指南/)

主题 Sublime Text

## 写在前面

之前一直在用notepad++，感觉也还不错。后来发现身边的人比自己写代码速度快很多，有点不服，就去找插件了，打算找个更好的代码补全插件，以提高效率。找来找去的结果就是卸载了npp，改用sublime。。

P.S.之前的之前一直在用Dreamweaver，后来发现编辑几千行的源码文件时会莫名其妙地崩溃，无法忍受，才换了轻小的npp，sublime也早就装了，感觉界面不如npp顺眼就一直没有用

一.Sublime的优势

其实放弃npp最直接的原因是找不到一款可以生成注释模版的插件（类似于Eclipse的Alt + Shift + j），前端开发中注释非常重要，没有方便的插件是万万不能接受的

找插件的过程中发现很多插件是针对PHP/Python的，针对前端的插件不多，而且根本没有找到好用的，至于代码补全/注释生成或许可以通过QuickText插件实现，但还是相对麻烦

Sublime最吸引人的地方可能是 Ctrl + p 提供的超便捷的功能，输入@显示函数/变量，输入:n跳转到第n行，这几个简单的功能在npp里至少需要2-3个插件，多一个插件意味着要多记一个快捷键组合

当然，npp也有亮点，比如自带的Launch in Chrome/IE/FF，而Sublime中需要装插件才能实现

放弃npp最大的原因是npp的前端插件不够用，很多插件都早就不更新了，而Sublime的前端插件本来就很多，而且正在变得越来越多

P.S.不用担心Sublime收费的问题，据说可以永久试用，只是偶尔会弹个提示框出来。当然，还有一种东西叫做注册码。。

## 二.安装Sublime

官网： http://www.sublimetext.com/

下载安装即可，目前稳定版本是2.0.2，注册码如下：

----- BEGIN LICENSE -----

Andrew Weber

Single User License

EA7E-855605

813A03DD 5E4AD9E6 6C0EEB94 BC99798F

942194A6 02396E98 E62C9979 4BB979FE

91424C9D A45400BF F6747D88 2FB88078

90F5CC94 1CDC92DC 8457107A F151657B

1D22E383 A997F016 42397640 33F41CFC

E1D0AE85 A0BBD039 0E9C8D55 E1B89D5D

5CDB7036 E56DE1C0 EFCC0840 650CD3A6

B98FC99C 8FAC73EE D2B95564 DF450523

------ END LICENSE ------

## 三.常用快捷键

1.万能命令

Ctrl+P，万能命令面板，直接键入字母搜索项目文件，速度很快。

Ctrl+P+输入@，js列出本文件的所有函数名\html列出所有id。

Ctrl+P+输入:N（N为数字），直接跳到第N行。

2.查询

Ctrl+Shift+F，快速在项目中查找关键词，类似于ack-grep的功能。

3.注释代码

Ctrl+/ 注释整行（如已选择内容，同“Ctrl+Shift+/”效果）

Ctrl+Shift+/ 注释已选择内容

4.折叠代码

Ctrl+Shift+[ 折叠代码

Ctrl+Shift+] 展开代码

Ctrl+KT 折叠属性

Ctrl+K0 展开所有

5.分栏

Alt+Shift+1 一栏浏览模式

Alt+Shift+2 垂直两栏浏览模式

Alt+Shift+8 水平两栏浏览模式

6.书签

Ctrl+F2 设置书签

F2 下一个书签

Shift+F2 上一个书签

7.选择

Ctrl+L 选择整行（按住-继续选择下行）

Ctrl+KK 从光标处删除至行尾

Ctrl+Shift+K 删除整行

Ctrl+Shift+D 复制光标所在整行，插入在该行之前

Ctrl+J 合并行（已选择需要合并的多行时）

Ctrl+KU 改为大写

Ctrl+KL 改为小写

Ctrl+D 选词 （按住-继续选择下个相同的字符串）

Alt+F3 一次性选择全部的相同文本进行同时编辑

Shift+鼠标右键 一次性选择全部的相同文本进行同时编辑

Ctrl+鼠标左键 可以手动选择同时要编辑的多处文本

Ctrl+M 光标移动至括号内开始或结束的位置

Ctrl+Shift+M 选择括号内的内容（按住-继续选择父括号）

Ctrl+Z 撤销

Ctrl+Y 恢复撤销

Ctrl+M 光标跳至对应的括号

Alt+. 闭合当前标签

Ctrl+Shift+A 选择光标位置父标签对儿

Ctrl+U 软撤销

Ctrl+T 词互换

Tab 缩进 自动完成

Shift+Tab 去除缩进

Ctrl+Shift+↑ 与上行互换

Ctrl+Shift+↓ 与下行互换

Ctrl+K Backspace 从光标处删除至行首

Ctrl+Enter 光标后插入行

Ctrl+Shift+Enter 光标前插入行

## 四.好用的插件

1.Sublime Package Control

插件管理器，不装会腰疼

2.GBK Encoding Support

如果打开某txt文件发现 中文乱码 ，那么你可能需要这个

3.Emmet

zenCoding升级版

保护手指的神器，类似于Markdown一样的东西， 具体语法

使用方法：快捷键 ctrl+e

4.BracketHighlighter

匹配的括号高亮显示

使用方法：自动

5.DocBlockr

注释模版生成工具（因为这个才抛弃了NPP）

使用方法：输入 “/**” + enter调出 (在function的上面一行才有效果)

6.js Format

看别人的代码得用这个

使用方法：快捷键 ctrl+alt+F

有了上面这6个插件应该是很不错了

## 参考资料

前辈博文 ：这篇文章真是太有用了

Sublime Text2.0.2注册码

