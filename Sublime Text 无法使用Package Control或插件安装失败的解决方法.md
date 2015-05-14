Sublime Text 无法使用Package Control或插件安装失败的解决方法

时间：2015-03-14 18:33:51      阅读：482      评论：0      收藏：0      [点我收藏+]
标签：sublime text   package control   pyv8安装   安装失败   快捷键   

Sublime Text用了一年多了，公司搬家最近突然发现Package Control无法安装新插件了，虽然不影响原有功能的使用，还是要解决它。由于本人用Windows系统，只讨论Windosw下的解决方法。Mac与Linux下的用户可以参照解决。

本文主要介绍Sublime Text如何开启debug模式，分析使用过程中一些常见错误情形的解决方法。情形一：Package Control:There are no packages available for installation。情形二：Package Control:Unableto download Emmet.Please view the console for more details. Error while loading PyV8 binary:exit code 3 …情形三：无法打开Package Control或没有安装PackageControl。稍后简单介绍一下前端开发常用的Package插件，最后会补充一些常用快捷键的作用等。

为了更准确的定位问题，建议插件在安装前开启控制台（快捷键Ctrl+~）,同时在开启debug模式，这样可以在安装过程中了解哪一步出了问题，然后有针对性的去解决问题。

 一、开启Debug模式

Debug模式开启方法：将PackageControl.sublime-settings文件中的debug参数设为true,举个例子，我的文件处于安装目录的这个位置：

D:\Program Files\Sublime Text 2\Data\Packages\PackageControl\ PackageControl.sublime-settings

 

技术分享
 

更多参数的含义，参见官网https://packagecontrol.io/docs/settings

二、安装错误情形 

下面汇总了安装过程中可能出现的一些常见问题：

 

情形一：Package Control：There are no packages available for installation

技术分享
 

据StackOverflow上说是IPv6造成，如果我们的Intent服务提供者（ISP）不支持IPv6就会引发上述错误，原文如下：

 

This error is happened with IPv6 problem. If yourInternet Service Provider (ISP) does not support for IPv6 you got this error.

具体请参考：http://stackoverflow.com/questions/25105139/sublime-text-2-there-are-no-packages-available-for-installation

如果IPV6有问题，curl就会打印类似这样的错误：

curl: (7) Failed to connect to xxxxx...

找到了问题原因，下面着手解决它。

 

第一步：取得sublime.wbond.net的IPv4地址。在命令提示符中输入以下命令：

ping sublime.wbond.net

技术分享
第二步：打开C:\Windows\system32\drivers\etc\hosts文件，增加如下对应关系：{IPv4 address}sublime.wbond.net

 技术分享技术分享

保存文件，然后再打开Package Control（快捷键Ctrl+Shift+P）开始安装即可。

 

情形二：Package Control：Unableto download Emmet.Please view the console for more details./Error while loading PyV8 binary:exit code 3…

 技术分享

类似这种插件无法下载的问题，一般是由于网速慢，或者目标域名被墙而无法正常访问导致的。

这种情况下，首先检查本地网络是否可以访问，检测下载速度是不是特别慢，

如果网速太慢，换个时间再安装。还有一个办法是：到github或第三方网站手动下载安装包，然后解压到安装目录下的/Packages目录下。

 

比如我的Emmet则需要解压到D:\ProgramFiles\Sublime Text 2\Data\Packages\Emmet目录下。

 

另外许多插件都依赖于Python的，在插件安装开始时会去下载Python相关资源，

比如，Emmet安装就会先下载你系统位数一致的Python版本，我们在debug窗口可以看到这些信息：

技术分享
其中有两条，表示下载失败，原因一般是网速慢请求超时或被墙了。

Emmet: Loading PyV8 binary from https://raw.github.com/emmetio/pyv8-binaries/master/pyv8-win64.zip

Emmet.pyv8loader: Unable to download package from https://raw.github.com/emmetio/pyv8-binaries/master/pyv8-win64.zip Wrong URL error

