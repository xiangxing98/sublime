How_To_Install_Python_Module.md

2011-07-21 17:27:24|  分类： python |  标签：python  模块安装   |举报|字号 订阅
下载LOFTER客户端
Python模块安装方法


## 一、方法1： 单文件模块
直接把文件拷贝到 $python_dir/Lib

## 二、方法2： 多文件模块，带setup.py

下载模块包，进行解压，进入模块文件夹，执行：
python setup.py install

## 三、 方法3：easy_install 方式

 先下载ez_setup.py,运行python ez_setup 进行easy_install工具的安装，之后就可以使用easy_install进行安装package了。
  easy_install  packageName
  easy_install  package.egg

## 四、 方法4：pip 方式 

先进行pip工具的安裝：easy_install pip（pip 可以通过easy_install 安裝，而且也会装到 Scripts 文件夹下。）

安裝：pip install PackageName

更新：pip install -U PackageName

移除：pip uninstall PackageName

搜索：pip search PackageName

帮助：pip help

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

注：虽然Python的模块可以拷贝安装，但是一般情况下推荐制作一个安装包，即写一个setup.py文件来安装。
setup.py文件的使用如下:
% python setup.py build     #编译
% python setup.py install    #安装
% python setup.py sdist      #制作分发包
% python setup.py bdist_wininst    #制作windows下的分发包
% python setup.py bdist_rpm

setup.py文件的编写
setup.py中主要执行一个 setup函数，该函数中大部分是描述性东西，最主要的是packages参数，列出所有的package，可以用自带的find_packages来动态获取package。所以setup.py文件的编写实际是很简单的。
简单的例子:
setup.py文件：

 from setuptools import setup, find_packages
setup(
       name = " mytest " ,
       version = " 0.10 " ,
       description = " My test module " ,
       author = " Robin Hood " ,
       url = " http://www.csdn.net " ,
       license = " LGPL " ,
       packages = find_packages(),
       scripts = [ " scripts/test.py " ],
       )

mytest.py

import sys
def get():
     return sys.path

scripts/test.py

import os
print os.environ.keys() 

setup中的scripts表示将该文件放到 Python的Scripts目录下，可以直接用。OK，简单的安装成功，可以运行所列举的命令生成安装包，或者安装该python包。本机测试成功(win32-python25)！


附注：setuptools工具安装方法

（方法一）. 使用ez_setup.py安装setuptools
　　进入https://pypi.python.org/pypi/setuptools下载ez_setup.py
 这是 setuptools 自豪的一种安装方式，只需要一个大约 8K 作为的脚本ez_setup.py，就能自动为用户安装包括 setuptools 自身在内的许多 Python 包。 使用这种方式，用户只需要下载 ez_setup。py 并运行，就可以自动下载和安装适合用户当前 Python 版本的适当的 setuptools egg 文件(当然，用户需要 Python 2.3.5 以上的版本，64 位操作系统的用户则需要 Python 2.4 以上的版本)。此外，这段脚本还会将可执行的 easy_install 脚本安装到用户所有的操作系统 Python 可执行脚本正常应该安装的位置(例如，Windows 用户会安装到 Python 安装目录下的 Scripts 目录中)。关于这种安装方法的更详细说明和注意事项，请参考其官方说明（见扩展阅读）。简单的安装命令如下： 　　wget -q ez_setup。py下载地址（见扩展阅读） 安装完后，最好确保
（方法二）. 使用完整的安装包安装setuptools
　　当然，用户也可以直接使用 setuptools发布版本来安装。对于使用 Windows 的用户，这也是挺方便的方法，许多 Linux 发行版的官方包管理仓库都包含 setuptools 的某个版本。例如，如果你跟我一样使用 Ubuntu ，那安装 setuptools 只是简单的进行如下操作：
# apt-get install python-setuptools
安装 easy_install package-name，比如 easy_install pylab
模块卸载 easy_install -m package-name， 比如easy_install -m pylab
easy_install -m 包名，可以卸载软件包，但是卸载后还要手动删除遗留文件。
setuptools它可以自动的安装模块，只需要你提供给它一个模块名字就可以，并且自动帮你解决模块的依赖问题。一般情况下用setuptools给安装的模块会自动放到一个后缀是.egg的目录里。

## windows install easy_install
```
cd /d E:\GitHub\sublime\python
python ez_setup.py
```
ok
>Installed d:\program files\python3\lib\site-packages\setuptools-18.0.1-py3.4.egg
>Processing dependencies for setuptools==18.0.1
>Finished processing dependencies for setuptools==18.0.12

有了setuptools，我们就要开始配置环境。因为你需要用到python安装目录下的Scripts文件夹里面的文件
在Windows里，easy_install这个命令在python安装目录下的scripts里面，所以需要把scripts加到环境变量的PATH里，这样用起来就更方便，linux下不需要注意这个问题。
"D:\Program Files\Python3\"

