from typing import Final

from hypothesis import given, strategies as st, assume

from main import Symbol

KEY_NONEXISTENT: Final[str] = "nonexistent"


@given(st.text())
def test_symbols_are_unique(key: str) -> None:
    sym1 = Symbol(key)
    sym2 = Symbol(key)

    assert sym1 != sym2
    assert sym1 == sym1
    assert sym2 == sym2


@given(st.text())
def test_symbol_str(key: str) -> None:
    assert str(Symbol(key)) == key


@given(st.text())
def test_symbol_hash(key: str) -> None:
    sym1 = Symbol(key)
    sym2 = Symbol(key)

    assert hash(sym1) == hash(sym1)
    assert hash(sym2) == hash(sym2)
    assert hash(sym1) != hash(sym2)


@given(st.text())
def test_symbol_repr(key: str) -> None:
    assert repr(Symbol(key)) == f"Symbol({repr(key)})"


def test_symbol_key_for_nonexistent() -> None:
    sym = Symbol(KEY_NONEXISTENT)
    assert Symbol.key_for(sym) is None


@given(st.text())
def test_key_for(key: str) -> None:
    assume(key != KEY_NONEXISTENT)
    assert Symbol.key_for(Symbol.for_(key)) == key


@given(st.text())
def test_symbol_for(key: str) -> None:
    assume(key != KEY_NONEXISTENT)

    sym1 = Symbol.for_(key)
    sym2 = Symbol.for_(key)
    sym3 = Symbol(key)

    assert sym1 == sym2
    assert sym1 != sym3
    assert sym2 != sym3
