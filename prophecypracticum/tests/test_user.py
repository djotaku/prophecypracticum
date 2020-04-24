"""Test user methods."""

from prophecypracticum.engine import user


def test_user_creation():
    """Create a user and check values."""
    my_user = user.User("Christopher", "Chris@chris.com")
    assert my_user.name == "Christopher"
    assert my_user.email == "Chris@chris.com"
    assert my_user.my_id == 0
    assert my_user.prophecy_given is False
    assert my_user.prophecy_received_and_interacted is False


