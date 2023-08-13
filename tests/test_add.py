import pytest

# Local imports
from src.demo_design_pattern import concept

##############################################################################
# Fixtures
##############################################################################


@pytest.fixture
def valid_item():
    item = {'test': 'Z', 'phone': 1234567890, 'address': 'a\\b building no X, floor X, landmark, city, state pincode '}
    return item


def test_valid_add(valid_item):
    filetype = 'Json'
    ui = concept.Ui(filetype)
    ui.call_add(valid_item)
