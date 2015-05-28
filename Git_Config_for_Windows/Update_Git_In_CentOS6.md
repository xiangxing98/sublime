# Update_Git_In_CentOS6
[Reference](http://blog.csdn.net/ljianhui/article/details/23888269)

Git现在的版本（我在写下本文时）已经是1.7.12了，然而CentOS的Git的版本却是1.7.1，而且用yum安装的Git的最高版本也只是去1.7.1，当然，如果你在工作使用中没有遇到问题，使用这个版本当然没有什么问题，但是如果你在工作中遇到只有高版本的Git才能支持的任务时，如何升级我们的Git呢？事实上，GitHub和许多Git服务依赖的Git版本不低于1.7.2。下面就以CentOS-6.5为例来说明，如何升级我们的Git。

## 一、安装证书
使用rpm的强大功能，从以下的地址中，导入安装所需要的证书，命令如下：
```bash
su
#[root@siqin siqin]# 

rpm --import http://apt.sw.be/RPM-GPG-KEY.dag.txt
```

## 二、安装RPMForge源
RPMForge源是什么呢？RPMForge是CentOS系统下的软件仓库，拥有4000多种的软件包，被CentOS社区认为是最安全也是最稳定的一个软件仓库。而CentOS默认自带CentOS-Base.repo源，但官方源中去除了很多有版权争议的软件，而且安装的软件也不是最新的稳定版。所以在这里，我们使用这个rpm软件仓库。其地址如下：
[http://rpmfusion.org](http://rpmfusion.org)
因为不同的CentOS版本的Git所对应的rpm包不同，所以在下载安装RPMForge时可先到该网站找到适合自己系统安装的RPMForge的rpm包。其地址如下：[http://pkgs.repoforge.org/rpmforge-release/](http://pkgs.repoforge.org/rpmforge-release/)
因为我的CentOS是CentOS-6.5 32 位，所以我对应的rpm安装包就是：rpmforge-release-0.5.3-1.el6.rf.i686.rpm，所以可用以下命令来安装：
```bash
rpm -i http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.i686.rpm
```
通过rpm的在线安装功能，我们也可以不下载rpm包，而直接在线安装

## 三、使用rpmforge-extra源更新
因为yum命令下载的软件依赖于其所使用的软件仓库，所以我们只要更改其指定的软件仓库，就能使用yum来方便地下载安装RPMForge源中的软件来更新本机的软件，从而简化安装操作。其命令如下：
```bash
yum --enablerepo=rpmforge-extras update
```
你会看到由于软件仓库的切换，导致会有大量的软件可更新，你可以选择安装或不安装。若选择安装，则输入‘y’,那么当安装完成时，Git也就变为最新的版本了，我就是用这种方式的。但由于要更新的软件实在太多，所以，也可以选择只安装Git，输入了‘n’。

注：上面的命令其实与yum update是一样的，只是上面的命令指定更新对比的软件仓库为RPMForge。经过我的观察，选项--enablerepo=rpmforge-extras并不会改变yum的默认软件仓库，所以每次要想从下载软件，都需要该选项。要想一直使用第三方的源，应需要安装yum-priorities插件，并配置相关文件/etc/yum.repos.d/CentOS-Base.repo。（这里如有错误还望指出）

## 四、查看可用的git模块
由于我们并不知道，我们的系统可以安装哪些版本的Git,所以可用如下命令来查看，并选择一个最新版本的git来安装。其命令如下：
```bash
yum --enablerepo=rpmforge-extras provides git

#通过下面的命令查找(推荐)
yum --enablerepo=rpmforge-extras provides git
#newest git @ 2015-05-28
#git-1.7.12.4-1.el6.rfx.i686
```

## 五、安装Git
由于我们使用的是RPMForge的软件仓库，所以在安装时，如果没有运行上第四点的命令，而又想知道，自己的系统应该选择哪个版本来安装，我们可以到其仓库中找到我们版本所对应的Git，其地址如下：
http://pkgs.repoforge.org/git/
由于我的是CentOS-6，所以最新的就是gitk-1.7.12.4-1.el6.rfx.i686.rpm了。http://pkgs.repoforge.org/git/gitk-1.7.12.4-1.el6.rfx.i686.rpm
其命令如下：
```bash
yum --enablerepo=rpmforge-extras install gitk-1.7.12.4-1.el6.rfx.i686.rpm
yum --enablerepo=rpmforge-extras install perl-Git-1.7.12.4-1.el6.rfx.i686.rpm
#No package gitk-1.7.12.4-1.el6.rfx.i686.rpm available.
```

## 六、版本检查
至此，我们的Git已经升级好了，旧的Git会被新的覆盖，我们可以通过如下命令来查看，git的版本：
```bash
git --version
#or use
rpm -q git
```

# Upgrade Git 1.7.4 to 1.9.0
```bash
. tar zxvf git-latest.tar.gz
. ./configure
. make
. make install
```

## 阿里云上配置CentOS安装Git（小沐git安装命令全集整理版）

http://www.bitscn.com/os/linux/201410/337776.html

```bash
#install git dependancy
yum install curl
yum install curl-devel
yum install zlib-devel
yum install openssl-devel
yum install perl
yum install cpio
yum install expat-devel
yum install gettext-devel
wget http://distfiles.macports.org/git/git-2.4.1.tar.gz
#http://distfiles.macports.org/git/git-2.1.1.tar.gz
#http://distfiles.macports.org/git/git-2.4.1.tar.gz
tar xzvf git-latest.tar.gz
cd git-2011-11-30 ＃你的目录可能不是这个
autoconf
./configure
make
sudo make install
git --version
```

步骤比较简单
主要是记录下 实现的过程 备忘！
比较详细的教程：http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137583770360579bc4b458f044ce7afed3df579123eca000
CentOS的yum源中没有git，只能自己编译安装
确保已安装了依赖的包
下载最新的git包
检查下安装的版本，大功告成
参考：
### 1 关于版本控制
版本控制是一种记录一个或若干文件内容变化，以便将来查阅特定版本修订情况的系统。有以下三种版本控制系统：
1. 本地版本控制系统
许多人习惯用复制整个项目目录的方式来保存不同的版本，或许还会改名加上备份时间以示区别。这么做唯一的好处就是简单。不过坏处也不少：有时候会混淆所在的工作目录，一旦弄错文件丢了数据就没法撤销恢复。
为了解决这个问题，人们很久以前就开发了许多种本地版本控制系统，大多都是采用某种简单的数据库来记录文件的历次更新差异。图示如下，
wKioL1NHz9KwrLVKAAB_hYDNW_c407.jpg
2. 集中化的版本控制系统
集中化的版本控制系统（ Centralized Version Control Systems，简称 CVCS ）能够让在不同的开发系统上的开发人员协同工作。这类系统，诸如 CVS，Subversion 以及 Perforce 等，都有一个单一的集中管理的服务器，保存所有文件的修订版本，而协同工作的人们都通过客户端连到这台服务器，取出最新的文件或者提交更新。多年以来，这已成为版本控制系统的标准做法
wKiom1NH0IrgjvjzAADzyUyCgk0082.jpg
3. 分布式版本控制系统
分布式版本控制系统(Distributed Version Control System，简称 DVCS ),像 Git，Mercurial，Bazaar 以及 Darcs 等，客户端并不只提取最新版本的文件快照，而是把代码仓库完整地镜像下来。这么一来，任何一处协同工作用的服务器发生故障，事后都可以用任何一个镜像出来的本地仓库恢复。因为每一次的提取操作，实际上都是一次对代码仓库的完整备份,
wKiom1NH0OLT_ylwAAFXxaszrSQ988.jpg
更进一步，许多这类系统都可以指定和若干不同的远端代码仓库进行交互。籍此，你就可以在同一个项目中，分别和不同工作小组的人相互协作。你可以根据需要设定不同的协作流程，比如层次模型式的工作流，而这在以前的集中式系统中是无法实现的。

### 2 关于Git
Git是分布式版本控制系统的一个完美实现，它与集中式版本控制系统SVN的基本区别如下：

Git是分布式的，而SVN不是

Git和SVN一样有自己的集中式版本库或服务器。但，GIT更倾向于被使用于分布式模式，也就是每个开发人员从中心版本库/服务器上chect out代码后会在自己的机器上克隆一个自己的版本库。

Git将内容按元数据方式存储，而SVN是按文件

所有的资源控制系统都是把文件的元信息隐藏在一个类似.svn,.cvs等的文件夹里。如果你把.git目录的体积大小跟.svn比较，你会发现它们差距很大。因为,.git目录是处于你的机器上的一个克隆版的版本库，它拥有中心版本库上所有的东西，例如标签，分支，版本记录等。

Git分支和SVN分支的不同

SVN的分支就是版本库中的另外一个目录，而Git的分支却是整个版本库的一个快照，而且可以在同一个工作目录下快速的在几个分支间切换。
Git没有一个全局的版本号，而SVN有
SVN的版本号实际是任何一个相应时间的源代码快照。而Git并没有这样的一个全局版本号，这也是Git缺少的最大的一个特征
Git的内容完整性要优于SVN
Git的内容存储使用的是SHA-1哈希算法。这能确保代码内容的完整性，确保在遇到磁盘故障和网络问题时降低对版本库的破坏。
Git的基本工作流程如下：

在工作目录中修改某些文件。

对修改后的文件进行快照，然后保存到暂存区域。
123456 	wget http://kernel.org/pub/software/scm/git/git-1.7.6.tar.bz2tar -xzvf git-1.7.6.tar.bz2cd git-1.7.6./configure --prefix=/usr/localmakemake install
12345 	$ mkdir project$ cd project$ git-init-dbgit #将会作出以下的回应defaulting to local storage area#或者Initialized empty Git repository in project/.git/
12 	$ git config --global user.name "Your Name Comes Here"$ git config --global user.email you@pub.admon.org
123 	$ cd project$ echo "tmp" > .gitignore$ git add .
123 	$ cp -R project/.git /tmp/test.git$ cd /tmp$ git clone test.git test-copy
提交更新，将保存在暂存区域的文件快照永久转储到 Git 目录中。 

### 3 Git服务器搭建
#### 1. 环境部署
系统环境：服务器端：CentOS 6.5 ，ip：192.168.56.1
客户端：CentOS 6.5 ，ip：192.168.56.101
软件版本：服务器端：源码编译安装，git-1.9.0.tar.gz
客户端：yum在线安装机制 

#### 2. 安装

##### 2.1 服务器端：
```
#yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel perl-devel
#wget http://git-core.googlecode.com/files/git-1.9.0.tar.gz
#tar zxvf git-1.9.0.tar.gz
#cd git-1.9.0
#make prefix=/usr/local all
#make prefix=/usr/local install #root用户运行 
```

查看版本号：git --version
`git version 1.9.0 `
安装gitosis：gitosis为Git用户权限管理系统,通过管理服务端的/home/git/.ssh/authorized_key文件来执行对用户权限的管理，是一个python模块包
```
#yum install python python-setuptools
#git clone git://github.com/res0nat0r/gitosis.git
#cd gitosis/
#python setup.py install
```
显示Finished processing dependencies for gitosis==0.2即表示成功 

#####2.2 客户端安装：

```
#yum install git
#git --version
git version 1.7.1 
```

#### 3. ssh设置
客户端生产密钥并上传到服务器端：
`#ssh-keygen -t rsa`
`#scp ~/.ssh/id_rsa.pub root@192.168.56.1:~/`
服务端查看已经上传的密钥：ls ～/id_rsa.pub 

#### 4. 服务器上生成git用户，使用git用户并初始化gitosis
添加用户git：
`#useradd -r -s /bin/sh -c 'git version control' -d /home/git git`
设置权限：
`#mkdir -p /home/git`
`#chown git:git /home/git`
 
在服务器端生成管理库：
`#sudo -H -u git gitosis-init < ～/id_rsa.pub`
Initialized empty Git repository in /home/git//repositories/gitosis-admin.git/ Reinitialized existing Git repository in /home/git/repositories/gitosis-admin.git/
注解：
1. 生成的gitosis-admin为Git的用户访问权限管理库，gitosis通过这个git库来管理所有git库的访问权限。
2. 通过执行初始化，该公钥的拥有者就能修改用于配置gitosis的那个特殊Git仓库了
 
修改上传权限：
#chmod 755 /home/git/repositories/gitosis-admin.git/hooks/post-update
 

#### 5. 客户端导出管理
```
#mkdir -p /git-repo/
#cd /git-repo/
#git clone git@192.168.56.1:gitosis-admin.git
#cd gitosis-admin
#find .
./gitosis.conf
./keydir
./keydir/oot@vm1.pub
```
注解：
gitosis.conf文件用来设置用户、仓库和权限的控制文件
keydir目录则是保存所有具有访问权限用户公钥的地方
./keydir/root@vm1.pub:如前所述，该用户具有访问权限
 
#### 6. 客户端创建及设置管理项目
```
#cd /git-repo/gitosis-admin
查看已经上传密钥
#ls keydir/
root@vm1.pub
```
 
授权和权限控制
```
#vim gitosis.conf
[gitosis]

[group gitosis-admin]
writable = gitosis-admin
members = root@vm1 #显示用户root@vm1.pub是初始化gitosis公钥的拥有者，是唯一能管理gitosis-admin项目的人

[group jay_fans] #组名称
members = root@vm1 #密钥用户名
writable = git-test #项目名称
```

#### 7. 初始、增加及使用项目git-test
```
#cd /git-repo
#mkdir git-test
#cd git-test
#git init
#touch README
#git add .
#git commit -a -m "init git-test"
#git remote add origin git@192.168.56.1:git-test.git
#git push origin master
```
注解：在新项目git-test里首次推送数据到服务器前，需先设定该服务器地址为远程仓库，但你不用事先到服务器上手工创建该项目的裸仓库— Gitosis 会在第一次遇到推送时自动创建。
 
#### 8. 客户端增加其他成员公钥到系统中：通过添加用户的公钥到keydir目录即可
`#cd /git-repo/gitosis-admin`
`#cp /path/to/member/public/key keydir/`
`#git add keydir/member.pub`
`修改gitosis.conf`
`[group jay_fans] #组名称`
`members = jay # 新的密钥用户名`
`writable = git-test`
 
提交修改：
`#git commit -a -m "granted jay commit rights to git-test"`
`#git push`
注解：gitosis实际上是从服务器端的/home/git/.gitosis.conf文件读取信息的，通过以上操作，会将新的权限信息写入到该文件中，如果搞错了配置，导致失去了推送权限，可以通过修改该文件来重新设定，如果你手工编辑该文件的话，它会一直保持到下次向 gitosis-admin 推送新版本的配置内容为止。
 
成员jay通过以下命令获取代码：
`#git clone git@192.168.56.1:git-test.git`
 
### 4 Github的使用
GitHub是一个托管Git项目的网站，对于闭源项目收费，开源项目则免费。使用Github进行代码发布和托管的步骤如下：
1. 登录Github官网https://github.com/ ,申请Github账户，并创建名为github-test的Repository
 
2. 安装Git客户端（Linux）
`#yum install git git-gui`
 
3. 生成密钥对，并拷贝到Github网站
`#ssh-keygen -t rsa -C “xxx@gmail.com”`
xxx@gmail.com为你注册Github时的邮箱账户
 
登录Github点击Edit your profile->SSH keys,添加./.ssh/id_rsa.pub中的内容
 
4. 设置ssh不输入口令
```
#eval `ssh-agent`
`#ssh-add`
```
 
5. 测试是否能连接上GIthub
```
#ssh git@github.com
```
PTY allocation request failed on channel 0
Hi rangochan! You've successfully authenticated, but GitHub does not provide shell access.
Connection to github.com closed.
连接成功
 
6. 配置Git全局用户配置
`# git config --global user.name xxx`
`# git config --global user.email xxx@gmail.com`
xxx及xxx@gmail.com分别为Github账户名和邮箱
 
7. 创建本地新项目
```
#mkdir github-test
#cd github-test/
#git init
#touch README
#git add README
#git commit -m 'my first commit'
``` 
 
定义远程服务器别名origin
`#git remote add origin git@github.com:xxx/github-test.git`
 
本地和远程实行合并，本地默认为master
`#git push origin master`
当通过Github以xxx对github-test作出修改时，由于本地快照与Github远程服务器上的不一致，会引起以下错误：
! [rejected] master -> master (fetch first)
error: failed to push some refs to 'git@github.com:xxx/puppet'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
解决：
通过pull子命令更新Github项目中作出的更改
`#git pull origin master`
之后再执行`git push origin master`
Counting objects: 8, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (7/7), 714 bytes | 0 bytes/s, done.
Total 7 (delta 0), reused 0 (delta 0)
 
登录https://github.com/xxx/github-test ,可查看到github-test项目
 
### 8. 更新文件
`#vim README`
`just for test`
 
自动commit更改文件
`#git commit -a`
 
更新到远程
`#git push origin master`
 
### 9. 创建和合并分支
`#git branch`
`* master`
显示当前分支是master

#git branch new-branch
创建分支

`# git checkout new-branch`
切换到新分支

`# vi check.py`
创建新文件
 
`# git add check.py`
`# git commit -a -m "added a python script"`
Commit 到本地Git

`# git push origin new-feature`
合并到远程服务器
 
如果new-branch分支成熟了，则可以合并进master
`#git checkout master`

`#git merge new-branch`

`#git branch`
`* master`
`new-banch`
 
`#git push`
执行合并，master中也合并了new-branch中的更新

登录到GitHub，点击"Switch Branches"可以更改分支来查看不同分支下代码情况。
——Rango Chen


本文出自 “游响云停” 博客，请务必保留此出处
http://rangochen.blog.bitsCN.com/2445286/1394340
 
 
## 1.1 Git 安装
Git的最新版本可以在http://git-scm.com/ 下载 ，它是基于命令行操作的，网上也有第三方开发的相应GUI可供下载，因为我比较喜欢命令行操作，所以没有对GUi下载和安装，有兴趣的同学可以自己试试。网上也有相应的文章和资料可供参考！
安装之前首先确保相应的依赖包已经安装，主要有以下几个:
zlib
libcurl
libcrypto（OpenSSL）
rsync（2.6.0 或更高版本）
这些条件满足之后，就可以对Git进行安装了：
安装成功可以通过git --vertion 查看版本。

## 1.2 项目仓库的建立
欲使用Git 对现有文档进行版本控制，首先要基于现有文档建立项目仓库。创建一个 Git 项目仓库是很容易的，只要用命令 git-init-db 就可以了。

这样，一个空的版本库就创建好了，并在当前目录中创建一个叫 .git 的子目录。
你可以用 ls -a 查看一下，并请注意其中的三项内容：
一个叫 HEAD 的文件，我们现在来查看一下它的内容：
$ cat .git/HEAD现在 HEAD 的内容应该是这样：
ref: refs/heads/master
我们可以看到，HEAD 文件中的内容其实只是包含了一个索引信息，并且，这个索引将总是指向你的项目中的当前开发分支。
一个叫 objects 的子目录，它包含了你的项目中的所有对象，我们不必直接地了解到这些对象内容，我们应该关心是存放在这些对象中的项目的数据。
另外project目录也不再是普通的文档目录了，今后我们将其称为工作树。因为我们主要是linux内核的开发，所以下面我举的例子主要是对内核文件的操作，所以project目录等同于源代码的根目录，亦即linux-2.6-vertex。
下面应当有选择地将工作树中的一些文档存储至Git 仓库中。由于Git 在向仓库中添加文档时并非是简单地文档复制过去，势必要将所添加文档进行一番处理，生成Git 仓库所能接受的数据格式，Git 称这个过程为"take a snapshot（" 生成快照）。若将工作树下所有文档（包含子目录）生成快照，可采用以下命令：
`$ cd project`
`$ git add .`
所生成的快照被存放到一个临时的存储区域，Git 称该区域为索引。使用git-commit 命令可将索引提交至仓库中，这个过程称为提交，每一次提交都意味着版本在进行一次更新。
`$ git commit`
执行上述git-commit 命令时，Git 会自动调用系统 默认的文本编辑器，要求你输入版本更新说明并保存。请记住，输入简约而又意义明确的版本更新说明是非常有必要的，可以帮助你快速回忆起对项目的重大改动。
对于简短的版本更新信息，可以使用git-commit 的“-m”选项，如下：
`$ git commit -m `"你的版本更新信息"
git-commit 命令在后面会详细讲解。
上述过程即为建立Git 仓库的一般过程
另外，在git 项目仓库建立中还要注意一下两个问题：
第一个问题是：在使用Git 之前，你需要面对Git 来一番自我介绍。Git 不喜欢不愿透漏姓名的人，因为它要求每个人在向仓库提交数据时，都应当承担一定的责任。要向Git 进行自我介绍，请使用以下命令：

第二个问题是：在生成文档内容快照时，工作树中有一些文档是你不希望接受Git 管理的，譬如程序编译时生成的中间文件，对于这样的文件如何避免为之生成快照？
譬如在工作树中存在以下子目录：
doc tmp ipc drivers fs
其中的tmp 目录存放着文档编译时生成的中间文件，因此该目录不应该被Git 所管理。为解决此类问题，Git 提供了文档忽略机制，可以将工作树中你不希望接受Git 管理的文档信息写到同一目录下的.gitignore 文件中。对于本例中的tmp 目录，采用如下操作可将其排除仓库之外，然后再对project 生成快照即可。

有关gitignore 文件的诸多细节知识可阅读其使用手册：
`$ man gitignore`

## 1.3 项目仓库与工作树
按照前文的说法，Git 仓库就是那个.git 目录，其中存放的是我们所提交的文档索引内容，Git 可基于文档索引内容对其所管理的文档进行内容追踪，从而实现文档的版本控制。工作树是包含.git 的目录，在前文示例中即project 目录。
为了更加明确仓库与工作树的概念，下面做一个实验：

首先，我们将project 目录中的.git 目录复制到/tmp 目录下并进行重命名为test.git ，然后使用git-clone 命令从test.git 中生成test-copy 目录。若进入test-copy 目录观察一下，就会发现该目录所包含的内容是等同于project 目录的。
上述实验意味着，只要我们拥有仓库，即test.git ，那么就可以很容易地生成工作树，而这个工作树又包含着一个仓库，即test-copy/.git 。所以，我们可以这样理解：在Git 中，仓库与工作树之间无需分的很清楚。

## 1.4 文件操作
在工作树中，我们日常所进行的工作无非是对Git 仓库所管理的文档进行修改，或者添加／删除一些文件。这些操作与采用Git 管理我们的文档之前没有任何差异，只是在你认为一个工作阶段完成之时，要记得通知Git，命令它记下你所进行更新，这一步骤是通过生成文档快照并将其加入 到索引中来实现的。下面举例说明。
譬如我向project 目录添加了一个新文件 fs/binfmt_hwt.c ，我需要通知Git 记住我的这一更新：
`$ cd project`
`$ git add fs/binfmt_hwt.c`
这样，Git 就会将有关fs/binfmt_hwt.c 的更新添加到索引中。然后我又对其它文档进行了一些修改，譬如修改了ipc/msg.c ，继续使用git-add 命令将它们的更新添加到索引中：
`$ git add ipc/msg.c`
这里也可以使用以下命令：
`$ git-update-index`
晚上，这一天的工作告以段落，我觉得有必要将今天所做的提交到仓库中，于是执行git-commit 操作，将索引内容添加到仓库中。
可能一天下来，你对工作树中的许多文档都进行了更新（文档添加、修改、删除），但是我忘记了它们的名字，此时若将所做的全部更新添加到索引中，比较轻省的做法就是：
1 工作树克隆命令，在后文中将会对其详细讲述。
`$ cd project`
`$ git add .`
`$ git commit -a`
... 输入日志信息...
最后这一步-a是通用的方法，我个人比较喜欢使用
git-commit –m “版本信息” –a ，这样就不用对版本文件操作了。
git-add 命令通常能够判断出当前目录（包括其子目录）下用户所添加的新文档，并将其信息追加到索引中。git-commit 命令的-a 选项可将所有被修改的文档或者已删除的文档的当前状态提交倒仓库中。记住，如果只是修改或者删除了已被Git 管理的文档，是没必要使用git-add 命令的。
本节并未讲述新的Git 命令，完全是前面所讲过的一些命令的重复介绍，只是它们出现的场景有所区别而已。另外，要注意的问题是，Git 不会主动记录你对文档进行的更新，除非你对它发号施令。

## 1.5 查看版本历史
在工作树中，使用git-log 命令可以查看当前项目的日志，也就是你在使用git-commit 向仓库提交新版本时所属如的版本更新信息。
`$ git log`
如果你想看一下每一次版本的大致变动情况，可使用以下命令：
`$ git log --stat --summary`
下面分析一下git-log 命令的回应信息。如下是我对内核修改后提交的几个版本，版本标记分别为first、second、third ，最下面的那个为原始版本。

每一个版本都对应着一次项目版本更新提交。在项目日志信息中，每条日志的首行（就是那一串莫名奇妙的数字）为版本更新提交所进行的命名，我们可以将该命名 理解为项目版本号。项目版本号应该是唯一的，默认由Git 自动生成，用以标示项目的某一次更新。如果我们将项目版本号用作git-show 命令的参数，即可查看该次项目版本的更新细节：
`$ git show `版本号（比较长我就不输了）
除了使用完整的版本号查看项目版本更新细节之外，也还可以使用以下方式：
`$ git show ddea091 # 一般只使用版本号的前几个字符即可  `
`$ git show HEAD # 显示当前分支的最新版本的更新细节`
每一个项目版本号通常都对应存在一个父版本号，也就是项目的前一次版本状态。可使用如下命令查看当前项目版本的父版本更新细节：
`$ git show HEAD^ # 查看HEAD 的父版本更新细节`
`$ git show HEAD^^ # 查看HEAD 的祖父版本更新细节`
`$ git show HEAD~4 # 查看HEAD 的祖父之祖父的版本更新细节`

## 1.6 撤销与恢复
版本控制系统的一个重要任务就是提供撤销和恢复某一阶段工作的功能。
git-reset 命令就是为这样的任务而准备的，它可以将项目当前版本定位到之前提交的任何版本中。
git-reset 命令有三个选项：--mixed 、--soft 和--hard 。我们在日常使用中仅使用前两个选项；第三个选项由于杀伤力太大，容易损坏项目仓库，需谨慎使用。
--mixed
仅是重置索引的位置，而不改变你的工作树中的任何东西（即，文件中的所有变化都会被保留，也不标记他们为待提交状态），并且提示什么内容还没有被更新了。这个是默认的选项。
--soft
既不触动索引的位置，也不改变工作树中的任何内容，我们只是要求这些内容成为一份好的内容（之后才成为真正的提交内容）。这个选项使你可以将已经提交的东 西重新逆转至“已更新但未提交（Updated but not Check in）”的状态。就像已经执行过 git-update-index 命令，但是还没有执行 git-commit 命令一样。
--hard
将工作树中的内容和头索引都切换至指定的版本位置中，也就是说自 <commit-ish> 之后的所有的跟踪内容和工作树中的内容都会全部丢失。因此，这个选项要慎用，除非你已经非常确定你的确不想再看到那些东西了。关于git-reset 命令的具体如何使用可留作本章的练习题，你可以随便创建一个Git 仓库并向其提交一些版本更新，然后测试--mixed 与--soft 选项的效果。
如果欲查看git-reset 命令对工作树的影响，可使用git-status 命令。这是我们工作中的重点和难点！

## 1.7 Git命令详解
分支管理：git-branch
直至现在为止，我们的项目版本库一直都是只有一个分支 master。在 git 版本库中创建分支的成本几乎为零，所以不必吝啬多创建几个分支。下面列举一些常见的分支策略，仅供大家参考：
创建一个属于自己的个人工作分支，以避免对主分支 master 造成太多的干扰，也方便与他人交流协作。
当进行高风险的工作时，创建一个试验性的分支，扔掉一个烂摊子总比收拾一个烂摊子好得多。
合并别人的工作的时候，最好是创建一个临时的分支，关于如何用临时分支合并别人的工作的技巧，将会在后面讲述。
创建分支
下面的命令将创建我自己的工作分支，名叫 litary，并且将以后的工作转移到这个分支上开展。
`$ git-branch litary`
`$ git-checkout litary`
删除分支
要删除版本库中的某个分支，使用 git-branch -D 命令就可以了，例如： 
`$ git-branch -D branch-name`
查看分支
运行下面的命令可以得到你当前工作目录的分支列表：
`$ git-branch`
输出的分支中前面带*的就是你现在所在的分支，如果你忘记了你现在工作在哪个分支上，可以这样查看，而且运行下面的命令也可以告诉你：
`$ cat .git/HEAD`
查看项目的发展变化和比较差异
这一节介绍几个查看项目的版本库的发展变化以及比较差异的很有用的命令：
`git-show-branch`
`git-diff`
`git-whatchanged`
`git-show-branch` 命令可以使我们看到版本库中每个分支的世系发展状态，并且可以看到每次提交的内容是否已进入每个分支。让我们看到版本库的发展记录。
譬如我们要查看世系标号为 master^ 和 litary 的版本的差异情况，我们可以使用这样的命令： $ git-diff master^ litary
合并两个分支：git-merge
既然我们为项目创建了不同的分支，那么我们就要经常地将自己或者是别人在一个分支上的工作合并到其他的分支上去。现在我们看看怎么将 litary 分支上的工作合并到 master 分支中。现在转移我们当前的工作分支到 master，并且将 litary 分支上的工作合并进来。
`$ git-checkout master`
`$ git-merge` "Merge work in litary" HEAD litary合并两个分支，还有一个更简便的方式，下面的命令和上面的命令是等价的。
`$ git-checkout master`
`$ git-pull . litary`
但是，此时 git 会出现合并冲突提示，就要根据具体的情况和需求对它修改。


## 参考：

1.显示服务器版本
`cat /etc/redhat-release`
`#CentOS release 6.4 (Final)`

`ipconfig`
#服务器IP192.168.1.225 域名www.domain.com  SSH端口8200(默认为22)


2.安装git
`yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel perl-devel`

#下载git-1.8.2.2.tar.gz 到 /usr/local/src 下载网址http://code.google.com/p/git-core
```
cd /usr/local/src
tar -zvxf git-1.8.2.2.tar.gz
cd git-1.8.2.2
make prefix=/usr/local/git all
make prefix=/usr/local/git install
#增加软连接
ln -s /usr/local/git/bin/* /usr/bin/
git --version
#如何能显示版本号，即表示成功
```

3.安装gitosis
```
yum install python python-setuptools
cd /usr/local/src
git clone git://github.com/res0nat0r/gitosis.git
cd gitosis
python setup.py install
#显示Finished processing dependencies for gitosis==0.2即表示成功
```

4.在开发机上,生产密钥并上传到服务器上
```
ssh-keygen -t rsa
#一路回车，不需要设置密码
#上传公钥到服务器(默认SSH端口22)
#scp ~/.ssh/id_rsa.pub root@192.168.1.225:/tmp
#或
#scp ~/.ssh/id_rsa.pub root@www.domain.com:/tmp/
#如修改SSH端口(端口8200)
#git clone ssh://git@192.168.1.225:8200/gitosis-admin.git
#或
#git clone ssh://git@www.domain.com:8200/gitosis-admin.git
```
```
#修改配置文件，可以省略每次输入端口
vim ~/.ssh/config
#修改客户端~/.ssh/config文件，添加以下代码
host www.domain.com
hostname www.domain.com
port 8200
#修改后，客户端即可用以下方式进行连接
#git clone ssh://git@www.domain.com/gitosis-admin.git
```

```
#上传公钥到服务器(修改端口，并在配置中指定端口)
scp ~/.ssh/id_rsa.pub root@www.domain.com:/tmp/
ls /tmp/id_rsa.pub
#显示已经上传的密钥
```
5.服务器上生成git用户，使用git用户并初始化gitosis
```
adduser -m git
su - git
gitosis-init < /tmp/id_rsa.pub
#显示以上信息即表示成功
#Initialized empty Git repository in /home/git/repositories/gitosis-admin.git/
#Reinitialized existing Git repository in /home/git/repositories/gitosis-admin.git/

#删除密钥
su - root
rm -rf /tmp/id_rsa.pub
```

6.在开发机上导出管理
```
mkdir -p /repo
cd /repo
git clone git@www.domain.com:gitosis-admin.git
```

7.增加及设置管理项目
```
cd /repo/gitosis-admin
#查看已经上传密钥
ls keydir
cat keydir/vicowong\@VICO.pub  #vicowong@VICO.pub为已经上传的开发机生成的公密
#显示密钥最后的符串为密钥用户名 这里为vicowong@VICO
vim gitosis.conf

#在文件尾增加以下内容
[group test-git] # 组名称
writable = test-git # 项目名称
members = vicowong@VICO #密钥用户名

#提交修改
git add .
git commit -a -m "add test-git repo"
git push
```


9.初始，增加及使用项目test-git
```
cd /repo
mkdir test-git
cd test-git
git inti
touch readme
git add .
git commit -a -m "init test-git"
git remote add origin git@www.domain.com:test-git.git
git push origin master
```

## 问题总结：

我在上传些代码的时候，有时候会遇到&ldquo;git did not exit cleanly (exit code 128)&rdquo;错误。
通常都是网络原因。
我在上传些代码的时候，有时候会遇到“git did not exit cleanly (exit code 128)”错误。通常都是网络原因。
找了网上解决的方法：
\
1、鼠标右键 -> TortoiseGit -> Settings -> Network
2、SSH client was pointing to C:\Program Files\TortoiseGit\bin\TortoisePlink.exe
3、Changed path to C:\Program Files (x86)\Git\bin\ssh.exe
---------------------- 拖走FM----期待与您交流！ --------
收音机,电台,网上电台,广播,在线广播,网络广播,广播电台,网络电台,在线电台,电台在线收听,广播电台在线收听,网络电台在线收听,在线收听电台,fm收音机,网络收音机,广播下载,在线收音机,收音机软件下载,电台软件下载,网络收音机下载--------------
---------------------- 拖走FM----期待与您交流！ -------- 
