"""Test prophecy."""

from prophecypracticum.engine import prophecy


def test_create_no_params_given():
    my_prophecy = prophecy.Prophecy()
    assert my_prophecy.prophecy_text == ""
    assert my_prophecy.prophecy_photo == ""
    assert my_prophecy.feedback_rating == 0
    assert my_prophecy.feedback_text == ""