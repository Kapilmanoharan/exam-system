import pytest
from app.main import grade, pass_fail

def test_grade_all_correct():
    student = {"q1": "A", "q2": "B"}
    correct = {"q1": "A", "q2": "B"}
    assert grade(student, correct) == 2

def test_grade_some_wrong():
    student = {"q1": "A", "q2": "C"}
    correct = {"q1": "A", "q2": "B"}
    assert grade(student, correct) == 1

def test_pass_fail_passes():
    assert pass_fail(3, 5, passing_percentage=50) == True

def test_pass_fail_fails():
    assert pass_fail(2, 5, passing_percentage=60) == False

def test_pass_fail_zero_total():
    assert pass_fail(0, 0) == False
