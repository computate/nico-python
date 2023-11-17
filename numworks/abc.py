def abstractmethod(funcobj):
    funcobj.__isabstractmethod__ = True
    return funcobj
class abstractclassmethod(classmethod):
    __isabstractmethod__ = True
    def __init__(self, callable):
        callable.__isabstractmethod__ = True
        super().__init__(callable)
class abstractstaticmethod(staticmethod):
    __isabstractmethod__ = True
    def __init__(self, callable):
        callable.__isabstractmethod__ = True
        super().__init__(callable)
class ABCMeta(type):
    def __new__(mcls, name, bases, namespace, **kwargs):
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        _abc_init(cls)
        return cls
    def register(cls, subclass):
        return _abc_register(cls, subclass)
    def __instancecheck__(cls, instance):
        return _abc_instancecheck(cls, instance)
    def __subclasscheck__(cls, subclass):
        return _abc_subclasscheck(cls, subclass)
    def _dump_registry(cls, file=None):
        print("Class: {cls.__module__}.{cls.__qualname__}", file=file)
        print("Inv. counter: {get_cache_token()}", file=file)
        (_abc_registry, _abc_cache, _abc_negative_cache,
         _abc_negative_cache_version) = _get_dump(cls)
        print("_abc_registry: {_abc_registry!r}", file=file)
        print("_abc_cache: {_abc_cache!r}", file=file)
        print("_abc_negative_cache: {_abc_negative_cache!r}", file=file)
        print("_abc_negative_cache_version: {_abc_negative_cache_version!r}",
              file=file)
    def _abc_registry_clear(cls):
        _reset_registry(cls)
    def _abc_caches_clear(cls):
        _reset_caches(cls)
def update_abstractmethods(cls):
    if not hasattr(cls, '__abstractmethods__'):
        return cls
    abstracts = set()
    for scls in cls.__bases__:
        for name in getattr(scls, '__abstractmethods__', ()):
            value = getattr(cls, name, None)
            if getattr(value, "__isabstractmethod__", False):
                abstracts.add(name)
    for name, value in cls.__dict__.items():
        if getattr(value, "__isabstractmethod__", False):
            abstracts.add(name)
    cls.__abstractmethods__ = frozenset(abstracts)
    return cls
class ABC(metaclass=ABCMeta):
    __slots__ = ()