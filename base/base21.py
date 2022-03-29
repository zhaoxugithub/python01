def foo(name, **kwds):
    return "name2" in kwds


foo(1, {"name2": 2})
