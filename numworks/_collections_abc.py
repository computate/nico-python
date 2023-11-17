
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

GenericAlias = type(list[int])
EllipsisType = type(...)
def _f(): pass
FunctionType = type(_f)
del _f
__all__ = ["Sequence"
           ]
__name__ = "collections_abc"
bytes_iterator = type(iter(b''))
bytearray_iterator = type(iter(bytearray()))
dict_keyiterator = type(iter({}.keys()))
dict_valueiterator = type(iter({}.values()))
dict_itemiterator = type(iter({}.items()))
list_iterator = type(iter([]))
list_reverseiterator = type(iter(reversed([])))
range_iterator = type(iter(range(0)))
longrange_iterator = type(iter(range(1 << 1000)))
set_iterator = type(iter(set()))
str_iterator = type(iter(""))
tuple_iterator = type(iter(()))
zip_iterator = type(iter(zip()))
dict_keys = type({}.keys())
dict_values = type({}.values())
dict_items = type({}.items())
mappingproxy = type(type.__dict__)
generator = type((lambda: (yield))())
def _check_methods(C, *methods):
    mro = C.__mro__
    for method in methods:
        for B in mro:
            if method in B.__dict__:
                if B.__dict__[method] is None:
                    return NotImplemented
                break
        else:
            return NotImplemented
    return True

class Container(metaclass=ABCMeta):
    __slots__ = ()
    @abstractmethod
    def __contains__(self, x):
        return False
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Container:
            return _check_methods(C, "__contains__")
        return NotImplemented
    __class_getitem__ = classmethod(GenericAlias)

class Sized(metaclass=ABCMeta):
    __slots__ = ()
    @abstractmethod
    def __len__(self):
        return 0
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            return _check_methods(C, "__len__")
        return NotImplemented

class Iterable(metaclass=ABCMeta):
    __slots__ = ()
    @abstractmethod
    def __iter__(self):
        while False:
            yield None
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterable:
            return _check_methods(C, "__iter__")
        return NotImplemented
    __class_getitem__ = classmethod(GenericAlias)
class Iterator(Iterable):
    __slots__ = ()
    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration
    def __iter__(self):
        return self
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            return _check_methods(C, '__iter__', '__next__')
        return NotImplemented
Iterator.register(bytes_iterator)
Iterator.register(bytearray_iterator)
Iterator.register(dict_keyiterator)
Iterator.register(dict_valueiterator)
Iterator.register(dict_itemiterator)
Iterator.register(list_iterator)
Iterator.register(list_reverseiterator)
Iterator.register(range_iterator)
Iterator.register(longrange_iterator)
Iterator.register(set_iterator)
Iterator.register(str_iterator)
Iterator.register(tuple_iterator)
Iterator.register(zip_iterator)
class Reversible(Iterable):
    __slots__ = ()
    @abstractmethod
    def __reversed__(self):
        while False:
            yield None
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Reversible:
            return _check_methods(C, "__reversed__", "__iter__")
        return NotImplemented

class Collection(Sized, Iterable, Container):
    __slots__ = ()
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Collection:
            return _check_methods(C,  "__len__", "__iter__", "__contains__")
        return NotImplemented

class Sequence(Reversible, Collection):
    __slots__ = ()
    __abc_tpflags__ = 1 << 5 # Py_TPFLAGS_SEQUENCE
    @abstractmethod
    def __getitem__(self, index):
        raise IndexError
    def __iter__(self):
        i = 0
        try:
            while True:
                v = self[i]
                yield v
                i += 1
        except IndexError:
            return
    def __contains__(self, value):
        for v in self:
            if v is value or v == value:
                return True
        return False
    def __reversed__(self):
        for i in reversed(range(len(self))):
            yield self[i]
    def index(self, value, start=0, stop=None):
        if start is not None and start < 0:
            start = max(len(self) + start, 0)
        if stop is not None and stop < 0:
            stop += len(self)
        i = start
        while stop is None or i < stop:
            try:
                v = self[i]
            except IndexError:
                break
            if v is value or v == value:
                return i
            i += 1
        raise ValueError
    def count(self, value):
        'S.count(value) -> integer -- return number of occurrences of value'
        return sum(1 for v in self if v is value or v == value)
Sequence.register(tuple)
Sequence.register(str)
Sequence.register(range)
Sequence.register(memoryview)
