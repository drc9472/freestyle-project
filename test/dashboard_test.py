
import os
import pytest

from app.dashboard import valuation 

def test_valuation():
    results = valuation(input="Long Island City")
    assert results == "OVERVALUED"