import pytest

# Local imports
from demo_design_pattern.test_05 import FileFactory

##############################################################################
# Fixtures
##############################################################################
@pytest.fixture
def write_json():
    first_file = FileFactory().file_referencer('Json')
    data = {'name': 'A', 'phone': 1234567890, 'address': 'a\\b building no X, floor X, landmark, city, state pincode '}
    first_file.write(data)


@pytest.fixture
def read_json():
    first_file = FileFactory().file_referencer('Json')
    first_file.read()


@pytest.fixture
def write_yaml():
    first_file = FileFactory().file_referencer('Yaml')
    data = {'name': 'A', 'phone': 1234567890, 'address': 'a\\b building no X, floor X, landmark, city, state pincode '}
    first_file.write(data)


@pytest.fixture
def read_yaml():
    first_file = FileFactory().file_referencer('Yaml')
    test_data = {'name': 'A', 'phone': 1234567890, 'address': 'a\\b building no X, floor X, landmark, city, state pincode '}
    first_file.read(test_data)


@pytest.fixture
def wrong_file():
    first_file = FileFactory().file_referencer('Abcd')
    test_data = {'name': 'A', 'phone': 1234567890, 'address': 'a\\b building no X, floor X, landmark, city, state pincode '}
    first_file.read(test_data)

##############################################################################
# Fixtures
##############################################################################


def test_write_json(data):
    assert data == {'name': 'A', 'phone': 1234567890, 'address': 'a\\b building no X, floor X, landmark, city, state pincode '}


def test_read_json(filename):
    assert filename == r'E:\my_jobs\pycharm\demo_design_pattern\src\demo_design_pattern\demo.json'
