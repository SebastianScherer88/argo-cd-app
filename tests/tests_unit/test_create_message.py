import pytest
from app.utils import create_message

@pytest.mark.parametrize(
    ('name,expected_message'),
    [('Test name','Hello!!! And welcome to the sample app, Test name!'),
    ('some really weird and fancy name','Hello!!! And welcome to the sample app, some really weird and fancy name!'),
    ('','Hello!!! And welcome to the sample app, !')]
)
def test_create_message(name, expected_message):

    assert expected_message == create_message(name)