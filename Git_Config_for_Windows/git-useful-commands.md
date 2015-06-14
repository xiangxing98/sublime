# git-useful-commands.md
http://eddumelendez.github.io/blog/2016/06/01/git-useful-commands/?utm_source=tuicool

Git is the most popular Version Control System at this time. There are several benefits like Distributed Version Control System, manage commits by references, save space and so on. And to be honest make my job easy in the software development.

In this post I will share some git useful commands.
## View cool log

Sometimes we don’t need to much detail in our log and it is enough reading the commit’s title. Also we would like to know ref names of commits. Additionally, we would like to display branching graph.

git log --oneline --decorate --graph

As a result, you can see the commit hash towards to the commit’s title. Also, you can see branches graph.

## View pending commits to push

Sometimes, I thought that have been sent my commits to the central repository. An easy way to know how many commits are in your local repository and ready to push them is with the command below.

git log --oneline origin/master.. master

## Rebase

Put your local commits to the top and pull all the changes in the repository avoiding conflicts with the central repository.

git pull --rebase origin master

You can also rebase in interactive mode, which allow to choose actions like pick , reword , edit , squash , fixup , exec . To know about this command check this link .

git rebase -i origin/master

## Push specific commit

If you have one pending commit and start in a new feature you maybe wondering how to push your commit without revert all the changes you started. You just need the commit hash and execute the command below.

git push origin hash:master

## Get commit from another branch

Imagine you are working in a new feature with your team in a different branch than master. Then, a team member add a cool functionality which will be util in production right now. You can not wait and want to deploy this functionality in production tonight.

Using the command below you just need to know the commit hash and all changes in that commit will be copy in your current branch. Awesome, isn’t it?

git cherry-pick hash

## Amend

Every day, as a developers we are introducing new code. After few changes we can save our work, but, wait!!! It’s not the end we need to do more changes to finish the feature. Git add amend which allow us to override the last commit. NOTE: which has not been pushed to the central repository.

git commit --amend --reuse-message=HEAD

## Building git command alias

All commands mentioned above can be too large or complex to remember them but you can use alias to give a easy name for you.

Command below will store log --oneline --decorate --graph in the alias logd

git config --global alias.lodg `log --oneline --decorate --graph`

After setup your new alias. You can use git lodg instead git log --oneline --decorate --graph and the result will be the same.