同时，pyv8下载失败会弹出一个提示框：

 技术分享

这时候，我们按照给出的zip包下载地址手动下载PyV8的安装包（PyV8的项目地址为https://github.com/emmetio/pyv8-binaries#readme，可以根据系统种类选择对应安装包），下载成功后打开菜单Preferences – Browser Packages，然后解压到子目录PyV8内。比如我的对应目录是D:\Program Files\Sublime Text2\Data\Packages\PyV8\win64（若你的是32位系统，最终目录则为win32）。

 

大多数情况，PyV8安装好了以后，再安装需要的其他插件便可顺利进行了。

 

情形三：无法调出Package Control或未安装PackageControl

首次安装或重新安装的方式是一样的，首先打开控制台（Ctrl+~），不过Sublime Text的版本不同，执行的命令是不一样的。

 

对于Sublime Text2输入以下命令执行：

import urllib2,os,hashlib; h = 'eb2297e1a458f27d836c04bb0cbaf282' + 'd0e7a3098092775ccb37ca9d6b2e4b7d'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler()) ); by = urllib2.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); open( os.path.join( ipp, pf), 'wb' ).write(by) if dh == h else None; print('Error validating download (got %s instead of %s), please try manual install' % (dh, h) if dh != h else 'Please restart Sublime Text to finish installation')
对于Sublime Text 3需要输入如下的命令：

import urllib.request,os,hashlib; h = 'eb2297e1a458f27d836c04bb0cbaf282' + 'd0e7a3098092775ccb37ca9d6b2e4b7d'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
执行完后，Package Control安装成功。此时便可以调出PackageControl命令输入面板（Ctrl+Shift+P），输入install

 

除了使用上述命令安装法，还可手动安装，需要的可访问官网查看https://packagecontrol.io/installation#st3

 三、 安装官方原版

上面的问题解决了，但是想想这么强大的工具，这么多的问题，持怀疑态度。折腾了这么久再卸载了有点太可惜了。不过为了弄清楚问题根本，狠狠心，果断卸载了我一直使用的Sublime Text 2 某破解优化版，其中已集成了JsFormat，Alignment，Emmet等这些常用的插件。卸载后去官网下载了官方版本http://www.sublimetext.com/2

并安装完成。

 

这次安装，先不要着急打开Sublime Text。为了以后安装方便，决定不再使用系统默认的Packages安装路径C:\Users\Administrator\AppData\Roaming\Data，在Sublime Text2的安装目录下新建文件夹/Data，该文件夹创建完成后再打开Sublime Text程序，我们发现，Packages被安装在了当前创建的文件夹下（我的路径是D:\Program Files\Sublime Text 2\Data）。稍后把其他必备插件装全了，我们备份一下Sublime Text 2文件夹，这样以后走到哪都可以无须一步步重新安装，快速部署我们的Sublime Text环境。

技术分享 

这次安装了七八个插件，也没有出现一次上述错误，说明官方版本还是比较靠谱比较稳定的。虽然每个月都会弹出付费注册提示，不过不影响使用就这样用吧。有洁癖的我建议你安装Sublime Text 3，本人测试发现最新版这个破解版相对来说比国内流行的某v2版要稳定的多，不过支持ST3的插件目前相对少一些。

英文官方原版首次使用时，会有两个依赖包升级提示: 

技术分享

技术分享

或

技术分享 

点“确定关闭”即可，无须理会。


四、Sublime必备插件



补充几个必备的开发插件，不了解作用的自行查找吧。

必备的：Alignment，JsFormat，CSSComb，CTags，DocBlockr，Emmet，FileDiffs，SASS，LESS，SASS Build，Lessc，Git，SublimeLinter

另外还有几个不错的，可以选择使用：Terminal，Trimmer，ColorPicker，ConverToUTF8等。


五、补充知识

 

最后普及几个需要了解的知识：

1.所装的插件列表(有些不在里面)

