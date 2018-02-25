# 343-HW1
This file contains a list of useful git commands, as well as some flags that can be used, and a description of each command/flag. For reference, the commands described here can be found in the [gitHub tutorial](https://try.github.io/)
```
git init 
```
__Creates and initialize a new git repository__
```
git status 
```
__Checks the status of the current repository__
```
git add <target>
```
__Adds a file to the staging area; from there, the file is ready to be committed__
```
git commit 
```
__Adds the files in the staging area to the current git repository.__

__-m "message": flag to add a message when committing, like a brief explanation of what the files changed.
log: print all the changes committed so far__
```
git remote add <target> <repository_URL>
```
__Adds a remote repository from <repository_URL> to the git repository; the remote repository will be named \<target>__
```
git push <pushTo_repo> <pushFrom_repo>
```
__Put the commits from one repository to the other, usually from a local repository to a remote one; in this case, we can think the command as "push <remote_repo> <local_repo>"__

__-u: save the parameters, to remember the local and remote repo in the future.__
```
git pull <pullFrom_repo> <pullTo_repo>
```
__The command copies all the changes committed in the <pullFrom_repo> in your own repo <pullTo_repo>; often the repo you are pulling from will be a remote repo where other have access to and can commit changes.__
```
git diff <pointer>
```
__The command shows a list with the differences between the commit, indicated by the pointer \<pointer>, and the commit before that. the pointer can be HEAD, which is our last commit, or a different commit in time.__
```
git diff --staged
```
__Shows the changes between the file(s) currently in the repo and the staged file(s).__
```
git reset <target>
```
__Resets the specified file(s) from the staging area, meaning that the specified files will be deleted from the staging area _only_.__
```
git checkout -- <target>
```
__Resets all the changes to the \<target> file since the last commit. Important to notice the space between the '--' and \<target>.__
```
git branch <branch_name>
```
__Creates a new branch with name "branch_name".__

__-d: flag used to delete a branch, it won't work on a branch that has not been merged.__

__-f: force the previous flag on the branch, for example force the branch to be deleted even if it has not been merged.__

__-D: flag that unite -d and -f in one command, using only one flag to delete a branch that has not been merged.__
```
git checkout <branch_target>
```
__Switchs branch from the current one to the <branch_target>.__
```
git rm <target>
```
__Removes the file(s) from the disk, and put the removal of the file(s) into the staging area for your git branch. note that to remove the files from the branch/repository definitely, you will have to commit the changes.__

__-r: recursive flag, used to remove a directory and all the files in it.__
```
git merge <origin>
```
__Merge the \<origin> branch into your master (main) branch.__
