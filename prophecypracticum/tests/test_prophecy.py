"""Test prophecy."""

from prophecypracticum.engine import prophecy
from datetime import datetime

test_datetime = datetime(2020, 12, 25, 00, 00)


def test_create_no_params_given():
    my_prophecy = prophecy.Prophecy(test_datetime)
    assert my_prophecy.date_of_prophecy == datetime(2020, 12, 25, 00, 00)
    assert my_prophecy.prophecy_text == ""
    assert my_prophecy.prophecy_photo == ""
    assert my_prophecy.feedback_rating == 0
    assert my_prophecy.feedback_text == ""


def test_create_with_prophecy_text():
    my_prophecy = prophecy.Prophecy(test_datetime, prophecy_text="You will be happy today.")
    assert my_prophecy.prophecy_text == "You will be happy today."


def test_create_with_prophecy_photo():
    my_prophecy = prophecy.Prophecy(test_datetime, prophecy_photo="/a/path/to/photo.jpg")
    assert my_prophecy.prophecy_photo == "/a/path/to/photo.jpg"


# API unit tests. Any changes here should signify a change in major version number
def test_get_text_prophecy():
    """The user should be able to get the text of the prophecy."""
    my_prophecy = prophecy.Prophecy(test_datetime, prophecy_text="You will be happy today.")
    prophecy_text = my_prophecy.get_text_prophecy()
    assert prophecy_text == "You will be happy today."


def test_modify_text_prophecy():
    """The user should be able to modify the text of their prophecy."""
    my_prophecy = prophecy.Prophecy(test_datetime, prophecy_text="You will be happy today.")
    my_prophecy.modify_text_prophecy("You will be sad today.")
    assert my_prophecy.prophecy_text == "You will be sad today."


def test_get_photo_prophecy():
    """The user should be able to get a photo prophecy. The web will actually return the photo."""
    my_prophecy = prophecy.Prophecy(test_datetime, prophecy_photo="/a/path/to/photo.jpg")
    photo_location = my_prophecy.get_photo_location()
    assert photo_location == "/a/path/to/photo.jpg"


def test_modify_photo_prophecy():
    """The user should be able to modify a photo prophecy to point to another photo."""
    my_prophecy = prophecy.Prophecy(test_datetime, prophecy_photo="/a/path/to/photo.jpg")
    my_prophecy.modify_photo_prophecy("a/different/photo.jpg")
    assert my_prophecy.prophecy_photo == "a/different/photo.jpg"


def test_set_feedback_rating():
    """The supplicant should be able to set a feedback rating."""
    my_prophecy = prophecy.Prophecy(test_datetime, prophecy_text="You will be happy today.")
    my_prophecy.set_feedback_rating(4)
    assert my_prophecy.feedback_rating == 4

def test_change_feedback_rating():
    """The supplicant should be able to change a feedback rating."""
    my_prophecy = prophecy.Prophecy(test_datetime, prophecy_text="You change your feedback today.")
    my_prophecy.set_feedback_rating(4)
    old_rating = my_prophecy.get_feedback_rating()
    assert old_rating == 4
    my_prophecy.set_feedback_rating(2)
    assert my_prophecy.get_feedback_rating() == 2

def test_get_feedback_rating():
    """A user should be able to retrieve the feedback rating."""
    my_prophecy = prophecy.Prophecy(test_datetime, prophecy_text="You will be happy today.")
    my_prophecy.feedback_rating = 3
    rating = my_prophecy.get_feedback_rating()
    assert rating == 3


def test_set_feedback_text():
    """The supplicant should be able to set feedback text."""
    my_prophecy = prophecy.Prophecy(test_datetime, prophecy_text="You will be happy today.")
    my_prophecy.set_feedback_text("Wow, that was so incredibly relevant.")
    assert my_prophecy.feedback_text == "Wow, that was so incredibly relevant."


def test_get_feedback_text():
    """A user should be able ot access feedback text."""
    my_prophecy = prophecy.Prophecy(test_datetime, prophecy_text="You will be happy today.")
    my_prophecy.feedback_text = "It was a little vague."
    text = my_prophecy.get_feedback_text()
    assert text == "It was a little vague."
