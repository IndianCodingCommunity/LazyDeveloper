import pytest
from lazyGeek.core import greet, LazyGeek

import sys
import os

# Append the path to your library's root directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_greet():
    result = greet("John")
    assert "Hello, John!" in result


def test_lazy_geek_double():
    lg = LazyGeek(5)
    assert lg.double() == 10
