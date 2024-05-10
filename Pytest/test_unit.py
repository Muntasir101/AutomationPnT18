import pytest


def add(x, y):
    return x + y


def test_add_TC1():
    assert add(10, 30) == 50


def test_add_TC2():
    assert add(50, 0) == 50
