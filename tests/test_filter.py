import pytest

# Local imports
from src.demo_design_pattern import concept

##############################################################################
# Fixtures
##############################################################################


@pytest.fixture
def valid_searchstring():
    return 'B*'


@pytest.fixture
def invalid_searchstring():
    return 'abracadabra'


def test_valid_filter(valid_searchstring):
    filetype = 'Json'
    ui = concept.Ui(filetype)
    ui.call_filter(valid_searchstring)


def test_invalid_filter(invalid_searchstring):
    filetype = 'Json'
    ui = concept.Ui(filetype)
    ui.call_filter(invalid_searchstring)
