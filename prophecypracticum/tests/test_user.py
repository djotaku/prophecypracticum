"""Test user methods."""

from prophecypracticum.engine import user


def test_user_creation():
    """Create a user and check values."""
    my_user = user.User("Christopher", "Chris@chris.com")
    assert my_user.name == "Christopher"
    assert my_user.email == "Chris@chris.com"
    assert my_user.my_id == 0
    assert my_user.supplicant_id == 0
    assert my_user.prophecy_given is False
    assert my_user.prophecy_received is False
    assert my_user.prophecy_received_and_interacted is False


# API unit tests. Any changes here should signify a change in major version number
def test_get_user_email():
    """The system needs to get user's email to send them an email."""
    my_user = user.User("Christopher", "Chris@chris.com")
    email = my_user.get_email_address()
    assert email == "Chris@chris.com"


def test_create_text_prophecy():
    """The user should be able to create a text prophecy"""
    my_user = user.User("Christopher", "Chris@chris.com")
    my_user.create_text_prophecy()
    assert my_user.prophecy_given is True


def test_create_photo_prophecy():
    """The user should be able to create a text prophecy"""
    my_user = user.User("Christopher", "Chris@chris.com")
    my_user.create_photo_prophecy()
    assert my_user.prophecy_given is True


def test_provide_supplicant_id():
    """The system needs to be able to provide a supplicant ID to the user."""
    my_user = user.User("Christopher", "Chris@chris.com")
    my_user.provide_supplicant_id(2)
    assert my_user.supplicant_id == 2


def test_is_weekly_work_done_yes():
    """The system needs to be able to check whether the work is all done.

    Not the purpose of an API unit test, but note to self: internally this will probably check to see if\
    all 3 bool variables are true."""
    my_user = user.User("Christopher", "Chris@chris.com")
    my_user.prophecy_given = True
    my_user.prophecy_received = True
    my_user.prophecy_received_and_interacted = True
    completed = my_user.is_practicum_complete()
    assert completed is True


def test_is_weekly_work_done_no():
    """The system needs to be able to check whether the work is all done.

    Not the purpose of an API unit test, but note to self: internally this will probably check to see if\
    all 3 bool variables are true."""
    my_user = user.User("Christopher", "Chris@chris.com")
    my_user.prophecy_given = True
    my_user.prophecy_received = True
    my_user.prophecy_received_and_interacted = True
    completed = my_user.is_practicum_complete()
    assert completed is False


def test_alert_user_to_prophecy_for_reading():
    """The system needs to let the user know they have received a prophecy."""
    my_user = user.User("Christopher", "Chris@chris.com")
    my_user.prophecy_ready_to_read()
    assert my_user.prophecy_received is True


def test_update_email_address():
    """The system should allow the user to update their email address."""
    my_user = user.User("Christopher", "Chris@chris.com")
    my_user.change_email_address("NewChris@chris.com")
    assert my_user.email == "NewChris@chris.com"


def test_update_username():
    """The system should allow the user to update their name."""
    my_user = user.User("Christopher", "Chris@chris.com")
    my_user.change_name("John")
    assert my_user.name == "John"
