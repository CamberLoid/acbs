
class LoaderHelper(object):

    func_maps = {}

    def __init__(self):
        return

    @classmethod
    def register(cls, when, args=()):
        def func(fn):
            if not cls.func_maps.get(when):
                cls.func_maps[when] = [(fn, args)]
            else:
                cls.func_maps[when].append((fn, args))
            return fn
        return func

    @staticmethod
    def callback(when):
        cbs = LoaderHelper.func_maps.get(when)
        if cbs:
            for cb in cbs:
                return cb[0](*cb[1])
