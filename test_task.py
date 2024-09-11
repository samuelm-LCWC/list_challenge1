import task
import pytest
from unittest.mock import patch

@patch('builtins.input', return_value = "Geoff")
def test_task(mock_input):
    assert task.task() == ["Matthew", "Mark", "Luke", "Geoff"]