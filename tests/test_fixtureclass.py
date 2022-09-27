import pytest

pytest_plugins = ["pytester"]

def test_example(testdir, pytester):
    pytester.copy_example("examples/fixtureclass.py")
    pytester.runpytest("-k", "fixtureclass")
