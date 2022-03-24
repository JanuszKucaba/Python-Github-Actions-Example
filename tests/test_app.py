import sys

sys.path.insert(0, 'C:\\Python\\Programy\\PODSTAWY\\CICD\\python-github-actions-example\\src')

from app import index


def test_index():
    assert index() == 'Hello, world!'