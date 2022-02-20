from unittest.mock import patch
import project
from project.main import check_todos, get_todos

@patch('project.main.get_todos',return_value=['dummy1','dummy2'])
def test_check_todos(mocker):
    result = project.main.check_todos()
    print (result)
    assert len(result) > 0
