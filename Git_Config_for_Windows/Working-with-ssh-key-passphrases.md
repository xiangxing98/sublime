# working-with-ssh-key-passphrases.md
# Working with SSH key passphrases
This article will walk you through the process of securing your SSH keys and configuring an authentication agent so that you won't have to re-enter your passphrase every time you use your keys.

## Why do I need a passphrase?

Passwords aren't very secure. If you use one that's easy to remember, it's also easier to guess or brute-force (try many options until one works). If you use one that's random, it's hard to remember, and thus you're more inclined to write it down. Both of these are Very Bad Things.

This is why you're using SSH keys. Of course, using a key without a passphrase is basically the same as writing down a random password: anyone who gains access to your computer has gained access to every system you use that key with. This is also a Very Bad Thing. The solution is to add a passphrase to the SSH key for an extra layer of security.

But I don't want to enter a long passphrase every time I use the key!

Neither do I! Thankfully, there's a nifty little tool called ssh-agent that can securely save your passphrase, so you don't have to re-enter it. If you're on OS X Leopard or later your keys can be saved in the system's keychain to make your life even easier. Most Linux installations will automatically start ssh-agent for you when you log in.

## Adding or changing a passphrase

You can change the passphrase for an existing private key without regenerating the keypair. Just type the following command:

```bash
ssh-keygen -p
# Start the SSH key creation process
# Enter file in which the key is (/Users/you/.ssh/id_rsa): [Hit enter]
# Key has comment '/Users/you/.ssh/id_rsa'
# Enter new passphrase (empty for no passphrase): [Type new passphrase]
# Enter same passphrase again: [One more time for luck]
# Your identification has been saved with the new passphrase.
If your key already has a passphrase, you will be prompted to enter it before you can change to a new passphrase.
```

## 为github帐号添加SSH keys验证
Why?
1. 使用ssh key验证github的好处就是不用每次提交代码的时候都要输入用户名和密码，因为着在一定程度上对效率有很大的影响，虽然这么做可以防止代码提交的次数过多，但这也看个人的习惯吧。
2. 使用git clone命令从github上同步github上的代码库时，如果使用SSH链接（如我自己的sublime项目：git@github.com:xiangxing98/sublime.git），而你的SSH key没有添加到github帐号设置中，系统会报下面的错误：
Permission denied (publickey).
fatal: The remote end hung up unexpectedly
这时需要在本地创建SSH key，然后将生成的SSH key文件内容添加到github帐号上去。

How?
创建SSH key的方法很简单，打开控制台，建一个目录，比如~/.ssh(其实叫什么都无所谓，网上搜的基本上都这么配置),
cd ~/.ssh
#ssh-keygen#生成密钥
#ssh-keygen -t rsa -C "youname@example.com"
ssh-keygen -t rsa -C xiangxing985529@163.com
#注意：双引号换成自己的邮箱，如果遇到权限问题，只需在前面加上sudo
#Generating public/private rsa key pair.
#Enter file in which to save the key (/c/Documents and Settings/Administrator/.ssh/id_rsa): github_ssh_key
#然后系统提示输入文件保存位置等信息，连续敲三次回车即可，生成的SSH key文件保存在中～/.ssh/id_rsa.pub
#这个时候，在.ssh目录下有两个文件
#id_rsa
#id_rsa.pub
#其中id_rsa是私钥 id_rsa.pub是公钥
#然后，执行下面的命令，将生成的key添加
ssh-add id_rsa
#Could not open a connection to your authentication agent.
ssh-agent bash
exit
#后话--刚开始忘记执行ssh-add id_rsa 命令，一直验证不成功，困在这里好久
#然后将id_rsa.pub里面的内容复制下来，在github上的settings里面找到add keys，将其粘贴到key即可，title随便填

#接着拷贝.ssh/id_rsa.pub文件内的所以内容，将它粘帖到github帐号管理中的添加SSH key界面中。
#C:\Documents and Settings\Administrator\.ssh\
#用文本编辑工具打开该文件，我用的是vim,所以命令是：
vim ~/.ssh/id_rsa.pub
yy

##打开github帐号管理中的添加SSH key界面的步骤如下：
1. 登录github
2. 点击右上方的Accounting settings图标
3. 选择 SSH key
4. 点击 Add SSH key
##在出现的界面中填写SSH key的名称，填一个你自己喜欢的名称即可，然后将上面拷贝的~/.ssh/id_rsa.pub文件内容粘帖到key一栏，在点击“add key”按钮就可以了。
##添加过程github会提示你输入一次你的github密码
##添加完成后再次执行git clone就可以成功克隆github上的代码库了。


#测试是否成功
ssh -T git@github.com
#no add publickey
Warning: Permanently added the RSA host key for IP address '192.30.252.129' to t
he list of known hosts.
Permission denied (publickey).
#这个时候可以在控制台上测试一下
ssh -T git@github.com
#Warning: Permanently added the RSA host key for IP address '192.30.252.131' to 
#the list of known hosts.
#Hi xiangxing98! You've successfully authenticated, but GitHub does not provide 
#shell access.


