import pytest
import habit_tracker as ht

task = ht.Task('exercise', [0, 2, 4])
task2 = ht.Task('clean')

def test_str():
    assert str(task) == 'exercise, M,W,F'
    assert str(task2) == 'clean'