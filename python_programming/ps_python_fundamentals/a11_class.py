
class BottomUp:
    def __init__(self, tool):
        if not isinstance(tool, str): # list, dict, int, str as types
            raise ValueError("tool must be string type")
        if not tool.isalpha():
            raise ValueError("tool must be in alphabetic charaters")
        self._tool = tool
    def _check_version(self):
        return self._tool+"_latest"
    def get_tools(self):
        return self._tool

g = BottomUp("keras")
g.get_tools()
g._check_version()
dir(g)
