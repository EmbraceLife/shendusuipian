import urllib
import urllib.request
type(urllib)
type(urllib.request)
urllib.__path__
urllib.__file__
urllib.__name__
urllib.__package__


urllib.request.__path__
urllib.request.__file__

###################
import sys
sys.path

import test_path
test_path.found()
# won't work outside this dir

# manually add into path
import sys
sys.path.append("/Users/Natsume/Documents/shendusuipian/python_programming/ps_python_beyond_basics")
sys.path
import test_path
test_path.found()

# 更简单的操作
`export PYTHONPATH=/Users/Natsume/Documents/shendusuipian/python_programming/ps_python_beyond_basics`

# 但都是临时效果，下一次重启terminal, 还是要重复export path
