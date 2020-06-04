import pytest
import habit_tracker as ht

task = ht.Task('exercise', ['M', 'W', 'F'])
task2 = ht.Task('clean')

def test_str():
    assert str(task2) == 'clean'
    assert str(task) == 'exercise; M,W,F'

def test_repr():
    assert repr(task) == 'exercise,M-W-F'