"""testing dictionary.py"""

__author__: str = "730760820"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

from dictionary import invert
import pytest


def test_invert_basic():
    """basic for invert"""
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}


def test_invert_single():
    """single for invert"""
    assert invert({"a": "1"}) == {"1": "a"}


def test_invert_empty():
    """Edge case: empty dictionary"""
    assert invert({}) == {}


def test_invert_keyerror():
    """Test for KeyError"""
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_favorite_color():
    """multiple people like same colors"""
    assert (
        favorite_color({"Aiah": "blue", "Seoyun": "blue", "Tina": "purple"}) == "blue"
    )


def test_favorite_color_single():
    """single person is tested"""
    assert favorite_color({"Chandi": "black"}) == "black"


def test_favorite_color_empty():
    """Edge case: empty dictionary"""
    assert favorite_color({}) == ""


def test_count_basic():
    """basic for count"""
    assert count(["snickers", "Kitkat", "kitkat", "twix"]) == {
        "snickers": 1,
        "kitkat": 2,
        "twix": 1,
    }


def test_count_single():
    """single chocolate is tested"""
    assert count(["hershey's"]) == {"hershey's": 1}


def test_count_empty():
    """Edge case: empty dictionary"""
    assert count([]) == {}


def test_bin_len_basic():
    """basic for bin_len"""
    assert bin_len(["glass", "chair"]) == {5: {"glass", "chair"}}


def test_bin_len_large():
    """test larger words"""
    assert bin_len(["glasses", "children", "mountain"]) == {
        7: {"glasses"},
        8: {"children", "mountain"},
    }


def test_bin_len_empty_zero():
    """Edge case: zero dictionary"""
    assert bin_len([]) == {}
