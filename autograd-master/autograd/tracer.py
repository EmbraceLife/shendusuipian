import warnings
from contextlib import contextmanager
from collections import defaultdict
from autograd.util import subvals
from autograd.wrap_util import wraps
#######################
#### what does contextmanager and defaultdict do?
# import contextlib
# help(contextlib)
# help(contextlib.contextmanager)
# help(defaultdict)
#### directory issues and package path
# from .util import subvals
# from autograd.util import subvals
# help(defaultdict)

# trace_stack(TraceStack), new_box
def trace(start_node, fun, x):
    with trace_stack.new_trace() as t:
        start_box = new_box(x, t, start_node)
        end_box = fun(start_box)
        if isbox(end_box) and end_box._trace == start_box._trace:
            return end_box._value, end_box._node
        else:
            warnings.warn("Output seems independent of input.")
            return end_box, None

# done
class Node(object):
    __slots__ = []
    def __init__(self, value, fun, args, kwargs, parent_argnums, parents):
        assert False # default assert False is for later overwrite?

    def initialize_root(self, *args, **kwargs):
        assert False # default assert False is for later overwrite?

    @classmethod
    def new_root(cls, *args, **kwargs):
        root = cls.__new__(cls)
        print("what is root: ", root)
        root.initialize_root(*args, **kwargs) # default assert False is for later overwrite?
        return root
# help(object.__new__)
# n = Node.new_root()
# def fun(x): pass
# node = Node(1, fun, 1, "node", parent_argnums=1, parents="p")
# n.initialize_root()
# n.new_root()

# wraps, subvals, find_top_boxed_args, new_box, notrace_primitives
def primitive(f_raw):
    """
    Wraps a function so that its gradient can be specified and its invocation
    can be recorded. For examples, see the docs."""
    @wraps(f_raw)
    def f_wrapped(*args, **kwargs):
        boxed_args, trace, node_constructor = find_top_boxed_args(args)
        if boxed_args:
            argvals = subvals(args, [(argnum, box._value) for argnum, box in boxed_args])
            if f_wrapped in notrace_primitives[node_constructor]:
                return f_wrapped(*argvals, **kwargs)
            parents = tuple(box._node for _     , box in boxed_args)
            argnums = tuple(argnum    for argnum, _   in boxed_args)
            ans = f_wrapped(*argvals, **kwargs)
            node = node_constructor(ans, f_wrapped, argvals, kwargs, argnums, parents)
            return new_box(ans, trace, node)
        else:
            return f_raw(*args, **kwargs)
    f_wrapped.fun = f_raw
    return f_wrapped

# defaultdict
notrace_primitives = defaultdict(set)

# notrace_primitives
def register_notrace(trace_type, primitive_fun):
    notrace_primitives[trace_type].add(primitive_fun)

# wraps, map
def notrace_primitive(f_raw):
    @wraps(f_raw)
    def f_wrapped(*args, **kwargs):
        argvals = map(getval, args)
        return f_raw(*argvals, **kwargs)
    f_wrapped._is_primitive = True
    return f_wrapped

# isbox
def find_top_boxed_args(args):
    top_trace = -1
    top_boxes = []
    top_node_type = None
    for argnum, arg in enumerate(args):
        if isbox(arg):
            trace = arg._trace
            if trace > top_trace:
                top_boxes = [(argnum, arg)]
                top_trace = trace
                top_node_type = type(arg._node)
            elif trace == top_trace:
                top_boxes.append((argnum, arg))
    return top_boxes, top_trace, top_node_type

# contextmanager
class TraceStack(object):
    def __init__(self):
        self.top = -1
    @contextmanager
    def new_trace(self):
        self.top += 1
        yield self.top
        self.top -= 1
trace_stack = TraceStack()

#
class Box(object):
    type_mappings = {}
    types = set()

    __slots__ = ['_value', '_trace', '_node']
    def __init__(self, value, trace, node):
        self._value = value
        self._node = node
        self._trace = trace

    def __bool__(self):
        return bool(self._value)

    __nonzero__ = __bool__

    def __str__(self):
        return "Autograd {0} with value {1}".format(
            type(self).__name__, str(self._value))

    @classmethod
    def register(cls, value_type):
        Box.types.add(cls)
        Box.type_mappings[value_type] = cls
        Box.type_mappings[cls] = cls

#
def toposort(end_node):
    child_counts = {}
    stack = [end_node]
    while stack:
        node = stack.pop()
        if node in child_counts:
            child_counts[node] += 1
        else:
            child_counts[node] = 1
            stack.extend(node.parents)

    childless_nodes = [end_node]
    while childless_nodes:
        node = childless_nodes.pop()
        yield node
        for parent in node.parents:
            if child_counts[parent] == 1:
                childless_nodes.append(parent)
            else:
                child_counts[parent] -= 1

# Box
box_type_mappings = Box.type_mappings

# box_type_mappings
def new_box(value, trace, node):
    try:
        return box_type_mappings[type(value)](value, trace, node)
    except KeyError:
        raise TypeError("Can't differentiate w.r.t. type {}".format(type(value)))

# Box
box_types = Box.types

# box_types
isbox  = lambda x: type(x) in box_types  # almost 3X faster than isinstance(x, Box)

# isbox, getval
getval = lambda x: getval(x._value) if isbox(x) else x
