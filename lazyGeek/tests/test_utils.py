import pytest
from lazyGeek.utils import add

def test_add():
    result = add(3, 5)
    assert result == 8