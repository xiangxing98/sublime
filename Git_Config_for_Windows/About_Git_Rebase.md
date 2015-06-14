# About_Git_Rebase.md
<!-- MarkdownTOC -->

- git rebase introduction
- 那么rebase都做了什么事情呢？

<!-- /MarkdownTOC -->

git show
git reflog show | grep add
git reflog show | grep commit
git reflog show | grep pull
git reflog show | grep 


git for-each-ref --sort=authordate \--format="%(*authordate:iso8601) %(objectname:short) %(refname:short)" \refs/tags/git reflog show | grep pull

git for-each-ref --sort=authordate

git branch

## git rebase introduction
git rebase 是个非常强大灵活的命令，它可以让你对commit进行修改、调整顺序、合并等操作、并能以线性的方式进行分支的合并与嫁接等。

简单来说 rebase 就是把某个分支上的一部分commit嫁接到另一个commit后面，而在这个过程中这些commit的base（基）变了，所以这个操作叫做『变基』。

比如我们有如下的提交历史，当前的分支是 topic ：
```
     A---B---C topic(HEAD)
    /
D---E---F---G master
```
我们执行了如下任何一个命令之后：
```
$ git rebase master
$ git rebase master topic
```
提交历史将会变成如下这样：
```
              A'--B'--C' topic(HEAD)
             /
D---E---F---G master
```
可以看出git把 A---B---C 这段commit嫁接到了 G 之后，不过虽然这些新commit的内容是一样的，但是hash值是不同的（ A'--B'--C' ），原因将在后面解释。

命令完整的形式如下：
```
$ git rebase <upstream> <branch>
```
其中 <upstream> 是新的base，如果你提供 <branch> ，那么首先会checkout到这个 <branch> ，然后再进行rebase操作。所以以下两种方式的区别是第一种形式会首先checkout到topic分支，然后再执行rebase的操作。
```
$ git rebase master topic
$ git rebase master
```

## 那么rebase都做了什么事情呢？

首先，git会对topic分支和 <upstream> 做一个差集，把不同的commit找出来，类似于执行`git log <upstream>..HEAD` ，对于以上例子来说结果就是 A---B---C ，然后把这些commit存在一个临时的地方。

其次，git会把当前分支reset到 <upstream> 上，类似于执行 `git reset --hard <upstream>`命令。对于以上例子来说就是reset到 master 。

最后，git把第一步中暂存的commit，按照顺序一个一个地应用到分支上，相当于一个一个重复提交，这就是为什么rebase之后commit的hash值变了。

如果 中的一个commit进行了某项修改，而当前分支中也存在一个commit，这两个commit的修改的内容一样，那么当前分支中的commit将会被忽略。比如以下的 A 和 A' 就是这样两个commit。
```
          A---B---C topic
         /
    D---E---A'---F master
```
执行完git rebase master之后，结果如下：
```
               B'---C' topic
              /
D---E---A'---F master        
```
如果你想更灵活的进行commit嫁接，那么你需要 rebase --onto ，命令格式如下：
```
$ git rebase --onto <newbase> <upstream> <branch>
```
假设你有如下的branch tree：
```
o---o---o---o---o  master
         \
          o---o---o---o---o  next
                           \
                            o---o---o  topic
```
你想要得到如下的branch tree：
```
o---o---o---o---o  master
        |            \
        |             o'--o'--o'  topic
         \
          o---o---o---o---o  next
```
那我们需要如下操作：
```
$ git rebase --onto master next topic
```
这个操作会把从 next 开始的commit嫁接到 master 上。如果你提供 <branch> ，那么首先会checkout到这个 <branch> ，然后再进行rebase操作。

我们再看一个例子，比如我们有如下的branch tree：
```
E---F---G---H---I---J  topicA
```
我们想要删除 F---G 这两个commit，那么通过 rebase --onto 就可以实现：
```
$ git rebase --onto topicA~5 topicA~3 topicA
```
执行结果是：
```
E---H'---I'---J'  topicA
```
同样，rebase也会产生冲突，当解决完冲突之后你可以继续rebase的进程：
```
$ git rebase --continue
```
或者取消此次rebase：
```
$ git rebase --abort
```
关于commit修改、顺序调整、合并等操作可以通过 rebase -i 来完成
```
$ git rebase -i <upstream>
```
chitsaou写的 [《Git-rebase 小筆記》]( http://blog.yorkxin.org/posts/2011/07/29/git-rebase/)中有详细的介绍，可以自行查看。
参考
(完) 
