 How-to-get-the-newest-code-from-github.md
 Git如何更新下载到代码到本地
 
方式一
1. 查看远程仓库
```
git remote -v
eoecn   https://github.com/eoecn/android-app.git (fetch)
eoecn   https://github.com/eoecn/android-app.git (push)
origin  https://github.com/com360/android-app.git (fetch)
origin  https://github.com/com360/android-app.git (push)
su@SUCHANGLI /e/eoe_client/android-app (master)
```
从上面的结果可以看出，远程仓库有两个，一个是eoecn，一个是origin
2. 从远程获取最新版本到本地
```
$ git fetch origin master
From https://github.com/com360/android-app
 * branch            master     -> FETCH_HEAD
su@SUCHANGLI /e/eoe_client/android-app (master)
```
$ git fetch origin master 这句的意思是：从远程的origin仓库的master分支下载代码到本地的origin master

3. 比较本地的仓库和远程参考的区别
```
$ git log-p master.. origin/master
su@SUCHANGLI /e/eoe_client/android-app (master)
```
因为我的本地仓库和远程仓库代码相同所以没有其他任何信息

4. 把远程下载下来的代码合并到本地仓库，远程的和本地的合并
```
git merge origin/master
Already up-to-date.
su@SUCHANGLI /e/eoe_client/android-app (master)
```
我的本地参考代码和远程代码相同，所以是Already up-to-date

以上的方式有点不好理解，大家可以使用下面的方式，并且很安全
方式二
1.查看远程分支，和上面的第一步相同
2. 从远程获取最新版本到本地

```
git fetch origin master:temp
From https://github.com/com360/android-app
 * [new branch]      master     -> temp
su@SUCHANGLI /e/eoe_client/android-app (master)
```
git fetch origin master:temp 这句命令的意思是：从远程的origin仓库的master分支下载到本地并新建一个分支temp

    比较本地的仓库和远程参考的区别

$ `git diff temp`
su@SUCHANGLI /e/eoe_client/android-app (master)

命令的意思是：比较master分支和temp分支的不同
由于我的没有区别就没有显示其他信息
4. 合并temp分支到master分支
```
$ git merge temp
merge is not possible because you have unmerged files.
git add .
git stash  
git checkout origin master
git pull origin master
Already up-to-date.
su@SUCHANGLI /e/eoe_client/android-app (master)
```
由于没有区别，所以显示Already up-to-date.
合并的时候可能会出现冲突，有时间了再把如何处理冲突写一篇博客补充上。
5.如果不想要temp分支了，可以删除此分支
$ git branch -d temp
Deleted branch temp (was d6d48cc).
su@SUCHANGLI /e/eoe_client/android-app (master)

如果该分支没有合并到主分支会报错，可以用以下命令强制删除git branch -D <分支名>
总结：方式二更好理解，更安全，对于pull也可以更新代码到本地，相当于fetch+merge，多人写作的话不够安全。

