"""bot context tests"""
import pytest

from bot_common.context import BotContext
from bot_common.exceptions import InvalidContextError


##############################################################################
# Fixtures
##############################################################################
@pytest.fixture
def show_context():
    return BotContext('mock01')


@pytest.fixture
def show_shot_context():
    return BotContext('mock01', 'shot02')


@pytest.fixture
def no_show_context():
    return BotContext(None, 'shot1')


@pytest.fixture
def invalid_show_type_context():
    return BotContext(1234)


@pytest.fixture
def invalid_shot_type_context():
    return BotContext('mock01', 1234)


##############################################################################
# Fixtures
##############################################################################
def test_show_context(show_context):
    assert show_context.show == 'mock01'
    assert show_context.shot is None


def test_show_shot_context(show_shot_context):
    assert show_shot_context.show == 'mock01'
    assert show_shot_context.shot == 'shot02'


def test_validate_show_context(show_context):
    try:
        show_context.validate()
    except Exception:
        raise


def test_validate_show_shot_context(show_shot_context):
    try:
        show_shot_context.validate()
    except Exception:
        raise


def test_validate_raises_exception_no_show_context(no_show_context):
    with pytest.raises(InvalidContextError):
        no_show_context.validate()


def test_validate_raises_exception_invalid_show_type_context(
        invalid_show_type_context):
    with pytest.raises(InvalidContextError):
        invalid_show_type_context.validate()


def test_validate_raises_exception_invalid_shot_type_context(
        invalid_shot_type_context):
    with pytest.raises(InvalidContextError):
        invalid_shot_type_context.validate()


def test_is_valid_show_context(show_context):
    assert show_context.is_valid()


def test_is_valid_invalid_shot_type_context(invalid_shot_type_context):
    assert not invalid_shot_type_context.is_valid()


def test_returns_as_dict_show_context(show_context):
    context_dict = show_context.as_dict()
    print(context_dict)
    assert isinstance(context_dict, dict)
    assert context_dict['show'] == show_context.show
    assert 'shot' not in context_dict


def test_returns_as_dict_show_shot_context(show_shot_context):
    context_dict = show_shot_context.as_dict()
    assert isinstance(context_dict, dict)
    assert context_dict['show'] == show_shot_context.show
    assert context_dict['shot'] == show_shot_context.shot