系统环境变量Path
先在最后加一个分号;
然后再输入 “你的python路径”\Scripts
比如我的python安装路径是D:\Program Files\Python3\
那么我应该输入D:\Program Files\Python3\Scripts

设置完毕之后，就可以直接用命令行安装模块了。
比如我要安装PIL模块，只需要输入easy_install PIL
回车

issues still exists
easy_install web.py
ImportError: No module named 'utils'
C:\DOCUME~1\ADMINI~1\LOCALS~1\Temp\easy_install-kaocolsk\web.py-0.37\

Python 实战（0）：初识 web.py

2015-03-29 Crossin的编程教室 Crossin的编程教室
在 Python 系列的基础课程结束之后，很长一段时间我不知道该写点什么。再加上工作很忙，也没法很系统地写一些教程文章。于是之前东拉西扯说过不少方面的东西，也分享过一些别人的文章。但我始终还是觉得该写点什么，虽然更新的频率不会很高。

有些初学 Python 的同学表示能不能提供一些实例，结合基础知识的学习。也有不少已经完成基础内容学习的同学询问，如何可以进一步提高编程能力。鉴于此，我想接下来的一段时间，做一个比较长的系列：这个系列会以一个项目为主线，过程中大概不会专门针对某一个内容去讲，基本是写到哪讲到哪，比较随意。目前对这个项目的初步设定是一个关于电影的网站，会涉及到网站搭建、爬虫、数据处理、数据库等内容，也会稍为涉及一点HTML相关的内容。

以这样的方式来做，对于初学编程的人，可以对软件开发这件事情有个更直观的认识，不再局限于用代码解题这种层面；对于已经有一定的编程基础人，我希望能抛砖引玉，给大家一点启发。你们可以在我这个虚拟项目的基础上，添加自己喜欢的功能，也可以仿照这个流程另起炉灶，做一些自己设计的项目。对于我自己来说，也可以更好地分享一些编程中的经验，而不是再和网上可以搜到的众多教程一样反复炒冷饭。

目前想法：如果进展顺利，会把项目放在 Github 上维护，同时也会在互联网上放置一个可运行的版本供人使(wei)用(guan)。这都是后话了。

那么今天先开个场：既然要做一个跟网站相关的项目，少不了要选择一个基于 Python 的 web 开发框架。这次我打算选择 web.py。我本人对 django 的经验比较多，web.py 并没有用过。不过都说 web.py 很简单，那么用来玩一玩也无妨。同时，也算是对 Aaron Swartz 致以我个人的敬意。

安装 web.py

web.py 有几种下载方式，通常用 easy_install 会比较方便一点。关于 easy_install 的使用网上可以很容易搜到，这里不再赘述。安装 easy_install 后，Linux 和 Mac 下都可以通过命令

sudo easy_install web.py

完成安装。Windows 下应该不用 sudo，手边没有 Win 系统无法验证，见谅。

或者也可以通过 pip 安装、下载或 clone 安装包等方式进行安装。

在你的 Python 命令行下输入

import web

无任何报错说明已安装成功。

运行你的第一个网站

在一个你找得到的地方新建一个叫做 code.py 的文件，然后输入敲入以下代码并保存：

import web

urls = (

'/', 'index'

)

class index:

def GET(self):

return "Hello, world!"

if __name__ == "__main__":

app = web.application(urls, globals())

app.run()

具体这些代码的含义今天先不解释，保证不要输错就好。

从命令行进入 code.py 所在的目录，运行：

python code.py

不出意外的话，应该会看到输出：

http://0.0.0.0:8080/

用浏览器打开这个地址，就可以看到一个只写着 Hello, world! 的页面。不过有些浏览器（比如我的 Chrome）会不认 0.0.0.0 这个地址而进行搜索。如果遇到这种情况，可以在运行时指定地址为 127.0.0.1，即：

python code.py 127.0.0.1

然后访问 http://127.0.0.1:8080/ 就 OK 了。

也许这就是你人生第一个网站吧，想想是不是还有点小激动呢。前方的路还很长，欲速则不达，且行且珍惜。

如果你按捺不住想要了解更多，可以先去 webpy.org 瞅瞅。上面的新手引导有中文版本。

#==== Crossin的编程教室 ====#

微信ID：crossincode

论坛：http://crossin.me

QQ群：241080058



感谢UPYUN对本微信的支持。UPYUN是国内领先的云服务提供商，专注于为开发者提供静态文件的云存储、云处理和CDN加速服务。现在注册www.upyun.com，即可免费体验！

« Older Article Python 实战（1）：在网页上显示信息
Newer Article » 【python课程】编程中的一个实用函数