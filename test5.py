import os
from unittest.mock import patch

def direction(name):
    return name in os.listdir()

@patch('os.listdir')
def test_direction(listdir_mock):
    listdir_mock.return_value = ['tmp', 'tmp1']
    assert direction('tmp')
    listdir_mock.assert_called_once()