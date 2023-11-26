# LALA

This a just to learn how writing a package works.


## Create the directory structure


## what goes into the tomlfile thing


## connect to remote (github)


## renaming branch from master to main

- To rename the current branch: `git branch -m <newname>`
- To rename a branch while pointed to any branch: `git branch -m <oldname> <newname>`
- To push the local branch and reset the upstream branch: `git push origin -u <newname>`
- To delete the remote branch: `git push origin --delete <oldname>`
- To create a git rename alias: `git config --global alias.rename 'branch -m'`

## installation

- intall: `pip install git+https://github.com/okoham/lalaproject.git``
- uninstall: `pip uninstall lala`