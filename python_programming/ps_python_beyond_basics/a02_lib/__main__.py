print("__main__.py is running")

# wrong to do it --> from a02_lib import *

from a03_m.func1 import use_all_ as why
from a03_m.func2 import use_all_how as how
why()
how()

# run it in terminal:
# python a02_lib

# run it as a zip file in terminal
# zip -r a02_lib.zip * （需要在a02_lib文件夹内部运行该代码）
# python a02_lib.zip
