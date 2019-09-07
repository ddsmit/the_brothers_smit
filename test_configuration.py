import configuration
import pytest

@pytest.fixture
def test_character():
    return configuration.load_character(r'test_characters.yml', 'test_character')


def test_load_character_relative(test_character):
    assert isinstance(test_character, dict)


@pytest.mark.parametrize('parameter', ['hp', 'ap', 'dp', 'mp', 'md'])
def test_initial_value(test_character, parameter):
    assert test_character[parameter] is not None
    assert test_character[parameter] > 0


def test_actions(test_character):
    assert test_character['actions'] == ['actions.jab', 'actions.slice']