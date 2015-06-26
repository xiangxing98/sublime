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

在Windows里，easy_install这个命令在python安装目录下的scripts里面，所以需要把scripts加到环境变量的PATH里，这样用起来就更方便，linux下不需要注意这个问题。