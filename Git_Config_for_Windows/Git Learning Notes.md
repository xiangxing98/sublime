# Git Learning Notes
2015-05-21 08:54:38  Collected and Modified By siqin.hou@gmail.com

--------------------------------------------------------------------------------
## Git Related People & Resourses
http://zachholman.com/
Git参考手册
Git简明手册
Git Magic
Git Community Book 中文版
Pro Git
图解Git
git-简明指南
learnGitBranching
## 参考网站
[1]	http://git-scm.com/
[2]	https://github.com/
[3]	ISBN：9787111349679, 由机械工业出版社华章公司于2011年7月出版。
[4]	http://book.git-scm.com/
[5]	http://progit.org/book/
[6] https://gist.github.com/
http://higrid.net/hi/docs/free-programming-books
http://zachholman.com/talk/how-github-uses-github-to-build-github/
http://yanxyz.github.io/emmet-docs/
http://gitbeijing.com/
http://www.worldhello.net/gotgithub/index.html
http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000
[Git Book](http://git-scm.com/book/zh/v1)
[Install Git-GUI]http://msysgit.github.io/

--------------------------------------------------------------------------------
## 配置-首先是配置帐号信息-git config 
pwd #查看present working directory
cd /o/ #take care Windows XP directory in Git is different
mkdir sublime #make project directory and change directory to that dir
cd /o/sublime
git config --global user.name xiangxing98
git config --global user.email xiangxing985529@163.com
#查看所有配置的信息
git config --list
#获取config帮助信息
git help config 

#编辑器配置
#To colorize git’s output for increased readability:
git config --global color.ui true
#To create a git s alias, can use git s to show status
git config --global alias.s "status -s"
#To create a git lg alias, use git lg to show log
git config --global alias.lg "log --oneline --decorate --all --graph"
git config --global alias.plog "log --pretty=fuller"

#配置自动换行-自动转换坑太大,提交到git是自动将换行符转换为lf
#To configure line endings correctly on Linux/Mac:
git config --global core.autocrlf input
#To configure line endings correctly on Windows:
git config --global core.autocrlf true

#To check your current username:
git config --global user.name
#To set your username:
git config --global user.name "xiangxing98"
#To check your email:
git config --global user.email
#To set your email:
git config --global user.email xiangxing985529@163.com
#To limit pushes to your current branch:
git config --global push.default simple
#To default all new branches to fetch and rebase - not merge:
git config --global branch.autosetuprebase always
#To record any merge conflict resolutions and reuse them automatically:
git config --global rerere.enabled true

--------------------------------------------------------------------------------
## 配置密钥
#C:\Documents and Settings\Administrator\.ssh\
cd ~/.ssh
ssh-keygen -t rsa -C xiangxing985529@163.com #生成密钥
#这个时候，在.ssh目录下有两个文件
#id_rsa id_rsa.pub, #其中id_rsa是私钥 id_rsa.pub是公钥
ssh-add id_rsa
#Could not open a connection to your authentication agent.
ssh-agent bash
exit
#接着拷贝.ssh/id_rsa.pub文件内的所以内容，将它粘帖到github帐号管理中的添加SSH key界面中。
#Linux Copy command
cat ~/.ssh/id_rsa.pub | pbcopy
#1. 登录github
#2. 点击右上方的Accounting settings图标
#3. 选择 SSH key
#4. 点击 Add SSH key
#测试是否成功
ssh -T git@github.com 
#Hi xiangxing98! You've successfully authenticated, but GitHub does not provide 
#shell access.

--------------------------------------------------------------------------------
## Create a new repository from scratch on the command line-GIT Bash Windows XP
cd /E/Github/
mkdir WebApp
cd WebApp
touch README.md
echo "#WebApp on Github Test/n/n## Just a Test" >> README.md
#Change New Line -e, >> out put to README.md
echo -e "#R-Programming\n\n##Line 2-Just a Test.\n##Line 3" >> README.md
## echo 
##功能说明：显示文字。 
##语法：echo [-ne][字符串]或 echo [--help][--version] 
##参数：-n 不要在最后自动换行 -e 若字符串中出现以下字符，
##则特别加以处理，而不会将它当成一般文字输出：
##\a 发出警告声； \b 删除前一个字符； \c 最后不加上换行符号； 
##\f 换行但光标仍旧停留在原来的位置； \n 换行且光标移至行首； 
##\r 光标移至行首，但不换行； \t 插入tab； \v 与\f相同；
git init #初始化
git status #获取状态
git add fileName #.或*代表全部添加git add ., git add README.md
git commit -m "Write Something Commit Message" #此处注意乱码 git commit -m "CommitMessage--My first commit"
git remote add origin git@github.com:xiangxing98/sublime.git #添加远程源ssh协议, 建议
git remote add origin https://github.com/xiangxing98/sublime.git #https protocol
#git remote add origin https://github.com/xiangxing98/R-Programming.git
git push -u origin master #push同时设置默认跟踪分支

--------------------------------------------------------------------------------
# Clone a repository from Github 从现有仓库克隆
git clone git://github.com/yanhaijing/data.js.git
git clone git@github.com:xiangxing98/sublime.git
#克隆到自定义文件夹
git clone git://github.com/xiangxing98/sublime.git mypro 
git clone https://github.com/xiangxing98/learn_git.git
#拉取最新的远程版本
git pull https://github.com/xiangxing98/sublime.git
git pull origin gh-pages

--------------------------------------------------------------------------------
## 0. Work On Local Repository 本地操作
git add *#跟踪新文件
rm *&git rm *#移除文件
git rm -f *#移除文件
git rm --cached *#取消跟踪
git mv file_from file_to#重命名跟踪文件
git log#查看提交记录
git log --pretty=fuller
git commit#提交更新
git commit -m 'message'
git commit -a#跳过使用暂存区域，把所有已经跟踪过的文件暂存起来一并提交
git commit --amend#修改最后一次提交
git reset HEAD *#取消已经暂存的文件
git checkout -- file#取消对文件的修改（从暂存区去除file）
git checkout branch|tag|commit -- file_name#从仓库取出file覆盖当前分支
git checkout -- .#从暂存区去除文件覆盖工作区

--------------------------------------------------------------------------------
## 1. 远程仓库相关命令-远端，源remote
#git是一个分布式代码管理工具，可以支持多个仓库.服务器上的仓库在本地称为remote。
#个人开发时，多源用的可能不多，但多源其实非常有用。
# push an existing repository from the command line
#1st Band the remote using ssh protocol-recommended
git remote add origin git@github.com:xiangxing98/R-Programming.git
git remote add origin git@github.com:xiangxing98/sublime.git
#https protocol
git remote add origin https://github.com/xiangxing98/R-Programming.git
#2nd push and set default track branch
git push -u origin master

#检出仓库：
git clone git://github.com/jquery/jquery.git
#查看远程仓库源remote：
git remote #显示全部远程仓库源
git remote -v #显示全部远程仓库源+详细信息
git remote show origin1#查看指定源的全部信息
#添加远程仓库源：
git remote add [name] [url]
#删除远程仓库源, 删除origin1 git remote rm origin1
git remote rm [name]
#修改远程仓库源：
git remote set-url --push [name] [newUrl]
#重命名远程仓库remote
git remote rename origin1 origin2#重命名
#拉取远程仓库源：
git pull [remoteName] [localBranchName]
#推送远程仓库源：
git push [remoteName] [localBranchName]
#*如果想把本地的某个分支test提交到远程仓库，并作为远程仓库的master分支，
#或者作为另外一个名叫test的分支，如下：
#// 提交本地test分支作为远程的master分支
git push origin test:master
#// 提交本地test分支作为远程的test分支
git push origin test:test

## 2. 分支(branch)操作相关命令
## 分支branch
git branch #查看,列出本地分支
git branch -r #列出远端分支
git branch -a #列出所有分支
git branch -v #查看各个分支最后一个提交对象的信息
git branch --merge #查看已经合并到当前分支的分支
git branch --no-merge #查看为合并到当前分支的分支
git branch [name] #创建本地分支---注意新分支创建后不会自动切换为当前分支
git branch test #新建test分支
git checkout test #切换到test分支 git checkout [name]
git checkout -b test #新建+切换到test分支 git checkout -b [name]
git checkout -b test dev #基于dev新建test分支，并切换
git branch -d test #删除test分支
#git branch -d [name]
#-d选项只能删除已经参与了合并的分支，对于未有合并的分支是无法删除的。
#如果想强制删除一个分支，可以使用-D选项
git branch -D test #强制删除test分支
git merge test #将test分支合并到当前分支
#合并分支：git merge [name]#将名称为[name]的分支与当前分支合并
git rebase master #将master分之上超前的提交，变基到当前分支
git fetch originname branchname#拉取远端上指定分支
git merge originname branchname#合并远端上指定分支
git push originname branchname#推送到远端上指定分支
#创建远程分支(本地分支push到远程)：git push origin [name]
git push -u origin master
git push originname localbranch:serverbranch#推送到远端上指定分支
git checkout -b test origin/dev#基于远端dev新建test分支
#删除远程分支：
git push origin :heads/[name] 
#或删除远程分支
git push origin :[name] 
#*创建空的分支：(执行命令之前记得先提交你当前分支的修改，否则会被强制删干净没得后悔)
$git symbolic-ref HEAD refs/heads/[name]
$rm .git/index
$git clean -fdx
#http://www.juvenxu.com/2010/11/28/a-successful-git-branching-model/

# Merging Branch via command line
#If you do not want to use the merge button or an automatic merge cannot be performed, 
#you can perform a manual merge on the command line.
`git://github.com/xiangxing98/sublime.git`
#Step 1: From your project repository, bring in the changes and test.
```bash
git fetch origin
git checkout -b TestBranch origin/TestBranch
git merge master
```
#Step 2: Merge the changes and update on GitHub.
```bash
git checkout master
git merge --no-ff TestBranch
git push origin master
```

## 3. 版本标签(tag)操作相关命令
#当开发到一定阶段时，给程序打标签是非常棒的功能。
#查看创建版本
git tag #列出现有标签,查看版本
git tag v0.1 #新建标签,创建版本git tag [name]
git tag -a v0.1 -m 'my version 1.4'#新建带注释标签git tag -a [name] -m 'yourMessage'
git checkout tagname#切换到标签
#远程版本标签
git tag -r #查看远程版本
git push origin [name] #创建远程版本-本地版本push到远程
git push origin v1.5#推送分支到源上
git push origin --tags#一次性推送所有分支,上传本地tag到远程仓库
git pull origin --tags #合并远程仓库的tag到本地
#删除版本
git tag -d v0.1#删除版本,删除标签git tag -d [name]
git push origin :refs/tags/v0.1#删除远程标签版本 git push origin :refs/tags/[name]

## 4. 子模块(submodule)相关操作命令
#添加子模块：
git submodule add [url] [path]
#如：
git submodule add git://github.com/soberh/ui-libs.git src/main/webapp/ui-libs
#初始化子模块,只在首次检出仓库时运行一次就行
git submodule init
#更新子模块, 每次更新或切换分支后都需要运行一下
git submodule update
#删除子模块,分4步走
#1) 
git rm --cached [path]
#2) 编辑“.gitmodules”文件，将子模块的相关配置节点删除掉
#3) 编辑“ .git/config”文件，将子模块的相关配置节点删除掉
#4) 手动删除子模块残留的目录

## 5. 忽略一些文件、文件夹不提交
#在仓库根目录下创建名称为“.gitignore”的文件，
#写入不需要的文件夹名或文件，每个元素占一行即可，如
touch .gitignore
#Change New Line -e, >> out put to .gitignore
echo -e "target\nbin\n*.db" >> .gitignore
cat .gitignore
target
bin
*.db



=====================
## Git 常用命令
git branch 查看本地所有分支
git status 查看当前状态
git commit 提交
git branch -a 查看所有的分支
git branch -r 查看本地所有分支
git commit -am "init" 提交并且加注释
git remote add origin git@192.168.1.119:ndshow
git push origin master 将文件给推到服务器上
git remote show origin 显示远程库origin里的资源
git push origin master:develop
git push origin master:hb-dev 将本地库与服务器上的库进行关联
git checkout --track origin/dev 切换到远程dev分支
git branch -D master develop 删除本地库develop
git checkout -b dev 建立一个新的本地分支dev
git merge origin/dev 将分支dev与当前分支进行合并
git checkout dev 切换到本地dev分支
git remote show 查看远程库
git add .
git rm 文件名(包括路径) 从git中删除指定文件
git clone git://github.com/schacon/grit.git 从服务器上将代码给拉下来
git config --list 看所有用户
git ls-files 看已经被提交的
git rm [file name] 删除一个文件
git commit -a 提交当前repos的所有的改变
git add [file name] 添加一个文件到git index
git commit -v 当你用－v参数的时候可以看commit的差异
git commit -m "This is the message describing the commit" 添加commit信息
git commit -a -a是代表add，把所有的change加到git index里然后再commit
git commit -a -v 一般提交命令
git log 看你commit的日志
git diff 查看尚未暂存的更新
git rm a.a 移除文件(从暂存区和工作区中删除)
git rm --cached a.a 移除文件(只从暂存区中删除)
git commit -m "remove" 移除文件(从Git中删除)
git rm -f a.a 强行移除修改后文件(从暂存区和工作区中删除)
git diff --cached 或 
git diff --staged 查看尚未提交的更新
git stash push 将文件给push到一个临时空间中
git stash pop 将文件从临时空间pop下来
---------------------------------------------------------
git remote add origin git@github.com:username/Hello-World.git
git push origin master 将本地项目给提交到服务器中
-----------------------------------------------------------
git pull 本地与服务器端同步
-----------------------------------------------------------------
git push (远程仓库名) (分支名) 将本地分支推送到服务器上去。
git push origin serverfix:awesomebranch
------------------------------------------------------------------
git fetch 相当于是从远程获取最新版本到本地，不会自动merge
git commit -a -m "log_message" (-a是提交所有改动，-m是加入log信息) 本地修改同步至服务器端 ：
git branch branch_0.1 master 从主分支master创建branch_0.1分支
git branch -m branch_0.1 branch_1.0 将branch_0.1重命名为branch_1.0
git checkout branch_1.0/master 切换到branch_1.0/master分支
du -hs
-----------------------------------------------------------







--------------------------------------------------------------------------------
## Git Help, Commands and Guides
git
git help
git help -a
git help -g
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p|--paginate|--no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
The most commonly used git commands are:
add        Add file contents to the index
bisect     Find by binary search the change that introduced a bug
branch     List, create, or delete branches
checkout   Checkout a branch or paths to the working tree
clone      Clone a repository into a new directory
commit     Record changes to the repository
diff       Show changes between commits, commit and working tree, etc
fetch      Download objects and refs from another repository
grep       Print lines matching a pattern
init       Create an empty Git repository or reinitialize an existing one
log        Show commit logs
merge      Join two or more development histories together
mv         Move or rename a file, a directory, or a symlink
pull       Fetch from and integrate with another repository or a local branch
push       Update remote refs along with associated objects
rebase     Forward-port local commits to the updated upstream head
reset      Reset current HEAD to the specified state
rm         Remove files from the working tree and from the index
show       Show various types of objects
status     Show the working tree status
tag        Create, list, delete or verify a tag object signed with GPG
> 'git help -a' and 'git help -g' lists available subcommands and some
> concept guides. See 'git help <command>' or 'git help <concept>'
> to read about a specific subcommand or concept.
## Git Available Commands
git help -a
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p|--paginate|--no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
available git commands in 'E:\Program Files\Git/libexec/git-core'
add                 get-tar-commit-id   receive-pack
add--interactive    grep                reflog
am                  gui                 relink
annotate            gui--askpass        remote
apply               gui--askyesno       remote-ext
archive             gui.tcl             remote-fd
bisect              hash-object         remote-ftp
bisect--helper      help                remote-ftps
blame               http-backend        remote-http
branch              http-fetch          remote-https
bundle              http-push           remote-testsvn
cat-file            imap-send           repack
check-attr          index-pack          replace
check-ignore        init                request-pull
check-mailmap       init-db             rerere
check-ref-format    log                 reset
checkout            ls-files            rev-list
checkout-index      ls-remote           rev-parse
cherry              ls-tree             revert
cherry-pick         mailinfo            rm
citool              mailsplit           send-email
clean               merge               send-pack
clone               merge-base          sh-i18n--envsubst
column              merge-file          shortlog
commit              merge-index         show
commit-tree         merge-octopus       show-branch
config              merge-one-file      show-index
count-objects       merge-ours          show-ref
credential          merge-recursive     stage
credential-store    merge-resolve       stash
credential-wincred  merge-subtree       status
daemon              merge-tree          stripspace
describe            mergetool           submodule
diff                mktag               subtree
diff-files          mktree              svn
diff-index          mv                  symbolic-ref
diff-tree           name-rev            tag
difftool            notes               unpack-file
difftool--helper    p4                  unpack-objects
fast-export         pack-objects        update-index
fast-import         pack-redundant      update-ref
fetch               pack-refs           update-server-info
fetch-pack          patch-id            upload-archive
filter-branch       prune               upload-pack
fmt-merge-msg       prune-packed        var
for-each-ref        pull                verify-pack
format-patch        push                verify-tag
fsck                quiltimport         web--browse
fsck-objects        read-tree           whatchanged
gc                  rebase              write-tree
'git help -a' and 'git help -g' lists available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.

## The Common Git Guides
git help -g
The common Git guides are:
attributes   Defining attributes per path
glossary     A Git glossary
ignore       Specifies intentionally untracked files to ignore
modules      Defining submodule properties
revisions    Specifying revisions and ranges for Git
tutorial     A tutorial introduction to Git (for version 1.5.1 or newer)
workflows    An overview of recommended workflows with Git
'git help -a' and 'git help -g' lists available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
#Show HTML Git guides
git help ignore
Launching default browser to display HTML ...