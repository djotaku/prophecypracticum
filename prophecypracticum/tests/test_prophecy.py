"""Test prophecy."""

from prophecypracticum.engine import prophecy


def test_create_no_params_given():
    my_prophecy = prophecy.Prophecy()
    assert my_prophecy.prophecy_text == ""
    assert my_prophecy.prophecy_photo == ""
    assert my_prophecy.feedback_rating == 0
    assert my_prophecy.feedback_text == ""


def test_create_with_prophecy_text():
    my_prophecy = prophecy.Prophecy(prophecy_text="You will be happy today.")
    assert my_prophecy.prophecy_text == "You will be happy today."


def test_create_with_prophecy_photo():
    my_prophecy = prophecy.Prophecy(prophecy_photo="/a/path/to/photo.jpg")
    assert my_prophecy.prophecy_photo == "/a/path/to/photo.jpg"


