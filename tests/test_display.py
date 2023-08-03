import pytest

# Local imports
from src.demo_design_pattern import concept

##############################################################################
# Fixtures
##############################################################################


def test_valid_display():
    filetype = 'Json'
    ui = concept.Ui(filetype)
    ui.call_display()
