import pytest

from src.demo_design_pattern import concept
############################################################################
# FIXTURES
############################################################################


@pytest.fixture
def valid_filetype_to():
    return 'Yaml'


@pytest.fixture
def invalid_filetype_to():
    return 'Ymal'


def test_valid_convert(valid_filetype_to):
    filetype_from = 'Json'
    ui = concept.Ui(filetype_from)
    ui.call_convert(valid_filetype_to)


def test_invalid_convert(invalid_filetype_to):
    filetype_from = 'Json'
    ui = concept.Ui(filetype_from)
    ui.call_convert(invalid_filetype_to)
