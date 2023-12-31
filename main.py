from __future__ import annotations

from typing import final, Final, Optional, Collection, Iterator

from bidict import bidict


@final
class Symbol(Collection[str]):
    """
    `Symbol` is a class whose constructor returns a `Symbol` value or just
    a `Symbol` — that's guaranteed to be unique. Symbols are often used to add
    unique property keys to an object that won't collide with keys any other
    code might add to the object.

    Every `Symbol()` call is guaranteed to return a unique `Symbol`.
    Every `Symbol.for("key")` call will always return the same `Symbol` for a
    given value of `"key"`. When `Symbol.for("key")` is called, if a `Symbol`
    with the given key can be found in the global `Symbol` registry, that
    `Symbol` is returned. Otherwise, a new Symbol is created, added to the
    global `Symbol` registry under the given key, and returned.
    """
    __shared: Final[bidict[str, Symbol]] = bidict()

    def __init__(self, description: str = "", /) -> None:
        """
        Creates a new Symbol object.

        :param description: A string. A description of the symbol which can be
        used for debugging but not to access the symbol itself. Defaults to an
        empty string.
        """
        self.__description: Final[str] = description
        self.__hash: Final[int] = id(self)

    @classmethod
    def for_key(cls, key: str, /) -> Symbol:
        """
        The `Symbol.for_key()` (`Symbol.for()` in JavaScript) static method
        searches for existing symbols in a runtime-wide symbol registry with
        the given key and returns it if found. Otherwise a new symbol gets
        created in the global symbol registry with this key.

        In contrast to `Symbol()`, the `Symbol.for_key()` function creates
        a symbol available in a global symbol registry list.
        `Symbol.for_key()` does also not necessarily create a new symbol on
        every call, but checks first if a symbol with the given key is already
        present in the registry. In that case, that symbol is returned. If no
        symbol with the given key is found, `Symbol.for_key()` will create
        a new global symbol.

        :param key: The key for the symbol (and also used for the
        description of the symbol).
        :return: An existing symbol with the given key if found; otherwise,
        a new symbol is created and returned.
        """
        if key not in cls.__shared:
            cls.__shared[key] = cls(key)

        return cls.__shared[key]

    @classmethod
    def key_for(cls, sym: Symbol, /) -> Optional[str]:
        """
        The `Symbol.key_for()` (`Symbol.keyFor()` in JavaScript) static method
        retrieves a shared symbol key from the global symbol registry for the
        given symbol.

        :param sym: The symbol to find a key for.
        :return: A string representing the key for the given symbol if one is
        found on the global registry; otherwise, `None`.
        """
        return cls.__shared.inverse.get(sym, None)

    def __str__(self) -> str:
        return self.__description

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.__description)})"

    def __eq__(self, other: object) -> bool:
        return self is other

    def __hash__(self) -> int:
        return self.__hash

    def __len__(self) -> int:
        return len(self.__description)

    def __iter__(self) -> Iterator[str]:
        return iter(self.__description)

    def __contains__(self, item: object) -> bool:
        return type(item) is str and item in self.__description
