# Conda
```bash
# download miniconda https://docs.conda.io/en/latest/miniconda.html
conda --version # check version:
conda update conda # update conda: , install outside env
conda create -n mesa-abm python=3.6 anaconda # build environment
source activate mesa-abm
source deactivate
conda info --envs # check envs
conda env list # all envs to view
conda create --name new_env --clone existed_env # clone an env
conda remove --name old_env --all # delete an env
conda env export > environment.yml # 输出env
conda env create -f environment.yml # build env from yml
```

# Jupyter notebook
```
# If you have Python 3 installed (which is recommended):

python3 -m pip install --upgrade pip
python3 -m pip install jupyter

jupyter notebook # to start 
```

# git
```bash
# create a new repo on github
# go to your Mac directory 
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/EmbraceLife/NetLogo-Modeling.git
git push -u origin master


# make my fork from official
# copy git repo link for clone
git clone https://github.com/EmbraceLife/mesa # from my fork to download the project into your Mac or PC
cd my_fork
git remote add upstream official-url-git # link to official repo
git pull upstream master # pull from official version
# git merge upstream/master # when necessary
git push # update my own fork version
git pull # pull from my own fork version

git push origin --delete a_remote_branch_name # to delete a branch remote in github
svn checkout url-folder-replace-tree/master-with-trunk # only download part of a repo

git branch # check all branches
git branch new_branch_name # create a branch from where we are
git branch -m a_new_name # rename
git branch -d branch_to_go # delete
git checkout new_branch # switch to a new branch

git merge new_branch # from where we are, merge new_branch into where we are.

git status
git add .
git commit -m "comment"
git push

git reset # to undo git add .
```

# 实验代码
```
# https://mesa.readthedocs.io/en/latest/tutorials/intro_tutorial.html
pip install mesa
pip install requirements.txt # inside folder of /Users/Natsume/Desktop/mesa/examples/boltzmann_wealth_model
# if can't run, then open this file with `nano requirement.txt` to see the libraries needed installation
```


# 重建工作平台
```bash
# 下载安装miniconda
conda create -n experiment3.5 python=3.5
# debug
pip install pdbpp
conda install scipy numpy matplotlib bcolz pandas autograd
conda install tensorflow keras
# 如果反复遇到报错，可以试试将 conda换成pip
# 更新最新版tensorflow
pip install tensorflow-1.3.0rc2-py3-none-any.whl
# 技术指标
brew install ta-lib
pip install TA-Lib
```

# debug工具
```bash
pip install pdbpp
python -m pdb file-name.py
# 原来进入代码，输入insert import pdb; pdb.set_trace() 来debug已经不需要了
sticky # 看到全局代码
ll # 从debug跳回到全局代码
# l 20
# l 1, 20: see line from 1 to 20
s # step into a function
n # 运行下一行
w # call stack, where I started and where I am in source code, d go down a stack, u to go up a stack
b 88 # 运行到88行，暂停
# b file.py:41 or b func_name
# b 11, this_year==2017: conditional breakpoint, at line 11 to breakpoint, if this_year == 2017
cl 1 # 删除第一个breakpoint
r # 运行所在 function
c # 运行直到结束
q # 终止
? # 查看文档
hit return # 重复上一次操作
pp variable_name # 友好打印 该变量
# 完成当前loop: until
```

# 构建bash_profile
```bash
cd # go to home directory
nano .bash_profile # go inside .bash_profile:

################# code content
alias v3='cd /Users/Natsume/Documents/course-v3/nbs/dl1; conda activate fastai'
alias sfastai='cd /Users/Natsume/miniconda3/envs/fastai/lib/python3.7/site-pack$
alias pdbpp='python -m pdb'
alias de='conda deactivate'
alias xcode="open -a Xcode"


function lazygit() {
    git add .
    git commit -a -m "$1"
    git push
}

export PS1="\w " ## show full address at cursor

###################
ctrl + x, y, enter # save and exit:
source .bash_profile # source to activate:

```

# 构建pdbrc
[如何构建和安装pdbrc video](https://www.bilibili.com/video/av16754002/)
[如何使用pdbpp来实验代码](https://www.bilibili.com/video/av16753161/)
```python
## located at ~ directory, named .pdbrc, no need for source, just save it

alias dr pp dir(%1) # 查看everything underneath the object
alias dt pp %1.__dict__ # 查看object's dictionaries
alias pdt for k, v in %1.items(): print(k, ": ", v) # 查看一个纯 python dictionary
alias loc locals().keys() # local variables
alias doc from inspect import getdoc; from pprint import pprint; pprint(getdoc(%1)) # documents
alias sources from inspect import getsourcelines; from pprint import pprint; pprint(getsourcelines(%1)) # source code
alias module from inspect import getmodule; from pprint import pprint; pprint(getmodule(%1)) # module name
alias fullargs from inspect import getfullargspec; from pprint import pprint; pprint(getfullargspec(%1)) # all arguments names
alias opt_param optimizer.param_groups[0]['params'][%1] # all parameters
alias opt_grad optimizer.param_groups[0]['params'][%1].grad # all gradients of parameters
```

# Jupyter notebook extensions
3 steps to install
```
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable toc2/main  # in terminal or notebook cell, both are fine
# edit/notebook_config (at bottom of the droplist)
```
# jn color theme 
```
pip install jupyterthemes
jt -t onedork 
#| grade3 | oceans16 | chesterish | monokai | solarizedl | solarizedd
```
