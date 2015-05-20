# Avoid Input User.Name and User.Email when push to Github
Git Push 避免用户名和密码方法

## 前言
在大家使用github的过程中，一定会碰到这样一种情况，就是每次要push 和pull时总是要输入github的账号和密码，这样不仅浪费了大量的时间且降低了工作效率。在此背景下，本文在网上找了两种方法来避免这种状况，这些成果也是先人提出来的，在此只是做个总结。

## 1.方法一 
### 1.1 创建文件存储GIT用户名和密码
在%HOME%目录中，一般为C:\users\Administrator，也可以是你自己创建的系统用户名目录，反正都在C:\users\中。
文件名为.git-credentials,由于在Window中不允许直接创建以"."开头的文件，所以需要借助git bash进行.
打开git bash客户端，进行%HOME%目录，然后用touch创建文件 .git-credentials, 用vim编辑此文件，输入内容格式：
cd /c/Documents\ and\ Settings//Administrator/
touch .git-credentials
vim .git-credentials
https://{username}:{password}@github.com

### 1.2 添加Git Config 内容
进入git bash终端， 输入如下命令：
git config --global credential.helper store
执行完后查看%HOME%目录下的.gitconfig文件，会多了一项：
[credential]

    helper = store
重新开启git bash会发现git push时不用再输入用户名和密码

## 2.方法二
### 2.1 添加环境变量
在windows中添加一个HOME环境变量，变量名:HOME,变量值：%USERPROFILE%
%USERPROFILE% XP下的路径一般为： C:\Documents and Settings\Administrator
在Bash下的路径： /c/Documents\ and\ Settings//Administrator/
### 2.2 创建git用户名和密码存储文件
进入%HOME%目录，新建一个名为"_netrc"的文件，
cd /c/Documents\ and\ Settings//Administrator/
touch _netrc
vim _netrc
##文件中内容格式如下：
machine {git account name}.github.com
login your-usernmae
password your-password
##重新打开git bash即可，无需再输入用户名和密码

##我已经在github中添加了ssh 密匙了，也在本地有一个SSH密匙，但是还是必须输入密码。
关键是你用了https，它不走ssh 通道,所以key都没用了，
https 保存密码 可以参考[http://git.oschina.net/oschina/git-osc/issues/2586]，
如果要ssh+key 无需密码提交，远程分支需要是ssh协议的 git@github.com:xx/xx.git
push的时候输入密码是很正常的，你可以采用一些措施省略该步骤：
## .git/config
在版本库的SSH方式和HTTPS方式是不同的，具体来说就是url信息的不同，但是，实际的认证机制也是不同的。
当建立了本机密钥之后，使用ssh方式实际上是不需要再次认证的，而https则每次需要输入密码 。
《Help.GitHub - SSH key passphrases》里也说了用SSH更方便更安全，不需要去输入长长的密码。

我去看了下repo目录下的.git/config，果然，我的url是HTTPS形式。
[remote "origin"]  
fetch = + refs/heads/*:refs/remotes/origin/*
url = https://username@github.com/username/projectname.git
*/使用SSH而不是https链接，为了使用SSH公钥的方式认证，我把config的url改成下面这样
[remote "origin"]  
fetch = + refs/heads/*:refs/remotes/origin/*  
url = git@github.com:xiangxing98/sublime.git

*/这样我git push的时候又可以用SSH公钥认证而不用去输入用户名和密码，不仅方便，而且更安全。
在Github里添加你的SSH公钥

## 为github帐号添加SSH keys




.gitignore的路径是相对repo本身的.