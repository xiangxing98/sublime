# git-bash-completion

## 0.切换到当前用户下的一个临时目录
cd ～/tmp
#/home/siqin/Documents/sublime/Git_Config_for_Windows/

## 1. github下载或者从源码中得到git-completion.bash， Download or copy git-completion.bash
1.1 从github下载git-completion.bash
https://github.com/markgandolfo/git-bash-completion.git
git clone https://github.com/git/git
1.2  从Git 的安装文件拷贝git-completion.bash
#cd git/contrib/completion/
cd /usr/share/doc/git-1.7.1/contrib/completion/

## 2. copy到用户根目录~/ 或者/etc/bash_completion.d/下
cp git-completion.bash ~/.git-completion.bash
#Copy to /etc/bash_completion.d/
#cp contrib/completion/git-completion.bash /etc/bash_completion.d/
#cp git/contrib/completion/git-completion.bash ~/.git-completion.bash
#cp git-completion.bash /etc/bash_completion.d/git-completion.bash

## 3. Make it effective加载使之生效(放在/etc/bash_completion.d/下加载后自动生效)
source ~/.git-completion.bash
#source /etc/bash_completion.d/git-completion.bash

## 4. 编辑~/.bashrc，加入source ~/.git-completion.bash
cd ~/
vi ~/.bashrc
#gedit ~/.bashrc
#在文件的最后加入下面内容
source ~/.git-completion.bash

#完成以上步骤后，重启shell，今后输入git命令时，就可以通过tab键自动补全命令了

