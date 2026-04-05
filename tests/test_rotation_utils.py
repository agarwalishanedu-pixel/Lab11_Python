"""
Program Name: Lab 11
My name: Ishan Agarwal
Purpose: This is to better understand how tests work, and also get in the hang of the tools used.
Starter Code: None
Date: 04/05/2026
"""

import pytest
from rotation_utils import adjust_rotation

# The tests

def test_input_positive_100():
    assert adjust_rotation(100) == 100

def test_input_positive_460():
    assert adjust_rotation(460) == 100

def test_input_positive_820():
    assert adjust_rotation(820) == 100    