D:\Program Files\Sublime Text2\Data\Packages\User\Package Control.sublime-settings

2. Package Control常用的命令InstallPackage (安装扩展)、List Packages (列出全部扩展)、Remove Package (移除扩展)、Upgrade Package (升级扩展)

3.插件热键冲突，可以自定义修改：Preferences > Package Settings > Alignment（或其他插件名） > Key Bindding - User然后写入快捷键。（有些插件需要到安装目录下的配置文件修改）

4.有Package Control其他相关问题上，上github项目查找。

https://github.com/wbond/package_control/issues?q=is%3Aclosed

 

比如较常见的问题Package control fails to download new packages：

https://github.com/wbond/package_control/issues/736

5.列一下常用的快捷键：

                                                                                           

Ctrl+D 选词 （反复按快捷键，即可继续向下同时选中下一个相同的文本进行同时编辑）

Ctrl+G 跳转到相应的行

Ctrl+J 合并行（已选择需要合并的多行时）

Ctrl+L 选择整行（按住-继续选择下行）

Ctrl+M 光标移动至括号内开始或结束的位置

Ctrl+T 词互换

Ctrl+U 软撤销

Ctrl+P 查找当前项目中的文件和快速搜索；输入 @ 查找文件主标题/函数；或者输入 : 跳转到文件某行；

Ctrl+R 快速列出/跳转到某个函数

Ctrl+K Backspace 从光标处删除至行首

Ctrl+KB 开启/关闭侧边栏

Ctrl+KK 从光标处删除至行尾

Ctrl+KT 折叠属性

Ctrl+KU 改为大写

Ctrl+KL 改为小写

Ctrl+K0 展开所有

Ctrl+Enter 插入行后（快速换行）

Ctrl+Tab 当前窗口中的标签页切换

Ctrl+Shift+A 选择光标位置父标签对儿

Ctrl+Shift+D 复制光标所在整行，插入在该行之前

ctrl+shift+F 在文件夹内查找，与普通编辑器不同的地方是sublime允许添加多个文件夹进行查找

Ctrl+Shift+K 删除整行

Ctrl+Shift+L 鼠标选中多行（按下快捷键），即可同时编辑这些行

Ctrl+Shift+M 选择括号内的内容（按住-继续选择父括号）

Ctrl+Shift+P 打开命令面板

Ctrl+Shift+/ 注释已选择内容

Ctrl+Shift+↑可以移动此行代码，与上行互换

Ctrl+Shift+↓可以移动此行代码，与下行互换

Ctrl+Shift+[ 折叠代码

Ctrl+Shift+] 展开代码

Ctrl+Shift+Enter 光标前插入行

Ctrl+PageDown 、Ctrl+PageUp 文件按开启的前后顺序切换

Ctrl+Z 撤销

Ctrl+Y 恢复撤销

Ctrl+F2 设置书签

Ctrl+/ 注释整行（如已选择内容，同“Ctrl+Shift+/”效果）

Ctrl+鼠标左键 可以同时选择要编辑的多处文本

Shift+鼠标右键（或使用鼠标中键）可以用鼠标进行竖向多行选择

Shift+F2 上一个书签

Shift+Tab 去除缩进

Alt+Shift+1~9（非小键盘）屏幕显示相等数字的小窗口

Alt+. 闭合当前标签

Alt+F3 选中文本按下快捷键，即可一次性选择全部的相同文本进行同时编辑

Tab 缩进 自动完成

F2 下一个书签

F9 行排序(按a-z)

F11 全屏模式

更多快捷键请参考这篇文章http://blog.csdn.net/fovwin/article/details/9102731

关于Sublime Text的问题就说这么多，基本上汇总了自己使用一年多遇到的各种问题吧。分享出来，希望能对大家有用。

 

本文来源于CSDN空间freshlover的博客《Sublime Text 无法使用Package Control或插件安装失败的解决方法》，转载请注明出处，谢谢！

http://blog.csdn.net/freshlover/article/details/44261229 
