# LALA

This a just to learn how writing a package works.

## Git and Github

### Create the directory structure


### what goes into the tomlfile thing


### connect to remote (github)

we call that repository __origin__


### delete local stuff completely

then: `git clone https://github.com/okoham/lalaproject.git` re-creates that stuff into the folder `lalaproject`


### usual stuff when I do changes
- `git add <filename>`
- `git commit -m "great description"`
- `git push origin main`


### renaming branch from master to main

- To rename the current branch: `git branch -m <newname>`
- To rename a branch while pointed to any branch: `git branch -m <oldname> <newname>`
- To push the local branch and reset the upstream branch: `git push origin -u <newname>`
- To delete the remote branch: `git push origin --delete <oldname>`
- To create a git rename alias: `git config --global alias.rename 'branch -m'`

### delete branches

- local: `git branch -d <branch_name>`
- remote: `git push <remote_name> --delete <branch_name>`

## installation

- intall from github repo: `pip install git+https://github.com/okoham/lalaproject.git`
- install from local directory: `pip install /opt/mypackage`
- uninstall: `pip uninstall lala`

TODO: 
- build stuff locally (as wheel or so, run from directory where `pyproject.toml` lives): `py -m build`
- use github to build stuff automatically.
- build frontends: pip, build, ...
- build backends: hatchling, setuptools, flit, PDM

---

- install pip: `py -m pip install --upgrade pip`
- install build: `py -m pip install --upgrade build`


## Python package, module, import


https://docs.python.org/3/tutorial/modules.html#packages

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```


Users of the package can import individual modules from the package, for example: 

```
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

An alternative way of importing the submodule is: 

```
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)
```
