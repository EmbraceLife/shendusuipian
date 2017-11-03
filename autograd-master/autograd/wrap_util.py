from .util import subvals

def unary_to_nary(unary_operator):
    @wraps(unary_operator)
    def nary_operator(fun, argnum=0, *nary_op_args, **nary_op_kwargs):
        print("""inside nary_operator:
                *nary_op_args: {},
                **nary_op_kwargs: {}
        """.format(nary_op_args, nary_op_kwargs))

        assert type(argnum) in (int, tuple, list), argnum
        @wrap_nary_f(fun, unary_operator, argnum)
        def nary_f(*args, **kwargs):
            print("""inside nary_f:
                    *args: {},
                    **kwargs: {}
            """.format(args, kwargs))

            @wraps(fun)
            def unary_f(x):
                if isinstance(argnum, int):
                    subargs = subvals(args, [(argnum, x)])
                else:
                    subargs = subvals(args, zip(argnum, x))
                return fun(*subargs, **kwargs)
            if isinstance(argnum, int):
                print("argnum: ", argnum)
                x = args[argnum]
            else:
                x = tuple(args[i] for i in argnum)
            return unary_operator(unary_f, x, *nary_op_args, **nary_op_kwargs)
        return nary_f
    return nary_operator




def wraps(fun, namestr="{fun}", docstr="{doc}", **kwargs):
    """创建和返回一个函数_wraps, 而_wraps则将函数fun的__name__, __doc__ (都是string)给予另一个函数f
    Args:
        fun: 一个函数
        namestr: 默认参数，"{fun}".format(fun = get_name)，用产生的新string取代{fun}
        docstr: 默认参数，意思同上
        **kwargs: 其他潜在named args
    Returns:
        _wraps
    """
    print(""" wraps:
                arg fun: {},
                arg namestr: {},
                arg docstr: {},
                arg **kwargs: {},
    """.format(fun.__name__, namestr, docstr, kwargs))
    def _wraps(f):
        """将函数fun的__name__, __doc__ (都是string)给予另一个函数f
        """
        print("_wraps: arg f is ", f.__name__)
        try:
            f.__name__ = namestr.format(fun=get_name(fun), **kwargs)
            f.__doc__ = docstr.format(fun=get_name(fun), doc=get_doc(fun), **kwargs)
        finally:
            return f
    return _wraps


def wrap_nary_f(fun, op, argnum):
    """ 创建新的可嵌入多个参数的namestr, docstr, 引入args: fun函数, op函数, argnum, 都作为wraps的参数，op函数的名称与argnum的值，会被带入到namestr与docstr中，然后返回wraps函数运行的结果，即_wraps函数

    Args:
        fun: 一个函数
        op: 估计也是函数
        argnum: 估计是int
    Returns:
        返回wraps函数

    Note: op=get_name(op), argnum=argnum, 对应的是wraps函数的**kwargs
    """
    print("""wrap_nary_f:
                arg fun: {},
                arg op: {},
                arg argnum: {}
                """.format(fun.__name__, op.__name__, argnum))
    namestr = "{op}_of_{fun}_wrt_argnum_{argnum}"
    docstr = """\
    {op} of function {fun} with respect to argument number {argnum}. Takes the
    same arguments as {fun} but returns the {op}.
    """

    return wraps(fun, namestr, docstr, op=get_name(op), argnum=argnum)


# 获取一个函数的名称，如果无名就返回'[unknown name]'
get_name = lambda f: getattr(f, '__name__', '[unknown name]')

# 获取一个函数的document，如果无名就返回''
get_doc  = lambda f: getattr(f, '__doc__' , '')
