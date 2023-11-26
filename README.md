# LALA

This a just to learn how writing a package works.


## Create the directory structure


## what goes into the tomlfile thing


## connect to remote (github)

we call that repository __origin__


## delete local stuff completely

then: `git clone https://github.com/okoham/lalaproject.git` re-creates that stuff into the folder `lalaproject`


## usual stuff when I do changes
- `git add <filename>`
- `git commit -m "great description"`
- `git push origin main`


## renaming branch from master to main

- To rename the current branch: `git branch -m <newname>`
- To rename a branch while pointed to any branch: `git branch -m <oldname> <newname>`
- To push the local branch and reset the upstream branch: `git push origin -u <newname>`
- To delete the remote branch: `git push origin --delete <oldname>`
- To create a git rename alias: `git config --global alias.rename 'branch -m'`

## delete branches

- local: `git branch -d <branch_name>`
- remote: `git push <remote_name> --delete <branch_name>`

## installation

- intall: `pip install git+https://github.com/okoham/lalaproject.git``
- uninstall: `pip uninstall lala`