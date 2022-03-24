import sys
import os

sys.path.append(os.path.abspath('../src'))

from app import index


def test_index():
    assert index() == 'Hello, world!'